def is_palindrome(string):
    word_check = ""
    for x in string:
        if x.isalnum():
            word_check += x.lower()
    return word_check == word_check[::-1]

word = input("Please write a word to know whether it is a palindrome or not: ")
if is_palindrome(word):
    print("It is a palindrome")
else:
    print("It isn't a palindrome")









