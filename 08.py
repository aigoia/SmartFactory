print("1.")
passward_input = input("비밀번호를 입력하세여: ")

if passward_input == "abc123":
    print("비밀번호가 맞습니다")

number_input = input("숫자를 입력하세여: ")

# 숫자를 입력했는지 문자를 입력했는지 확인이 필요하다
# 예를들어 6이 아닌 Six를 입력할 가능성이 충분히 있다
number_input = float(number_input)

# 숫자 중에서 정수를 입력했는지도 확인이 필요하다
if number_input.is_integer():
    number_input = int(number_input)
    if number_input % 2 == 0:
        print("짝수 입니다")
