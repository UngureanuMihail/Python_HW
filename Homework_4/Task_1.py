# Set the natural number N.
# Write a program that will make a list of prime factors of the number N.

def try_to_int(value):
    try:
        return int(value)
    except ValueError:
        return None


def prime_factors(value):
    value = try_to_int(value)
    if type(value) == None or value <= 0:
        return None
    if value in range(1, 4):
        return [1, value]
    result = []
    d = 2
    while d * d <= value:
        if value % d == 0:
            result.append(d)
            value //= d
        else:
            d += 1
    if value > 1:
        result.append(value)
    if (len(result) == 1):
        result.insert(0, 1)
    return result


print('To exit press Enter')

while True:
    s = input('Introduce your number: ')
    if s == '':
        exit()
    prime_factors = prime_factors(s)
    print(
        f"{' * '.join(map(str, prime_factors))} = {s}" if prime_factors != None else 'Eror. Please try again.')
