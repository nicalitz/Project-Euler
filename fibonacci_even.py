value1 = 1
value2 = 2
sum = 2

while True:
    [value1, value2] = [value2, value1 + value2]
    if value2 > 4000000:
        break
    elif value2%2 == 0:
        sum += value2
print sum

