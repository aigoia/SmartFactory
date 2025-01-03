import sys

times_input = input("몇단을 출력할까여: ")

if_input = float(times_input)

if if_input.is_integer() == False:
    sys.exit()

if_input = int(if_input)

for i in range(1, 10):
    print(f"{times_input} x {i} = {times_input * i}")