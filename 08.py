print("1.")
passward_input = input("비밀번호를 입력하세여: ")

if passward_input == "abc123":
    print("비밀번호가 맞습니다")

if_input = input("숫자를 입력하세여: ")

# 숫자를 입력했는지 문자를 입력했는지 확인이 필요하다
# 예를들어 6이 아닌 Six를 입력할 가능성이 충분히 있다
if_input = float(if_input)

# 숫자 중에서 정수를 입력했는지도 확인이 필요하다
if if_input.is_integer():
    if_input = int(if_input)
    if if_input % 2 == 0:
        print("짝수 입니다")


else_input = input("숫자를 입력하세여: ")

else_input = float(else_input)

if else_input.is_integer():
    else_input = int(else_input)
    if else_input % 2 == 0:
        print("짝수입니다")
    else:
        print("홀수입니다")
else:
    print("정수가 아닙니다")
    

elif_input = input("점수를 입력하세여: ")

elif_input = float(elif_input)

# 음수 입력이 가능한 버전
if 60 > elif_input:
    print("학점: F")
elif 70 > elif_input:
    print("학점: D")
elif 80 > elif_input:
    print("학점: C")
elif 90 > elif_input:
    print("학점: B")
else:
    print("학점: A")

