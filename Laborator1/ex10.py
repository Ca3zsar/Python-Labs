#Ex10

def count_words(text):
    return len(text.split())

text = input("Enter a text : ")
print(count_words(text))