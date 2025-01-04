weather_data = [
    ["2024-11-20", "서울", 15.2, 0.0],
    ["2024-11-20", "부산", 18.4, 0.0],
    ["2024-11-21", "서울", 10.5, 2.3],
    ["2024-11-21", "부산", 14.6, 1.2],
    ["2024-11-22", "서울", 8.3, 0.0],
    ["2023-11-22", "부산", 12.0, 0.0],
]

print("[날씨 데이터 분석 프로그램] \n",
      "1. 평균 기온 계산 \n",
      "2. 최고/최저 기온 찾기 \n",
      "3. 강수량 분석 \n",
      "4. 날씨 데이터 추가 \n",
      "5. 전체 데이터 출력 \n",
      "6. 종료 ")

want = input("원하는 기능의 번호를 입력하세여: ")
want = int(want)

if want <= 0 or want >= 4:
    pass
else:
    city_input = input("도시의 이름을 입력하세요: ")

    heat_list = [heat for _, city, heat, _ in weather_data if city == city_input]
    water_list = [water for _, city, _, water in weather_data if city == city_input]
    water_day_list = [day for day in water_list if day != 0]

    mean_heat = lambda data: sum(data) / len(data)
    city_heat = mean_heat(heat_list)

    min_heat = min(heat_list)
    max_heat = max(heat_list)

    sum_water = sum(water_list)
    count_water = len(water_day_list)

def print_all():
    for date, city, heat, water in weather_data:
        print(f"날짜: {date}, 도시: {city}, 평균기온: {heat}c, 강수량: {water}mm")

if want == 5:
    print_all()
elif want == 1:
    print(f"{city_input}의 평균기온: {round(city_heat, 2)}c")
elif want == 2:
    print(f"{city_input}의 최고기온: {round(max_heat, 2)}c, 최저기온: {round(min_heat, 2)}c")
elif want == 3:
    print(f"{city_input}의 총 강수량: {round(sum_water, 2)}c")
    print(f"{city_input}의 강수량이 있던날: {count_water}일")

elif want == 4:
    day = input("날짜를 입력하세여: ") 
    city = input("도시를 입력하세여: ")
    heat = input("평균기온을 입력하세여: ")
    water = input("강수량을 입력하세여: ")
    
    weather_data.append([day, city, round(float(heat), 1), round(float(water), 1)])
    print("서울의 날씨 데이터가 추가되었습니다")
    print_all()
