rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']

print(rainbow)
print(f"2: {rainbow[2-1]}")

sorted_rainbow = rainbow.copy()
sorted_rainbow.sort()
print(sorted_rainbow)

another_sorted_rainboe = sorted(rainbow)
print(another_sorted_rainboe)

append_rainbow = rainbow.copy()
append_rainbow.append('crimson')
print(append_rainbow)

# 이건 코드가 복잡하다
pop_rainbow = rainbow.copy()
pop_rainbow.pop(2)
pop_rainbow.pop(2)
pop_rainbow.pop(2)
pop_rainbow.pop(2)
print(pop_rainbow)

# 제거할게 연속적인걸 활용하는 방법
del_rainbow = rainbow.copy()
del del_rainbow[2:6]
print(del_rainbow)

# 지우는걸 반대로 생각해서 남은걸 넣는 다는 걸로 해결
deleted_rainbow = [rainbow[0], rainbow[1], rainbow[6]]
print(deleted_rainbow)
