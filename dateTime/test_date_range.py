
import datetime as dt
import pandas as pd
 
# initializing date
test_date = dt.datetime.strptime("2020-01-01", "%Y-%m-%d")
 
# initializing K
K = 365
 
date_generated = pd.date_range(test_date, periods=K)
#print(date_generated.strftime("%Y-%m-%d"))
"""
Index(['2022-12-27', '2022-12-28', '2022-12-29', '2022-12-30', '2022-12-31'], dtype='object')
"""
# for i in date_generated.strftime("%Y-%m-%d"):
#     print(i)
"""
2022-12-27
2022-12-28
2022-12-29
2022-12-30 
2022-12-31
"""
# for i in date_generated.strftime("%Y%m%d"):
#     print(str(i))




# 시작날짜 설정
srtDate= dt.datetime.strptime("1996-05-25", "%Y-%m-%d")
# 인수 설정
K= 3143
date_generated = pd.date_range(srtDate, periods=K)

# 날짜 범위 리스트화
date_ls= []

# srtYMD기준 maxNum까지 하루 증감하면서 date_ls에 append
for i in date_generated.strftime("%Y%m%d"):
    # plusDate= srtdt + dt.timedelta(days=-i) 
    # YMD=plusDate.strftime('%Y%m%d')    
    date_ls.append(str(i))
date_ls.sort(reverse=True)
print(date_ls[:10   ])