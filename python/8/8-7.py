while True:
    positive_input = input("양수를 입력하세여 ('종료' 입력시 프로그램 종료): ")
    
    if positive_input == "종료":
        print("프로그램을 종료 합니다")
        break

    try:
        positive_input = int(positive_input)
        
        if positive_input < 0:
            print("양수만 입력하세여")
            continue
        elif positive_input == 0:
            continue
        else:
            result = 0
            i = 1

            while i <= positive_input:
                result = result + i
                i = i + 1
            
            print(f"1부터 {positive_input}의 합은 {result}입니다")
        
    except:
        print("양수만 입력하세여")
        continue
