# 학생 딕셔너리
student_list = {}

# 각 데이터를 추가한다
student_list.update({"Alice": 85, "Bob": 90, "Charlie": 95})
print(student_list)

# David 학생에 점수로 80을 추가한다
student_list.update({"David": 80})
print(student_list)

# Alice 학생에 점수를 88로 수정한다
student_list["Alice"] = 88
print(student_list)

# Bob 학생을 딕셔너리에서 삭제한다
student_list.pop("Bob")
print(student_list)
