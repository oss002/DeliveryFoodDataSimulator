# Delivery Food Data Simulator

## 배달 음식 데이터 시뮬레이터

### 개요
설계된 relational model 에서 일정 부분은 요기요(https://www.yogiyo.co.kr/mobile/#/)에서 크롤링 하여 얻어지고, 나머지는 임의로 제작된다. 크롤링 및 제작된 데이터는 json 파일로 반환된다.

### Relational Model

#### Entity
1) STORE : 음식점 정보를 가지는 Entity type
- S_ID : 각 음식점을 식별하기 위한 ID 값 [key]
- S_NAME : 음식점의 이름
- ADDRESS : 음식점의 주소
- S_PHONE : 음식점의 전화번호
- ORDER_N : 음식점의 누적 주문 횟수
2) STORE_OP_TIME : 음식점 별 영업시간에 대한 정보를 가지는 Entity type
- O_S_ID : 음식점의 ID값 [key]
- O_DATE : 음식점의 영업 시간 별 영업 날짜(요일) [key]
- O_START_TIME : 해당 요일(O_DATE 값)에 대한 영업 시작 시간
- O_CLOSE_TIME : 해당 요일(O_DATE 값)에 대한 영업 종료 시간
- O_BREAK_TIME : 해당 요일(O_DATE 값)에 대한 브레이크 타임 시작 시간
- O_BREAK_END : 해당 요일(O_DATE 값)에 대한 브레이크 타임 종료 시간
3) MENU : 각 음식점 별로 판매하는 메뉴에 대한 정보를 저장하는 Entity type
- M_NAME : 메뉴 이름
- M_ID : 메뉴를 식별하기 위한 ID 값 [key]
- MS_ID : 해당 메뉴를 판매하는 가게의 ID값
- CATEGORY : 해당 메뉴의 분류
- SPICY : 해당 메뉴의 맵기
- INGREDIENT : 해당 메뉴에 들어간 주 재료
4) USER : 서비스 사용자의 정보를 가지는 Entity type
- U_ID : 각 유저를 식별하기 위한 ID값
- ID : 유저가 로그인 시 사용하는 ID
- PW : 유저가 로그인 시 사용하는 PW
- NAME : 유저의 이름
- NICKNAME : 유저의 닉네임
5) REVIEW : 사용자가 작성한 리뷰에 대한 정보를 가지는 Entity type
- REVIEW_ID : 각 리뷰를 식별하기 위한 ID값
- RS_ID : 해당 리뷰가 달린 가게의 ID값
- RU_ID : 해당 리뷰를 작성한 유저의 ID값
- POINTS : 리뷰에서 부여한 별점 정보
- COMMENTS : 작성한 리뷰의 내용
6) DEL_APP : 배달 어플에 대한 정보를 가지는 Entity type
- APP_ID : 배달 어플을 식별하기 위한 ID값
- APP_NAME : 배달 어플의 이름

#### Relationship 
1) OPERATION : 가게와 해당 가게의 운영 시간 정보 간의 relationship
2) SELL : 가게와 해당 가게에서 판매하는 메뉴들 간의 relationship
3) APP_DISCOUNT : 배달 어플 별 음식점의 할인 정보에 대한 relationship
- AD_APP_ID : 배달 어플의 ID값
- AD_S_ID : 가게의 ID값
- AD_PRICE : 속한 배달어플 및 가게에 따른 할인 기준 가격
- AD_DISCNT : 할인 기준 가격에 따른 할인 가격
4) DELIVERY TIP : 배달 어플 별 음식점의 배달 팁 정보에 대한 relationship
- DT_APP_ID : 배달 어플의 ID값
- DT_S_ID : 가게의 ID값
- DT_PRICE : 속한 배달어플 및 가게에 따른 배달팁 기준 가격
- DEL_TIP : 배달팁 기준 가격에 따른 배달팁
5) APP_SELL : 어플 별로 판매하는 메뉴의 가격이 다른 경우를 고려하기 위한 relationship
- AAPP_ID : 배달 어플의 ID값
- AM_ID : 가게의 ID값
- PRICE(AS_PRICE) : 배달 어플 별 메뉴의 가격
6) RATING : 가게와 해당 가게의 리뷰에 대한 relationship
7) CONTRIBUTE : 리뷰와 해당 리뷰의 작성자 간의 relationship
