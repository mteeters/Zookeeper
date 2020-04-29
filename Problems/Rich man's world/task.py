deposit = int(input())
protected_amount = 700000
i = 0
while deposit < protected_amount:
    deposit += deposit * 0.071
    i += 1
print(i)
