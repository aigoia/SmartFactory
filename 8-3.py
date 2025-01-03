import sys

else_input = input("숫자를 입력하세여: ")

else_input = float(else_input)

if else_input.is_integer() == False:
    sys.exit()
else_input = int(else_input)    

if else_input % 2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")