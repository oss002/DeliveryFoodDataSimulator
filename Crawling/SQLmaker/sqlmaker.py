import json
import random

import pymysql.cursors


def insertsql_from_json():
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306, user="root",  # ex) root
        password="Kkj0405love!",
        database="Delivery_DB",
        charset='utf8'
    )

    # Cursor Object 가져오기
    cursor = conn.cursor()

    with open('./Data.json', encoding='utf-8') as json_file:
        json_data = json.load(json_file)
        json_store = json_data['menu']

        for a in json_store:
            if a['as_price'] == '':
                a['as_price'] = '5000'

            m_id = a['m_id']

            as_price = int(a['as_price'])
            range = int(as_price / 3)
            ass_price = as_price + random.randrange(-range+1, range+2)
            asss_price = as_price + random.randrange(-range+1, range+2)
            assss_price = as_price + random.randrange(-range+1, range+2)

            sql = "INSERT IGNORE INTO app_sell(aapp_id, am_id, as_price) VALUES (%s, %s, %s)"
            val = (0, m_id, as_price)
            cursor.execute(sql, val)
            conn.commit()

            sql = "INSERT IGNORE INTO app_sell(aapp_id, am_id, as_price) VALUES (%s, %s, %s)"
            val = (1, m_id, ass_price)
            cursor.execute(sql, val)
            conn.commit()

            sql = "INSERT IGNORE INTO app_sell(aapp_id, am_id, as_price) VALUES (%s, %s, %s)"
            val = (2, m_id, asss_price)
            cursor.execute(sql, val)
            conn.commit()

            sql = "INSERT IGNORE INTO app_sell(aapp_id, am_id, as_price) VALUES (%s, %s, %s)"
            val = (3, m_id, assss_price)
            cursor.execute(sql, val)
            conn.commit()


    print(cursor.rowcount, "record inserted")



insertsql_from_json()


