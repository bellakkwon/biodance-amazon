"""Recompute every deck number from data/ and write outputs/numbers.md.

    python analysis/run_all.py
"""
import s01_catalog_badges
import s02_bestsellers
import s03_rank_price
import s04_review_speed
import s05_eye_reviews
import s06_sizing
from common import OUT, RESULTS

for m in (s01_catalog_badges, s02_bestsellers, s03_rank_price, s04_review_speed, s05_eye_reviews, s06_sizing):
    print(f"\n== {m.__name__}")
    m.run()

lines = ["# 덱 숫자 재계산 결과", "", "`python analysis/run_all.py`가 data/ 파일로 다시 계산한 값입니다.", "",
         "| 쪽 | 항목 | 재계산 | 덱 | 일치 |", "|---|---|---|---|---|"]
lines += [f"| {p} | {lab} | {got} | {deck} | {'✓' if ok else '✗'} |" for p, lab, got, deck, ok in RESULTS]
(OUT / "numbers.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
bad = [r for r in RESULTS if not r[4]]
print(f"\n{len(RESULTS) - len(bad)}/{len(RESULTS)} match -> outputs/numbers.md")
raise SystemExit(1 if bad else 0)
