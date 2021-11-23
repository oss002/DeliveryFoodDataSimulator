from random import *


DATE = ['월','화','수','목','금','토','일']
DT_LIMIT_PRICE = [7000,8000,9000,10000,11000,12000,13000,14000,15000,17000,18000,19000,20000,21000,22000]
TIP = [0,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000]
DISCOUNT = [0,1000,2000,5000]
AD_LIMIT_PRICE = [0,10000,15000,30000]

#STORE_OP_TIME, DERIVERY_TIP, APP_DISCOUNT
#requires number of stores, and number of Delivery app


def makeData1(num_stores, num_delApp, STORE_OP_TIME[], DERIVERY_TIP[], APP_DISCOUNT[]) {
    for i in range(0,num_stores) {
        op_time_week = randint(10,17)
        working_hour_week = randint(10,15)
        close_time_week = min(op_time_week+working_hour_week,4+24) % 24

        week_break = randint(15,16)
        week_break_end= randint(16,17)

        op_time_weekend = randint(9,15)
        working_hour_weekend = randint(12,18)
        close_time_weekend = min(op_time_weekend+working_hour_weekend,4+24) % 24

        #STORE_OP_TIME
        for j in range(0,7) {
            if(j < 5) {
                STORE_OP_TIME[i+j] = {'O_S_ID': i,'O_DATE':DATE[j],'O_START_TIME':op_time_week,'O_CLOSE_TIME':close_time_week,'O_BREAK_TSTART':week_break , 'O_BREAK_END':week_break_end}
            } else {
                STORE_OP_TIME[i+j] = {'O_S_ID': i,'O_DATE':DATE[j],'O_START_TIME':op_time_weekend,'O_CLOSE_TIME':close_time_weekend,'O_BREAK_TSTART':week_break , 'O_BREAK_END':week_break_end}
            }
        }

        #DERIVERY_TIP, APP_DISCOUNT
        for j in range(0, num_delApp) {
            DERIVERY_TIP[i+j] = {'DT_APP_ID':j,'DT_S_ID':i,'DT_PRICE':DT_LIMIT_PRICE[randint(0,length(DT_LIMIT_PRICE)]),'DEL_TIP':TIP[randint(0,length(TIP))]}
            APP_DISCOUNT[i+j] = {'AD_APP_ID':j,'AD_S_ID':i,'AD_PRICE':AD_LIMIT_PRICE[0],'AD_DISCNT':DISCOUNT[0]}
        }
    }
}


#REVIEW, USER

def makeData2(num_review, num_user, REVIEW[], USER[]) {
    nameList = open('/wordlist/usernames.txt','r').readlines()
    passwordList = open('/wordlist/ssh_passwd.txt','r').readlines()

    
    

}


STORE_OP_TIME[]


#create jsonFile
