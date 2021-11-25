import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import json
import time
import random

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

PATH = './chromedriver.exe'
driver = webdriver.Chrome(PATH)  # 크롬 드라이버 실행하기

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

menu_id = 0
store_id = 0

data = {'store': [], 'menu': []}
check_store = []


def insert_target(target: str):  # 검색할 주소 입력 함수
    xpath = '//*[@id="search"]/div/form/input'
    element = driver.find_element(By.XPATH, xpath)
    element.clear()
    time.sleep(3)
    element.send_keys(target)
    time.sleep(1)


def search():  # 검색 버튼 누르기용 함수
    search_xpath = '//*[@id="button_search_address"]/button[2]'
    driver.find_element(By.XPATH, search_xpath).click()


def to_bottom():  # 스크롤 가장 아래로 내리기 함수
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")  # 스크롤을 가장 아래로 내린다
    time.sleep(2)
    pre_height = driver.execute_script("return document.body.scrollHeight")  # 현재 스크롤 위치 저장

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")  # 스크롤을 가장 아래로 내린다
        time.sleep(1)
        cur_height = driver.execute_script("return document.body.scrollHeight")  # 현재 스크롤을 저장한다.
        if pre_height == cur_height:
            break
        pre_height = cur_height


def crawl_store_data(s_id: int, category: str):  # 음식점 정보(id, name, address, phone, order number) 크롤링
    # 음식점 이름 (store_name)
    store_name = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div[1]/div[1]/span').text
    print("s_name: " + store_name)

    if not (store_name in check_store):  # store 중복 체크
        check_store.append(store_name)
        global store_id
        store_id += 1
        # 음식점 id (store_id) -> 크롤링 순서대로
        print("s_id: " + str(s_id))

        crawl_menu(s_id, category)  # 해당 음식점의 메뉴 및 가격 크롤링하기

        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/ul/li[3]/a').click()
        time.sleep(2)

        # 음식점 주소(store_address)
        store_address = driver.find_element(By.XPATH, '//*[@id="info"]/div[2]/p[3]/span').text
        print("address: " + store_address)

        # 음식점 전화번호(store_phone)
        store_phone = driver.find_element(By.XPATH, '//*[@id="info"]/div[2]/p[2]/span').text
        store_phone = store_phone.split(' ')[0]
        print("s_phone: " + store_phone)

        # 음식점 주문횟수(store_order) -> random 값
        store_order = random.randrange(100, 50000)
        print("s_order: " + str(store_order))

        data['store'].append({'s_id': s_id, 's_name': store_name, 'address': store_address, 's_phone': store_phone,
                              'order_n': store_order})


def crawl_menu(mstore_id: int, category_str: str):  # 음식점 탭 접속 후 메뉴 크롤링
    global menu_id
    category = driver.find_elements(By.CLASS_NAME, 'panel-title')

    if category:
        try:
            del category[0]
            del category[-1]
        except IndexError:
            return

    try:
        for cate in range(len(category)):
            category[cate].click()
    except selenium.common.exceptions.ElementNotInteractableException:
        pass
    except selenium.common.exceptions.ElementClickInterceptedException:
        pass

    j = 3
    while j < len(category) + 2:
        find_name = '// *[ @ id = "menu"] / div / div[' + str(
            j) + '] / div[2] / div / ul / li / table / tbody / tr / td[1] / div[2]'
        name = driver.find_elements(By.XPATH, find_name)
        find_price = '// *[ @ id = "menu"] / div / div[' + str(
            j) + '] / div[2] / div / ul / li / table / tbody / tr / td[1] / div[4] / span[1]'
        price = driver.find_elements(By.XPATH, find_price)

        for k in range(len(name)):
            menu_id += 1
            # 메뉴 이름 (m_name in menu)
            m_name = name[k].text
            # 메뉴 id (m_id in menu)
            m_id = menu_id
            # 메뉴 판매 가게 id (ms_id in menu)
            ms_id = mstore_id
            # 메뉴 가격 (as_price in app_sell)
            as_price = price[k].text.replace("원", "").replace(",", "")
            # 메뉴 카테고리 (category)
            category = category_str
            # 매운정도(1~3단계로 분류 / spicy in menu)
            spicy = 0
            if name[k].text.find("매운") > 0 or name[k].text.find("핫") > 0 or name[k].text.find("레드") > 0 or name[
                k].text.find("청양") > 0 or (name[k].text.find("불") > 0 and name[k].text.find("불고기") < 0) or name[
                k].text.find("hot") > 0 or name[k].text.find("맵") > 0 or name[k].text.find("매") > 0:
                spicy = 3
            elif name[k].text.find("양념") > 0 or name[k].text.find("얼큰") > 0 or name[k].text.find("짬뽕") > 0 or name[
                k].text.find("떡볶이") > 0 or name[k].text.find("고추") > 0:
                spicy = 2
            else:
                spicy = 1

            data['menu'].append({'m_name': m_name, 'm_id': m_id, 'ms_id': ms_id, 'category': category, 'spicy': spicy,
                                 'as_price': as_price})
        j += 1


