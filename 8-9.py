times_input = input("몇단을 출력할까여: ")

times_input = int(times_input)

for i in range(1, 10):
    print(f"{times_input} x {i} = {times_input * i}")