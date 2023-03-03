import pandas as pd


df= pd.DataFrame({'item':['아이폰','갤럭시노트20','안드로이드']
     ,'Price':[800000,1200000,500000]
     })

row_list= []
for idx,row in df.iterrows():
    row_list.append(row)



print(row_list)