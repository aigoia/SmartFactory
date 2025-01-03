calorie = {"apple": 95, "banana": 105, "cherry": 50}

calorie_input = input("과일을 영문으로 입력하세여: ")

if calorie_input in calorie:
    print(f"{calorie_input}의 칼로리는 {calorie[calorie_input]}Kcal입니다")
else:
    print("존재하지 않는 과일입니다")