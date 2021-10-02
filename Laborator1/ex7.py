#Ex7

def find_number(text):
    number = ''
    for symbol in text:
        if symbol.isnumeric():
            number += symbol
        elif number:
            return number
    return "No number found"

text = input("Input text : ")
print(find_number(text))