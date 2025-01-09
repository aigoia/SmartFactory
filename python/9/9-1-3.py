vending_machine = ['게토레이', '게토레이', '레쓰비', '레스비','생수', '생수', '생수', '이프로']

def check_machine():
    print("남은 음료수: ", vending_machine)
    
def is_drink(drink):
    return drink in vending_machine

def add_drink(drink):
    if is_drink(drink):
        same_drink_list = filter(lambda i : i == drink, vending_machine)
        input_index = vending_machine.index(drink)
        input_index = input_index + len(list(same_drink_list))
        vending_machine.insert(input_index, drink)  
        print(f"이미 {drink} 있는거 뒤에 추가 완료")
    else:
        vending_machine.append(drink)
        print(f"{"그냥 맨뒤에 추가"}")
      
def remove_drink(drink):
    if is_drink(drink):
        vending_machine.remove(drink)
        print(f"{drink} 드릴게여")
    else:
        print("음료가 없습니다")

while True:
    user_type = input("사용자 유형을 선택하세여 \n"
                      "1. 소비자\n"
                      "2. 주인\n"
                      "0. 종료\n"
                      ": ")
    
    if user_type == "1": # 소비자 
        drink = input("마시고 싶은 음료? ")
        remove_drink(drink)
        check_machine()
        
    elif user_type == "2":
        action = input("할일을 선택하세여\n"
                       "1. 추가\n"
                       "2. 삭제\n"
                       ": ")

        if action == "1":
            drink = input("추가할 음료수? ")
            add_drink(drink)
            
        elif action == "2":
            drink = input("삭제할 음료수? ")
            vending_machine.remove(drink)
            print(f"{drink}을 삭제 완료")
        else:
            print("잘못된 값입니다")
        check_machine()
        
    elif user_type == "0":
        print("프로그램을 종료합니다")
        break
    else:
        print("다시 입력하세여")