def is_palindrome(word):
    length = len(word)
    for i in range(length // 2):
        if word[i] != word[length - i - 1]:
            print(f"The word {word} is not a palindrome")
            print(f"because {word[::-1]} is not equal to {word}")
            return
    
    print(f"The word {word} is a palindrome")

word = input("Please enter the word to check: ")
is_palindrome(word)

