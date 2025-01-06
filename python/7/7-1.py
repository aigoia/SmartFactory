rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']

print(rainbow[2-1])
print(len(rainbow))

sorted_rainbow = rainbow.copy()
sorted_rainbow.sort()
print(sorted_rainbow)

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

# 때문에 지우는걸 반대로 생각해서 남은걸 넣는 다는 걸로 해결한다
deleted_rainbow = [rainbow[0], rainbow[1], rainbow[6]]
print(deleted_rainbow)

