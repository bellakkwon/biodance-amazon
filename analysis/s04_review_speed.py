"""02 · Reviews per day since the listing appeared on Keepa (free view, up to 2026-11-23).

Whether variants share one review count matters: the jelly mist shares reviews with the PDRN mist,
so it is left out. Eye patch variants show separate rating counts; four serums share one.
"""
from common import check, load


def run():
    k = load("keepa_summary_2026-11-23.csv").set_index("form")
    bio = k[k.brand == "biodance"]
    eye, serum = bio.loc["hydrogel eye patch"], bio.loc["serum"]
    check("02", "하루 리뷰 수 아이패치 vs 세럼", f"{eye.reviews_per_day} vs {serum.reviews_per_day}", "20.6 vs 6.0")
    check("02", "배수", f"{eye.reviews_per_day / serum.reviews_per_day:.1f}배", "3.4배")
    cat = load("catalog_2026-11-22.csv")
    eye_r = cat[cat.form == "eye patch"].ratings.astype(int).tolist()
    check("02", "아이패치 변형별 평가 수(서로 다름)", " · ".join(f"{r:,}" for r in eye_r), "6,600 · 2,600 · 493")
    serum_shared = int((cat[cat.form == "serum"].ratings == 2800).sum())
    check("02", "평가 수 2,800을 함께 쓰는 세럼 변형", serum_shared, 4)
    check("02", "구매 배지 아이패치(콜라겐) vs 세럼 전체",
          f"{cat.loc[cat['product'].str.startswith('Hydrogel Eye Patches Collagen'), 'bought_past_month'].iloc[0] / 10000:g}만+ vs "
          f"{cat[cat.form == 'serum'].bought_past_month.sum() / 10000:g}만+", "8만+ vs 1.86만+")


if __name__ == "__main__":
    run()
