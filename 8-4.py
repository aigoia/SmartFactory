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