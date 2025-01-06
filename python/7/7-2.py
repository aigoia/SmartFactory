student_list = {}

student_list.update({"Alice": 85, "Bob": 90, "Charlie": 95})
print(student_list)
student_list.update({"David": 80})
print(student_list)
student_list["Alice"] = 88
print(student_list)
student_list.pop("Bob")
print(student_list)