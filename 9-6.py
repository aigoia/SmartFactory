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

city_input = input("도시의 이름을 입력하세요: ")

city_data = [heat for _, city, heat, _ in weather_data if city == city_input]
mean_heat = lambda data: sum(data) / len(data)
result = mean_heat(city_data)

if result != None:
    print(f"{city_input}의 평균 기온: {round(result, 2)}°C")
