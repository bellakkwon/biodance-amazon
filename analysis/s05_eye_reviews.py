"""03·04 · US eye patch reviews (385), coded without text. See tools/code_eye_reviews.py.

Sampling: newest 100 + newest 100 for each star filter (only 38 two-star reviews exist), duplicates
removed, US only. Low stars are over-represented, so these are counts, not rates.
"""
from common import check, load, note


def run():
    c = load("eye_reviews_coded.csv")
    check("04", "미국 리뷰 수 · 별점 구성", f"{len(c)} · " + " ".join(f"{s}점 {n}" for s, n in c.star.value_counts().sort_index().items()),
          "385 · 1점 83 2점 38 3점 70 4점 94 5점 100")
    mk = c[c.makeup_mention]
    check("00·04", "화장 언급 · 그중 5점", f"{len(mk)}건 · {int((mk.star == 5).sum())}건", "11건 · 0건")
    check("00·04", "화장 밀림(화장 언급 + 필링·잔여물 태그)", f"{int(c.makeup_pilling.sum())}건", "7건")
    check("04", "아침 사용 · 밤 사용", f"{int(c.use_morning.sum())} · {int(c.use_night.sum())}", "9 · 8")
    freq = c.use_frequency.fillna("")
    note("03", "사용 빈도를 적은 리뷰 중 매일 · 그보다 적게", f"{int((freq == 'daily').sum())} · {int((freq == 'less_than_daily').sum())}")
    wear = c.wear_time.fillna("").astype(str)
    check("04", "착용 시간 15분 기준 · 20–30분", f"{int((wear == '15').sum())} · {int((wear == '20-30').sum())}", "4 · 5")
    fm = c[c.face_mask_compare]
    check("04", "바이오던스 마스크와 비교 · 별점", f"{len(fm)}건 · {fm.star.min()}-{fm.star.max()}점", "5건 · 1-3점")
    check("04", "붙인 채 잠들어 마름·부음", f"{int(c.dried_swollen_after_sleep.sum())}건", "2건")
    check("04", "‘효과 체감 없음’ 태그", f"{int(c.tag_no_effect.sum())}건", "93건")


if __name__ == "__main__":
    run()