# 시작점!

# 카테고리
search_division = ['치킨', '피자양식', '중식', '한식', '일식돈까스', '족발보쌈', '야식', '분식', '카페디저트']

# 아주대, 경희대 국제, 성균관대 자연, 단국대 인근
search_location = ['경기도 수원시 영통구 원천동 산 5-1 아주대학교', '경기도 안성시 대덕면 내리 72-1 중앙대학교',
                   '경기도 용인시 수지구 죽전동 1491 단국대학교','경기도 성남시 수정구 복정동 620-2 가천대학교']

for location in search_location:

    # 주소 입력
    driver.get('https://www.yogiyo.co.kr/mobile/#/')
    driver.implicitly_wait(2)
    insert_target(location)

    # 검색
    search()
    time.sleep(1)
    curr_url = driver.current_url

    for division in search_division:
        print(division)
        driver.get(curr_url + division + "/")
        time.sleep(2)

        # 스크롤 가장 아래로
        to_bottom()
        time.sleep(1)

        category_stores = driver.find_elements(By.XPATH, '//*[@id="content"]/div/div[4]/div/div[2]/div/div')
        limit = len(category_stores)
        i = 1

        while i <= limit:

            click_xpath = '//*[@id="content"]/div/div[4]/div/div[2]/div['+str(i)+']/div'

            while True:
                try:
                    driver.find_element(By.XPATH, click_xpath).click()
                except selenium.common.exceptions.NoSuchElementException:
                    s_pre_height = driver.execute_script("return document.body.scrollHeight")  # 현재 스크롤 위치 저장
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")  # 스크롤을 가장 아래로 내린다
                    time.sleep(5)
                    s_cur_height = driver.execute_script("return document.body.scrollHeight")  # 현재 스크롤을 저장한다.

                    try:
                        driver.find_element(By.XPATH, click_xpath).click()
                    except selenium.common.exceptions.NoSuchElementException:
                        if s_pre_height == s_cur_height:
                            break
                        else:
                            continue
                    else:
                        time.sleep(4)
                        crawl_store_data(store_id, division)
                        break
                except selenium.common.exceptions.ElementClickInterceptedException:
                    break
                except:
                    break
                else:
                    time.sleep(4)
                    crawl_store_data(store_id, division)
                    break

            i += 1
            driver.get(curr_url + division + "/")
            time.sleep(3)



# JSON 파일 생성
with open('Data2.json', 'w', encoding='utf-8') as make_file:
    json.dump(data, make_file, ensure_ascii=False, indent='\t')

# JSON 파일 테스트
with open("Data.json", "r", encoding="utf8") as f:
    contents = f.read()  # string 타입
    json_data = json.loads(contents)

    print(json_data["store"][0]["s_name"])
