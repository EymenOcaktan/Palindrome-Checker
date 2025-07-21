# Palindrome-Checker
This project includes two versions of a **Palindrome Checker** built in Python. A palindrome is a word or phrase that reads the same forwards and backwards. The project shows how the same task can be approached differently as programming knowledge improves.

---

## 📌 Features: Beginner Version of Palindrome Checker

- Uses basic `while` loop and index tracking
- Compares characters from the beginning and end manually
- Uses a boolean flag (`is_palindrome`) to determine result
- Checks only for character equality (no cleaning of input)
- No use of functions — procedural style
- Ideal for practicing:
  - Looping
  - Index manipulation
  - Basic conditional logic

---

## 📌 Features: The Function Version of Palindrome Checker

- Uses a reusable function: `is_palindrome(string)`
- Cleans input using `.isalnum()` to remove punctuation
- Makes the comparison **case-insensitive**
- Uses string slicing (`[::-1]`) to check reverse
- More modular, readable, and maintainable
- Ideal for practicing:
  - Function creation
  - String processing
  - Clean code design

---

## ▶️ How to Use

1. Clone the repository or download the `.py` files.
2. Run either `beginner_version.py` or `function_version.py` in a Python environment.
3. Enter a word or sentence when prompted.
4. The program will tell you whether your input is a palindrome.

## 🧪 Example Output

### 🟡 Beginner Version Output

```text
Enter a word to see if it is a palindrome or not: radar
radar is a palindrome
Enter a word to see if it is a palindrome or not: Hello
Hello is not a palindrome
```

---

### 🟢 Function Version Output

```text
Please write a word to know whether it is a palindrome or not: A man, a plan, a canal, Panama
It is a palindrome
