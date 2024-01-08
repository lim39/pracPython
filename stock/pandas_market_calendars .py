import pandas_market_calendars as mcal
import pandas as pd
import warnings

'''
# Market Code # 
    XKRX : Korea
    XHKG : Hongkong
    JPX  : Japan
    SSE  : Sanghai
    NYSE : NewYork
'''

warnings.filterwarnings('ignore')


# 다른 마켓 코드 확인
calendar_name_ls = mcal.get_calendar_names()
print('########################## 다른 마켓 코드 확인 ##########################')
print(calendar_name_ls)
print('########################################################################\n\n\n')

start_date = '2023-12-01'
end_date = '2024-01-31'

# 한국 증시 캘린더
market_code= 'XKRX'
calendar_kor = mcal.get_calendar(market_code) 

timezone= calendar_kor.tz.zone
df_stock_calendar_kor = calendar_kor.schedule(start_date=start_date, end_date=end_date,tz=timezone)
list_stock_calendar_kor = df_stock_calendar_kor.index.date.tolist()

print('########################## 한국 증시 캘린더 ##########################')
print(df_stock_calendar_kor)
print('########################################################################\n\n\n')


# 미국 증시 캘린더
market_code= str('NYSE')
calendar_nyse = mcal.get_calendar('NYSE')
timezone= calendar_nyse.tz.zone
df_stock_calendar_nyse = calendar_nyse.schedule(start_date=start_date, end_date=end_date,tz=timezone)
list_stock_calendar_nyse = df_stock_calendar_nyse.index.date.tolist()

print('########################## 미국 증시 캘린더 ##########################')
print(df_stock_calendar_nyse)
print('########################################################################\n\n\n')


# db insert 시 dbms의 설정된 timezone으로 강제 변환될 수 있기 때문에
# date,time으로 나누어 insert 하면 안전
def get_df_market_open_time(market:str):
    calendar = mcal.get_calendar(market)
    tz= calendar.tz.zone   

    
    df = calendar.schedule(start_date=start_date, end_date=end_date,tz=tz)
    
    # 'end_date' 컬럼을 timestamp 타입으로 변환
    df['market_open'] = pd.to_datetime(df['market_open'])
    # 'market_open_date' 컬럼에는 날짜 정보만 저장 ('YYYY-MM-DD' 형식)
    df['market_open_date'] = df['market_open'].dt.strftime('%Y-%m-%d')
    # 'market_open_time' 컬럼에는 시간 정보만 저장 ('HH:mm' 형식)
    df['market_open_time'] = df['market_open'].dt.strftime('%H:%M')

    df['market_close'] = pd.to_datetime(df['market_close'])
    # 'market_open_date' 컬럼에는 날짜 정보만 저장 ('YYYY-MM-DD' 형식)
    df['market_close_date'] = df['market_close'].dt.strftime('%Y-%m-%d')
    # 'market_open_time' 컬럼에는 시간 정보만 저장 ('HH:mm' 형식)
    df['market_close_time'] = df['market_close'].dt.strftime('%H:%M')

    # 'end_date' 컬럼에서 날짜 부분만 추출하여 'date' 컬럼 추가
    df['datadate'] = df['market_open'].dt.date
    df['market_cd']=market
    df['timezone']=tz
    
    df= df.reset_index()
    
    df= df[['market_cd','datadate','timezone','market_open_date','market_open_time','market_close_date','market_close_time']]
    
    return df

df_stock_calendar_jpx = get_df_market_open_time('JPX')

print('##########################  일본 증시 캘린더 (date/time 분리) ##########################')
print(df_stock_calendar_jpx)
print('########################################################################\n\n\n')










warnings.filterwarnings('default')