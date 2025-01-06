text = "Hello Python"

date = "20250106"
year = date[:4]
month = date[4:6]
day = date[6:]

# print(year)
# print(month)
# print(day)

# print(len(date))
# print(text.count("l"))

# print(text.count("p"))

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix.append([10, 11, 12])
print(matrix)

matrix[1].insert(1, -1)
print(matrix)

matrix.insert(2, ["a", "b", "c"])
print(matrix)

student_list = {}

words = [["아"], ["이"]]
new_word = words[0][0][0] + words[1][0][0]
print(new_word)