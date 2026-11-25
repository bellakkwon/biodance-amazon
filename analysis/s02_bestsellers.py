"""01 · Amazon US Best Sellers top 50 in three categories, one day (2026-11-23, Black Friday week).

Read from page screenshots. Counts are listings, not products: Biodance groups variants into one listing.
"""
from common import check, load


def run():
    b = load("bestsellers_top50_2026-11-23.csv")
    assert b.groupby("category").size().to_dict() == {"eye": 50, "mask": 50, "serum": 50}
    bio = b[b.brand == "Biodance"]
    check("01", "리스팅 수 메디큐브 vs 바이오던스", f"{(b.brand == 'medicube').sum()} vs {len(bio)}", "18 vs 4")
    ranks = " · ".join(f"{c} {r}위" for c, r in zip(bio.category, bio["rank"]))
    check("01", "바이오던스 순위", ranks, "mask 1위 · eye 3위 · eye 31위 · serum 43위")
    p = b[b.pdrn_in_title]
    split = f"{len(p)}개 (메디큐브 {(p.brand == 'medicube').sum()} · 우리 {(p.brand == 'Biodance').sum()} · 기타 {(~p.brand.isin(['medicube', 'Biodance'])).sum()})"
    check("01", "제목에 PDRN", split, "18개 (메디큐브 7 · 우리 1 · 기타 10)")
    m = b[b.category == "mask"]
    check("01", "마스크 50개 중 Collagen 제목 · 그중 다른 브랜드 Bio-Collagen",
          f"{m.collagen_in_title.sum()} · {m.other_brand_bio_collagen_name.sum()}", "20 · 4")


if __name__ == "__main__":
    run()
