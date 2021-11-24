import random
import os
import math
import json

#load Data from /lists
idList = open('lists/usernames.txt','r')
ID = []
while True:
    line = idList.readline()
    if not line: break
    if len(line) > 4 : ID.append(line[:-1])

temp = math.ceil(len(ID)/2)
NICKNAME = ID[0:temp]
ID = ID[temp:len(ID)]

passwordList = open('lists/ssh_passwd.txt','r',encoding='UTF8')
PASSWORD = []
while True:
    line = passwordList.readline()
    if not line: break
    PASSWORD.append(line[:-1])

nameList = open('lists/namelist.txt','r')
NAME= []
while True:
    line = nameList.readline()
    if not line: break
    NAME.append(line[:-1])


DATE = ['월','화','수','목','금','토','일']
DT_LIMIT_PRICE = [7000,8000,9000,10000,11000,12000,13000,14000,15000,17000,18000,19000,20000,21000,22000]
TIP = [0,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000]
DISCOUNT = [0,1000,2000,5000]
AD_LIMIT_PRICE = [0,10000,15000,30000]

#STORE_OP_TIME, DERIVERY_TIP, APP_DISCOUNT
#requires number of stores, and number of Delivery app
def makeData1(num_stores, num_delApp, STORE_OP_TIME, DERIVERY_TIP, APP_DISCOUNT) :
    for i in range(0,num_stores) :
        op_time_week = random.randrange(10,18)
        working_hour_week = random.randrange(10,16)
        close_time_week = min(op_time_week+working_hour_week,4+24) % 24

        week_break = random.randrange(15,17)
        week_break_end= random.randrange(16,18)

        op_time_weekend = random.randrange(9,16)
        working_hour_weekend = random.randrange(12,19)
        close_time_weekend = min(op_time_weekend+working_hour_weekend,4+24) % 24

        #STORE_OP_TIME
        for j in range(0,7):
            if(j < 5):
                STORE_OP_TIME.append({'O_S_ID': i,'O_DATE':DATE[j],'O_START_TIME':op_time_week,'O_CLOSE_TIME':close_time_week,'O_BREAK_TSTART':week_break , 'O_BREAK_END':week_break_end})
            else :
                STORE_OP_TIME.append({'O_S_ID': i,'O_DATE':DATE[j],'O_START_TIME':op_time_weekend,'O_CLOSE_TIME':close_time_weekend,'O_BREAK_TSTART':week_break , 'O_BREAK_END':week_break_end})


        #DERIVERY_TIP, APP_DISCOUNT
        for j in range(0, num_delApp) :
            DERIVERY_TIP.append({'DT_APP_ID':j,'DT_S_ID':i,'DT_PRICE':DT_LIMIT_PRICE[random.randrange(0,len(DT_LIMIT_PRICE))],'DEL_TIP':TIP[random.randrange(0,len(TIP)-1)]})
            APP_DISCOUNT.append({'AD_APP_ID':j,'AD_S_ID':i,'AD_PRICE':AD_LIMIT_PRICE[0],'AD_DISCNT':DISCOUNT[0]})


#REVIEW, USER
#requires number of review, and number of user
def makeData2(num_review, num_user, REVIEW, USER) :
    random.shuffle(NICKNAME)
    random.shuffle(ID)
    random.shuffle(PASSWORD)
    random.shuffle(NAME)
    for i in range(0,num_user):
        USER.append({'U_ID':i,'ID':ID[i],'PW':PASSWORD[i],'NAME':NAME[i],'NICKNAME':NICKNAME[i]})
        
    for j in range(0,num_review):
        temp_storeID = random.randrange(1,1001)
        temp_userID = random.randrange(1,num_user+1)
        temp_point = random.randrange(1,6)
        REVIEW.append({'REVIEW_ID':j, 'RS_ID': temp_storeID, 'RU_ID':temp_userID, 'POINTS':temp_point})


# Lists that are going to be transfer to json
STORE_OP_TIME=[]
DERIVERY_TIP=[]
APP_DISCOUNT=[]
REVIEW=[]
USER=[]

makeData1(8000,4,STORE_OP_TIME, DERIVERY_TIP, APP_DISCOUNT)
makeData2(1000,1000,REVIEW,USER)

print(STORE_OP_TIME[10])
print(DERIVERY_TIP[10])
print(APP_DISCOUNT[10])
print(REVIEW[10])
print(USER[10])

print(len(STORE_OP_TIME))
print(len(DERIVERY_TIP))
print(len(APP_DISCOUNT))
print(len(REVIEW))
print(len(USER))

#create jsonFile
with open('STORE_OP_TIME.json','w',encoding='utf-8') as file:
    json.dump(STORE_OP_TIME, file, ensure_ascii=False, indent='\t')

with open('DERIVERY_TIP.json','w',encoding='utf-8') as file:
    json.dump(DERIVERY_TIP, file, ensure_ascii=False, indent='\t')

with open('APP_DISCOUNT.json','w',encoding='utf-8') as file:
    json.dump(APP_DISCOUNT, file, ensure_ascii=False, indent='\t')

with open('REVIEW.json','w',encoding='utf-8') as file:
    json.dump(REVIEW, file, ensure_ascii=False, indent='\t')

with open('USER.json','w',encoding='utf-8') as file:
    json.dump(USER, file, ensure_ascii=False, indent='\t')
