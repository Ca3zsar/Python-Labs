#Ex2

vowels = 'aeiouAEIOU'

def count_vowels(word):
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1

    return count

word = input("Please enter a word : ")
print(count_vowels(word))