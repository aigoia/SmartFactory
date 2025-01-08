def six():
    return 6 

def two():
    return 2

def plus(a, b):
    return a + b

def void():
    pass

print(void())

int_six = 6
def_six = six()

print(int_six)
print(def_six)

test_plus = plus(2, six())
print(test_plus)

test_minus = six() - two()
def_plus = plus(six(), two())

print(test_minus)
print(def_plus)
