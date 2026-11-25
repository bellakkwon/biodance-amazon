"""03·04 · Price per use and the size of a conversion change. Arithmetic on lower bounds, not a forecast."""
from common import check, load


def run():
    cat = load("catalog_2026-11-22.csv").set_index("product")
    mask = cat.loc["Bio-Collagen Real Deep Mask 4ea", "price_usd"] / 4
    patch = cat.loc["Hydrogel Eye Patches Collagen Peptide 60ct", "price_usd"] / 30  # 60 patches = 30 pairs
    check("03", "회당 가격 마스크 vs 아이패치(11/22 판매가)", f"${mask:.2f} vs ${patch:.2f}", "$3.50 vs $0.58")
    badge = cat.loc["Hydrogel Eye Patches Collagen Peptide 60ct", "bought_past_month"]
    list_price = 23.0
    units = [round(badge * p) for p in (0.01, 0.03, 0.05)]
    check("04", "판매 +1% · +3% · +5%일 때 월 추가 개수(배지 하한 8만+ 기준)", " · ".join(f"{u:,}" for u in units), "800 · 2,400 · 4,000")
    check("04", "+1%일 때 금액(정가 $23)", f"${units[0] * list_price / 10000:.1f}만", "$1.8만")


if __name__ == "__main__":
    run()
