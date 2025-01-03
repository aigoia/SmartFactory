sum_input = input("어디까지 계산할까여: ")

sum_input = int(sum_input)

result = 0
for i in range(1, sum_input + 1):
    if i % 2 == 1:
        result = result + i
        
print(result)