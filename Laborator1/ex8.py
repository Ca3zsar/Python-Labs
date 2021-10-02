#Ex8

def count_bits(number):
    count = 0
    while number:
        count += 1
        number &= (number-1)

    return count

number = int(input("Enter a number : "))
print(count_bits(number))