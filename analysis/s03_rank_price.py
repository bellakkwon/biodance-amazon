"""00·03 · Eye patch ranks at full price vs the Black Friday discount day, and the October discount.

Daily rank and price recorded from ParseShelf (2026-09-28 to 11-23). Rank is not sales.
Skin Care ranks exist only from 2026-11-01; October uses the Beauty & Personal Care (BPC) rank.
Medicube has no price rows 11/9-11 and no rank rows 11/12-17.
"""
import pandas as pd

from common import check, load


def run():
    d = load("eye_patch_daily_rank_price.csv", parse_dates=["date"])
    days = pd.date_range("2026-11-01", "2026-11-19")
    bio = d[d.listing == "biodance_eye_patch"].set_index("date").reindex(days)
    med = d[d.listing == "medicube_eye_patch"].set_index("date").reindex(days)
    bio_full = bio.skincare_rank[bio.price >= 23.0]
    med_full = med.skincare_rank[med.price >= 21.9].dropna()
    check("00·03", "정가 기간(11/1-19) Skin Care 순위 중앙값 바이오던스 vs 메디큐브",
          f"{bio_full.median():g} vs {med_full.median():g}", "26 vs 70.5")
    check("03", "정가 기간 순위 범위", f"{bio_full.min():g}-{bio_full.max():g} vs {med_full.min():g}-{med_full.max():g}",
          "18-29 vs 55-79")
    day = d[d.date == "2026-11-23"].set_index("listing").skincare_rank
    check("03", "할인일(11/23) Skin Care 순위 메디큐브 vs 바이오던스",
          f"{day['medicube_eye_patch']:g} vs {day['biodance_eye_patch']:g}", "11 vs 12")
    check("03", "메디큐브 순위 기록 없는 날(11/1-19)", int(med.reviews.isna().sum()), 6)
    oct_ = d[(d.listing == "biodance_eye_patch") & (d.date <= "2026-10-31")].set_index("date")
    disc = oct_[oct_.price < 23]
    check("03", "10월 할인일 · 가격", f"{' '.join(disc.index.strftime('%m/%d'))} · ${disc.price.iloc[0]:.2f}", "10/07 10/08 · $17.50")
    after = oct_.loc["2026-10-09":"2026-10-20"]
    assert (after.price == 23.0).all()
    check("03", "할인 뒤 정가 기간 BPC 순위", f"{len(after)}일 · {after.bpc_rank.min():g}-{after.bpc_rank.max():g}위", "12일 · 18-24위")
    pre = oct_.loc[:"2026-10-06"].bpc_rank
    check("03", "할인 전 · 10/29 BPC 순위",
          f"{pre.min():g}-{pre.max():g}위 · {oct_.loc['2026-10-29', 'bpc_rank']:g}위", "46-57위 · 55위")


if __name__ == "__main__":
    run()
