import pandas as pd


df = pd.DataFrame({'month': [1, 4, 7, 10],
                   'year': [2012, 2014, 2013, 2014],
                   'sale': [55, 40, 84, 31]})

print(df)

# print(df.set_index('month'))
"""
       year  sale
month
1      2012    55
4      2014    40
7      2013    84
10     2014    31
"""
# print(df.set_index('month')['sale'])
"""
month
1     55
4     40
7     84
10    31
Name: sale, dtype: int64
"""
# print(df.set_index(['year', 'month']))
"""
            sale
year month
2012 1        55
2014 4        40
2013 7        84
2014 10       31
"""
mylist=[]
for idx,row in df.iterrows():
    #print(idx)
    #print(row.to_list())
    mylist.append(row.to_list())
print(mylist)
# dataFrame에 행 추가
# List to append
#list = ['2015', 6, 60]

# 3가지 방법
# df.loc[len(df)] = list

# df = df.append(pd.DataFrame([list], columns=df.columns), ignore_index=True)

# df = df.append(pd.Series(list, index = df.columns), ignore_index=True)