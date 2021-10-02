#Ex 4

string = input("Enter a string in camelcase : ")
result = ''
for letter in string:
    if letter.isupper() :
        result += '_'
    result += letter.lower()
result = result[1:]
print(result)