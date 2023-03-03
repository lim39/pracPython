
# 리스트를 문자열로 변환
my_list = ['apple', 'banana', 'grape']
result = "(" + ','.join("'" + item + "'" for item in my_list) + ")"
print(result)