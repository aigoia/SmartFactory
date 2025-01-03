# 1
rainbow = ['red', 'oprange', 'yellow', 'green', 'blue', 'indigo', 'purple']
print("1.")

print(rainbow[2-1])

sorted_rainbow = rainbow
sorted_rainbow.sort()
print(sorted_rainbow)

append_rainbow = rainbow
append_rainbow.append('crimson')
print(append_rainbow)

deleted_rainbow = []
deleted_rainbow.append(rainbow[0])
deleted_rainbow.append(rainbow[1])
deleted_rainbow.append(rainbow[6])
print(deleted_rainbow)

#2
print("2.")
student_list = {}
student_list.update({"Alice": 85, "Bob": 90, "Charlie": 95})
print(student_list)
student_list.update({"David": 80})
print(student_list)
student_list["Alice"] = 88
print(student_list)
student_list.pop("Bob")
print(student_list)