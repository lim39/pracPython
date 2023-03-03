import pandas as pd

def df_ck(df: pd.DataFrame()= None):
    if not df.empty:
        print('exists')
    else:
        print('None')
def str_ck(objName: str= None):
    if not objName==None:
        print('exists')
    else:
        print('None')

df = pd.DataFrame({'month': [1, 4, 7, 10],
                   'year': [2012, 2014, 2013, 2014],
                   'sale': [55, 40, 84, 31]})

#df = pd.DataFrame()

str_ck()
# if not df.empty:
#     print (df.head())