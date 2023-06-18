# Hangman mini project

# Problem break-up
# 1: Generate random word
# 2: Generate the spaces as per the word
# 3: Ask user to guess the letter
# 4: Guessed letter right or wrong
# 5: response for correct guess
# 6: response for wrong guess
# 7: number of lifes(wrong guesses) and its response
# 8: win/loss response


# 1: Generate or pick randon word.

import random

words = ["pleasant", "shark", "tolerate", "husband", "effort","spare","skeleton","top","humanity","ideal"]
usedWords = []

def getWord(words, usedWords):
    word = random.choice(words)
    usedWords.append(word)    
    if word not in usedWords:
        return word
    else:
        getWord(words,usedWords)        

life = 3
remLetters = 0

word = getWord(words, usedWords)
spaces = ""
for i in word:
    spaces += '_'


guess = input("Guess the letter: ")
if guess in word:
    print("Correct")
else:
    print("Wrong")
    life -= 1
    
print(f"Word={word}")
print(f"Spaces={spaces}")