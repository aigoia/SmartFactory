pay_list = [[0, 450, 720, 1200, 0], 
           [0, 450, 1000, 1300, 0]]

years = input("나이를 숫자로 입력해주세여: ")
years = int(years)
how = input("결제방법을 입력해주세여 (카드 또는 현금): ")

code = -1
result = 0

code = 0 if how == "카드" else 1\
         if how == "현금" else -1 

result = pay_list[code][0] if years < 8 else pay_list[code][1]\
                           if years < 14 else pay_list[code][2]\
                           if years < 20 else pay_list[code][3]\
                           if years < 75 else pay_list[code][4]

if code == 0:
    print(f"{years}세의 카드요금은 {result}입니다")
else:
    if code == 1:
        print(f"{years}세의 현금은 {result}입니다")
    else:
        print("결제방법을 잘못 입력하였습니다")
    