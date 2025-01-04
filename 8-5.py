pay = [[0, 450, 720, 1200, 0], 
      [0, 450, 1000, 1300, 0]]

years = input("나이를 숫자로 입력해주세여: ")
years = int(years)

how = input("결제방법을 입력해주세여 (카드 또는 현금): ")

code = -1
result = 0

if how == "카드":
    code = 0
elif how == "현금":
    code = 1
else:
    how = input("결제방법을 다시 입력해주세여 (카드 또는 현금): ")
    if how == "카드":
        code = 0
    elif how == "현금":
        code = 1


if years < 8:
    result = pay[code][0]
elif years < 14:
    result = pay[code][1]
elif years < 20:
    result = pay[code][2]
elif years < 75:
    result = pay[code][3]
else:
    result = pay[code][4]

if code == 0 or code == 1:
    print(f"{years}세의 {how}요금은 {result}입니다")
else:
    print("결제방법을 잘못 입력하였습니다")