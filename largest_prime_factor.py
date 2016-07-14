value = 600851475143
largest_prime = 0

def check_prime(value):
    if (value%2 == 0) or (value%3 ==0) or (value%5 == 0):
        return False
    for i in range(value/5):
        if value%i == 0:
            return False
    return True

i = 2
while True:
    if value%i == 0:
        if check_prime(value/i):
            largest_prime = value/i
            break
    i += 1

print largest_prime