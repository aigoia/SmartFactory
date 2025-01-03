import sys

if_input = input("숫자를 입력하세여: ")

if_input = float(if_input)


if if_input.is_integer() == False:
    sys.exit()

if_input = int(if_input)

if if_input % 2 == 0:
    print("짝수 입니다")