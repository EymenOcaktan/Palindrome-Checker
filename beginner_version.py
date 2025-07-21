word = input("Enter a word to see if it is a palindrome or not: ")
n = 0
x = -1
is_palindrome = True
while n < len(word)//2:
    if word[n] != word[x]:
        is_palindrome = False
        break
    n += 1
    x -= 1
if is_palindrome:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")