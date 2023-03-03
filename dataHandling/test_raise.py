a = int(input("1~5 까지 숫자 입력 : "))
# 범위를 벗어나면 error 발생!
if a < 1 or a > 5:
    raise ValueError
    #print("범위 내 숫자가 아닙니다.")
# 범위 안에 있으면 정상 출력
print(f"입력한 a : {a} 입니다.")

