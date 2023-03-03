import pandas as pd
import sys
# snowflake 커넥션
sys.path.append("C:\\Users\\USER\\Documents\\config\\")
import connSnowflake as sfcon

sf= sfcon.sf()


score = pd.DataFrame({

        'date': ['2019-07-28']*4, 

        'name': ['kim', 'lee', 'choi', 'park'], 

        'age': [19, 20, 19, 20], 

        'math_score': [91, 95, 92, 70], 

        'pass_yn': [True, True, True, False]}, 

         columns=['date', 'name', 'age', 'math_score', 'pass_yn'])

print(score)

with sf.connect() as conn:
    score.to_sql(name='')