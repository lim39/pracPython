import pandas as pd
from sklearn import datasets

iris = datasets.load_iris()
df = pd.DataFrame(iris['data'], columns=iris['feature_names'])


# 딕셔너리로 변환하고 가져오기
df_dict = df.to_dict()
dic_val = df_dict['sepal length (cm)'].values()
dic_list = list(dic_val)


# 컬럼을 선택한 후에 리스트로 변환하기
df['sepal length (cm)'].to_list()
list(df['sepal length (cm)'])

# 행을 리스트로 추출하기
df.iloc[0].to_list()
list(df.iloc[0])