#Ex9

def most_frequent_letter(text : str):
    counter = {}
    for symbol in text:
        if symbol.isalpha():
            if counter.get(symbol.lower()):
                counter[symbol.lower()] += 1
            else:
                counter[symbol.lower()] = 1
    
    frequent = ''
    maximum = 0
    for key in counter:
        if counter[key] > maximum:
            maximum = counter[key]
            frequent = key
    
    return frequent

text = input("Enter a text : ")
print(most_frequent_letter(text))