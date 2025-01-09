
def max(list):
    result = 0
    for i in list:
        result = i if i > result else result
    return result

print(max([1, 4, 3]))