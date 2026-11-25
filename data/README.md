# data

모두 미국 Amazon 공개 화면에서 기록한 값입니다. 판매량·매출 같은 내부 데이터는 없습니다.

## catalog_2026-11-22.csv

바이오던스 Amazon 리스팅 59개 (2026-11-22, Amazon 검색 결과).

| 열 | 뜻 |
|---|---|
| form | 형태 (sheet mask = 하이드로겔 마스크, eye patch, neck patch, mist, serum …) |
| ingredient | 대표 성분 (collagen, caviar PDRN …) |
| rating · ratings | 별점 · 평가 수 |
| bought_past_month | "지난달 N+ 구매" 배지의 하한 (50K+ → 50000). 배지가 없으면 빈 칸 = 0으로 계산 |
| price_usd · discount_pct | 기록일 판매가 · 표시된 할인율 |
| note | Best Seller 배지, "ratings shared"(다른 변형과 평가 공유) 등 |

배지의 합은 하한의 합이라 실제 판매 구성비가 아닙니다.

## bestsellers_top50_2026-11-23.csv

Amazon US Best Sellers 마스크·아이·세럼 카테고리 1–50위 (2026-11-23 하루, 블랙프라이데이 주간). 화면을 보고 브랜드를 기록했습니다.

| 열 | 뜻 |
|---|---|
| category · rank · brand | 카테고리 · 순위 · 브랜드 (`(무브랜드)` = 브랜드 표기 없음) |
| pdrn_in_title | 제목에 PDRN이 있음 |
| collagen_in_title | (마스크만) 제목에 Collagen이 있음 |
| other_brand_bio_collagen_name | (마스크만) 바이오던스가 아닌데 ‘Bio-Collagen’ 이름을 씀 |

## eye_patch_daily_rank_price.csv

바이오던스·메디큐브 아이패치의 일별 순위·가격 (ParseShelf, 2026-09-28 – 11-23).

| 열 | 뜻 |
|---|---|
| bpc_rank | Beauty & Personal Care 전체 순위 |
| skincare_rank | Skin Care 순위 (2026-11-01부터 기록) |
| price · rating · reviews | 판매가 · 별점 · 누적 리뷰 수 |

메디큐브는 10/8부터 기록이 있고, 11/9–11 가격과 11/12–17 행이 없습니다. 빈 날은 채우지 않았습니다.

## keepa_summary_2026-11-23.csv

바이오던스·메디큐브 주요 리스팅의 Keepa 무료 화면 요약. `reviews_per_day` = 누적 리뷰 수 ÷ Keepa 기록 시작 후 일수. `variations` = 변형 수.

## eye_reviews_coded.csv

바이오던스 콜라겐 아이패치 미국 리뷰 385건의 분류표. 리뷰 원문과 작성자 이름은 없습니다. `tools/code_eye_reviews.py`가 비공개 원본에서 만듭니다.

- **표본:** 최신순 100건 + 별점 필터별 최신순 100건(2점은 38건이 전부), 중복 제거, 미국만. 저평점이 실제보다 많습니다.
- **키워드 열:** `makeup_mention` = make-up·foundation·concealer·sunscreen·SPF. `tag_*` = 원본 파일의 키워드 태그.
- **사람이 읽고 분류한 열:** `use_morning` · `use_night`(본인이 그 시간에 쓴다고 쓴 리뷰만), `use_frequency`(매일 / 그보다 적게, 사용 빈도를 적은 리뷰만), `wear_time`(리뷰에 적힌 착용 시간: 15분 기준 / 20–30분), `face_mask_compare`(바이오던스 마스크와 비교), `dried_swollen_after_sleep`(붙인 채 잠들어 마르거나 부음). 해당 리뷰 번호와 제외 이유는 스크립트에 적혀 있습니다.

## 파일 없이 인용한 숫자

| 숫자 | 출처 | 보고서 |
|---|---|---|
| PDRN 인기 +322% (2025.03–2026.02) | Spate 2026 Ingredients Report | 01 |
| 콜라겐 마스크 +52.9% · 언더아이 마스크 +52.5% (성장 예측 2·3위) | Spate 2026 Beauty & Wellness Predictions | 01 |
| ‘#15-min Magic’ · ‘#Makeup-Ready Skin’ · ‘Busy Mornings’ | 아이패치 상세페이지의 마스크 비교 이미지 (2026-11-23) | 00·04 |
| Remove after 20–30 minutes | 같은 페이지 How to Use | 00·03·04 |
| 작은 부위에 10–15분 테스트 (사용 시간 아님) | 같은 페이지 Safety Information | 04 |
| 메디큐브 아이패치 4–5월·8–9월 $17–18 할인, 11월 최저 $15.33 | Keepa 가격 그래프 | 03 |
