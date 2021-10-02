#Ex6

def isPalindrome(number):
    string = str(number)
    to_substract = (len(string) % 2 + 1 ) %2

    first_half = len(string)//2
    second_half = len(string)//2-to_substract

    return string[:first_half] == string[len(string)-1:second_half:-1]

word = int(input("Write a number : "))  
print(isPalindrome(word))
    