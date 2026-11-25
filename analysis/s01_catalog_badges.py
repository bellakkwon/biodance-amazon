"""00·02 · Purchase badges by product form (Biodance catalog, 59 listings, 2026-11-22).

A badge ("50K+ bought in past month") is a lower bound shown by Amazon, not a sales count.
Listings without a badge count as 0. Sums of lower bounds are not a sales mix.
"""
from common import OUT, check, load

GROUP = {"sheet mask": "stick", "eye patch": "stick", "neck patch": "stick", "mist": "mist",
         "serum": "apply", "eye cream": "apply", "cream": "apply", "toner pad": "apply", "toner": "apply",
         "booster": "apply", "gua sha cream": "apply", "kit": "etc", "cleanser": "etc", "duo": "etc"}


def run():
    cat = load("catalog_2026-11-22.csv")
    assert len(cat) == 59 and set(cat.form) <= set(GROUP)
    cat["badge"] = cat.bought_past_month.fillna(0)
    by_form = cat.groupby("form").badge.sum().sort_values(ascending=False)
    total = by_form.sum()
    check("00", "마스크 구매 배지 합계(천 개+)", f"{by_form['sheet mask'] / 1000:g}+", "145+")
    check("00", "아이패치 구매 배지 합계(천 개+)", f"{by_form['eye patch'] / 1000:g}+", "110+")
    check("02", "전체 하한 합계", f"{total / 10000:.1f}만+", "36.8만+")
    grp = cat.groupby(cat.form.map(GROUP)).badge.sum() / total
    check("00·02", "붙이는 제품 3종 비중", f"{grp['stick']:.0%}", "77%")
    check("02", "미스트 · 바르는 제품 · 기타 비중",
          f"{grp['mist']:.1%} · {grp['apply']:.1%} · {grp['etc']:.0%}", "9.5% · 12.3% · 1%")
    pdrn_eye = cat[(cat.form == "eye patch") & (cat.ingredient == "caviar PDRN")].badge.iloc[0]
    check("02", "PDRN 아이패치 구매 배지", f"{pdrn_eye / 10000:g}만+", "2만+")
    top = cat.sort_values("badge", ascending=False).reset_index(drop=True)
    mist_rank = int(top.index[top.form == "mist"][0]) + 1
    check("02", "젤리 미스트 리스팅 순위 · 배지", f"{mist_rank}위 · {top.badge[mist_rank - 1] / 10000:g}만+", "3위 · 3만+")
    table = cat.pivot_table(index="form", columns="ingredient", values="badge", aggfunc="sum", fill_value=0) / 1000
    table.loc[by_form.index].to_csv(OUT / "form_by_ingredient_badges_k.csv")


if __name__ == "__main__":
    run()
