score_input = input("점수를 입력하세여: ")

score_input = int(score_input)

score = "F"
if score_input < 60:
    score = "F"
elif score_input < 70:
    score = "D"
elif score_input < 80:
    score = "C"
elif score_input < 90:
    score = "B"
else:
    score = "A"

print(f"학점: {score}")
