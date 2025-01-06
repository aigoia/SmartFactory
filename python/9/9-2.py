def add_fee(fee):
    return fee + 2500 if fee < 20000 else fee

print(add_fee(15000)) 