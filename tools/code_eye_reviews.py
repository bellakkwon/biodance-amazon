"""Turn the private eye-patch review file into a coded table without review text or reviewer names.

Usage:
    python tools/code_eye_reviews.py PATH_TO_PRIVATE_REVIEW_XLSX

Input  : the review workbook copied from Amazon on 2026-11-23 (sheet "리뷰 전체").
         It holds review text and reviewer names, so it is NOT in this repository.
Output : data/eye_reviews_coded.csv, one row per US review, flags only.

Keyword flags are found by regular expression. Time of use, face-mask comparison and
"dried or swollen after sleeping in them" need reading the review, so those are listed
by review number below together with the reason, and anyone with the source file can
check them.
"""
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

MAKEUP = r"(?i)make-?up|foundation|concealer|sunscreen|spf"

# Read and classified by hand. Count only reviewers who say they themselves use the
# patches at that time.
MORNING = {5, 36, 58, 103, 109, 120, 223, 322, 393}
NIGHT = {42, 53, 77, 148, 255, 263, 383, 389}
TIME_EXCLUDED = {
    83: "says 'getting ready in the morning or winding down at night' in general terms",
    45: "wishes to sleep with them, not actual use",
    103: "night: wishes to sleep with them (counted as morning use only)",
    363: "'overnight' refers to a different Biodance product",
    245: "'leaving it to soak in overnight' is unclear about the patch itself",
    191: "woke up with puffy eyes, use time not stated",
    54: "describes waking up with bags, use time not stated",
    405: "'after a late night out', use time not stated",
}
# Compares the eye patches with Biodance face masks (not just mentions a mask).
FACE_MASK_COMPARE = {46, 200, 348, 363, 410}
# Fell asleep with them on, then dried out or swelled.
DRIED_SWOLLEN_AFTER_SLEEP = {263, 383}


def main(src):
    d = pd.read_excel(src, sheet_name="리뷰 전체")
    d = d[d["국가"] == "미국"].copy()
    text = d["제목"].fillna("") + " " + d["본문"].fillna("")
    tags = d["태그"].fillna("")
    out = pd.DataFrame({
        "review_no": d["No"].astype(int),
        "date": pd.to_datetime(d["작성일"]).dt.date,
        "star": d["별점"].astype(int),
        "sample_source": d["수집 출처"],
        "makeup_mention": text.str.contains(MAKEUP, regex=True),
        "tag_pilling_residue": tags.str.contains("필링", regex=False),
        "tag_no_effect": tags.str.contains("효과 체감 없음", regex=False),
        "tag_morning_use": tags.str.contains("아침 루틴 사용", regex=False),
        "tag_sleep_use": tags.str.contains("취침 중 사용", regex=False),
    })
    out["makeup_pilling"] = out.makeup_mention & out.tag_pilling_residue
    out["use_morning"] = out.review_no.isin(MORNING)
    out["use_night"] = out.review_no.isin(NIGHT)
    out["face_mask_compare"] = out.review_no.isin(FACE_MASK_COMPARE)
    out["dried_swollen_after_sleep"] = out.review_no.isin(DRIED_SWOLLEN_AFTER_SLEEP)
    missing = (MORNING | NIGHT | FACE_MASK_COMPARE | DRIED_SWOLLEN_AFTER_SLEEP | set(TIME_EXCLUDED)) - set(out.review_no)
    assert not missing, f"review numbers not in the US sample: {missing}"
    dst = ROOT / "data" / "eye_reviews_coded.csv"
    out.sort_values("review_no").to_csv(dst, index=False)
    print(f"wrote {dst} ({len(out)} reviews)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
