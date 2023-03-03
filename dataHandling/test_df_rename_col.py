import pandas as pd 


PATH = 'C:\\Users\\USER\\DownloadS\\'
FILE_NAME='Test_grid'
CSV_NAME= FILE_NAME+'.csv'
tbName= 'test_table'# 컬럼명 설정해서 불러오기

df = pd.read_csv(PATH+CSV_NAME
                        ,header=0                                                
                        , engine='python')
# 첫 번째 컬럼명 'date' 로 변환
df= df.rename(columns= {df.columns[0]:'date'})