import sys

#Ex 1
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


def multiple_gcd(numbers):
    if len(numbers) == 1:
        return numbers[0]

    result = numbers[0]
    for number in numbers[1:]:
        result = gcd(result , number)

    return result

print(multiple_gcd(list(map(int,sys.argv[1:]))))