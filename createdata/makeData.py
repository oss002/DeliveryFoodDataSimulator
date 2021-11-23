from random import *
import os
import math
#load Data from /lists
idList = open('lists/usernames.txt','r')
ID = []
while True:
    line = idList.readline()
    if not line: break
    if len(line) > 4 : ID.append(line)

temp = math.ceil(len(ID)/2)
NICKNAME = ID[0:temp]
ID = ID[temp:len(ID)]

passwordList = open('lists/ssh_passwd.txt','r',encoding='UTF8')
PASSWORD = []
while True:
    line = passwordList.readline()
    if not line: break
    PASSWORD.append(line)

nameList = open('lists/namelist.txt','r')
NAME= []
while True:
    line = nameList.readline()
    if not line: break
    NAME.append(line)


DATE = ['월','화','수','목','금','토','일']
DT_LIMIT_PRICE = [7000,8000,9000,10000,11000,12000,13000,14000,15000,17000,18000,19000,20000,21000,22000]
TIP = [0,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000]
DISCOUNT = [0,1000,2000,5000]
AD_LIMIT_PRICE = [0,10000,15000,30000]

#STORE_OP_TIME, DERIVERY_TIP, APP_DISCOUNT
#requires number of stores, and number of Delivery app
def makeData1(num_stores, num_delApp, STORE_OP_TIME, DERIVERY_TIP, APP_DISCOUNT) :
    for i in range(0,num_stores) :
        op_time_week = randint(10,17)
        working_hour_week = randint(10,15)
        close_time_week = min(op_time_week+working_hour_week,4+24) % 24

        week_break = randint(15,16)
        week_break_end= randint(16,17)

        op_time_weekend = randint(9,15)
        working_hour_weekend = randint(12,18)
        close_time_weekend = min(op_time_weekend+working_hour_weekend,4+24) % 24

        #STORE_OP_TIME
        for j in range(0,7):
            if(j < 5):
                STORE_OP_TIME.append({'O_S_ID': i,'O_DATE':DATE[j],'O_START_TIME':op_time_week,'O_CLOSE_TIME':close_time_week,'O_BREAK_TSTART':week_break , 'O_BREAK_END':week_break_end})
            else :
                STORE_OP_TIME.append({'O_S_ID': i,'O_DATE':DATE[j],'O_START_TIME':op_time_weekend,'O_CLOSE_TIME':close_time_weekend,'O_BREAK_TSTART':week_break , 'O_BREAK_END':week_break_end})


        #DERIVERY_TIP, APP_DISCOUNT
        for j in range(0, num_delApp) :
            DERIVERY_TIP.append({'DT_APP_ID':j,'DT_S_ID':i,'DT_PRICE':DT_LIMIT_PRICE[randint(0,length(DT_LIMIT_PRICE))],'DEL_TIP':TIP[randint(0,length(TIP))]})
            APP_DISCOUNT.append({'AD_APP_ID':j,'AD_S_ID':i,'AD_PRICE':AD_LIMIT_PRICE[0],'AD_DISCNT':DISCOUNT[0]})




#REVIEW, USER

def makeData2(num_review, num_user, REVIEW, USER) :
    random.shuffle(NICKNAME)
    random.shuffle(ID)
    random.shuffle(PASSWORD)
    random.shuffle(NAME)
    
    for i in (0,num_user):
        USER.append({'U_ID':i,'ID':ID[i],'PW':PASSWORD[i],'NAME':NAME[i],'NICKNAME':NICKNAME[i]})
        
    
        


    
    
#        USER.append({'U_ID':,'ID':,'PW':,'NAME':,'NICKNAME':
#         })

#       REVIEW.append({'REVIEW_ID':,'RS_ID':.'RU_ID':.'POINTS':,'COMMENTS':
#          })
    
    




# Lists that are going to be transfer to json
#STORE_OP_TIME=[]
#DERIVERY_TIP=[]
#APP_DISCOUNT=[]
#REVIEW=[]
#USER=[]





#create jsonFile

