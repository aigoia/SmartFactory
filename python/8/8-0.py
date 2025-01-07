a, b = 5, 8
max_value = a if a > b else b
print(max_value)

score = 91 
grade = "A" if score >= 90 else ("B" if score >= 60 else "c")

new_grade = "A" if score >= 90 else "B" \
                if score >= 60 else "c" 
            
print(grade)
print(new_grade)