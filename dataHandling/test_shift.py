import pandas as pd

idx = pd.date_range(start='2022-01-01',periods=5,freq='2D')
# 2일 간격으로 5행의 인덱스 생성
data={'col1':[10,20,30,40,50],'col2':[1,3,6,7,9],'col3':[43,13,82,47,31]}
df = pd.DataFrame(data=data, index=idx)
print(df)