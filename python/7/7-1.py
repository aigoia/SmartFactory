rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']

print(rainbow)
print(f"2: {rainbow[2-1]}")

sorted_rainbow = rainbow.copy()
sorted_rainbow.sort()
print(sorted_rainbow)

another_sorted_rainbow = sorted(rainbow)
print(another_sorted_rainbow)

appended_rainbow = rainbow.copy()
appended_rainbow.append('crimson')
print(appended_rainbow)

# 라인이 당겨질때마다 뽑아내는 방법 
pop_rainbow = rainbow.copy()
for i in range(4):
    pop_rainbow.pop(2)
print(pop_rainbow)

# 제거할게 연속적인걸 활용하는 방법
del_rainbow = rainbow.copy()
del del_rainbow[2:6]
print(del_rainbow)

# 지우는걸 반대로 생각해서 남은걸 넣는 다는 걸로 해결
deleted_rainbow = [rainbow[0], rainbow[1], rainbow[6]]
print(deleted_rainbow)
