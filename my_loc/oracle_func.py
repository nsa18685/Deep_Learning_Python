
# coding: utf-8

# In[ ]:

from calendar import monthrange
import datetime
from dateutil.relativedelta import relativedelta
    
def initcap(data):
    return data[0].upper() + data[1:].lower()

def substr(data,n1,n2):
    return data[(n1-1):((n1+n2)-1)]

def lpad(string, num, st):
    return st * (num-len(string)) + string

def rpad(string, num, st):
    return string + st * (num-len(string))

def instr(data, w):
    for i in range(len(data)):
        if data[i] == w :
            return i+1
    return 'null'

def nvl(val1,val2):
    if val1 is '':
        return val2
    return val1

def decode(base, if_, eq, n_eq):
        if base == if_:
            return eq
        else:
            return n_eq

# 날짜 함수        
def months_between(date1, date2):

    dt1 = datetime.datetime.strptime(date1,'%Y-%m-%d')
    dt2 = datetime.datetime.strptime(date2,'%Y-%m-%d')
    
    
    year_b = abs(dt1.year - dt2.year)
    if dt1.month > dt2.month: 
        month_b = year_b*12 + (dt1.month - dt2.month)
    else:
        month_b = year_b*12 - (dt1.month - dt2.month)
        
    return month_b

def add_months(date,add):
    
    return datetime.datetime.strptime(date, '%Y-%m-%d') + relativedelta(months = +int(3))

def next_day(date,day):
    
    days = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
#     dic_ = {'월요일':0,'화요일':1,'수요일':2,'목요일':3,'금요일':4,'토요일':5,'일요일':6}
    
    date2 = datetime.datetime.strptime(date, '%Y-%m-%d')
    num1 = date2.weekday()
    num2 = days.index(day)
#     num2 = dic_[day]
    dif = (7 + (num2-num1))%7   # from. 수학과
    date3 = date2 + datetime.timedelta(days = dif)
    return str(date3)[:11]

def last_day(date):

    year = datetime.datetime.strptime(date, '%Y-%m-%d').year
    month = datetime.datetime.strptime(date, '%Y-%m-%d').month
    return date[:8] + str(monthrange(year, month)[1])

