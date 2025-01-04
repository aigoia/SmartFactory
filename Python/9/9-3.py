vending_machine = ['게토레이', '게토레이', '레쓰비', '레스비','생수', '생수', '생수', '이프로']

def check_machine(vending_machine):
    return vending_machine

def is_drink(vending_machine, drink):
    return drink in vending_machine

def add_drink(vending_machine, drink):
    vending_machine.append(drink)
    return vending_machine

def remove_drink(vending_machine, drink):
    if drink in vending_machine:
        vending_machine.remove(drink)
    return vending_machine

print(check_machine(vending_machine))
print(is_drink(vending_machine, '게토레이'))
print(add_drink(vending_machine, '이프로'))
print(remove_drink(vending_machine, '생수'))