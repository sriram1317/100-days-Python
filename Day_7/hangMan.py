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
import os

words = ["pleasant", "shark", "tolerate", "husband", "effort","spare","skeleton","top","humanity","ideal"]
usedWords = []
endOfGame = False

def getWord(words, usedWords):
    word = random.choice(words)
    if word not in usedWords:
        usedWords.append(word)  
        return word
    else:
        getWord(words,usedWords)        

def replaceSpace(spaces,guess,word):
    for i in range(0,len(word)):
        if guess == word[i]:
            spaces[i] = guess
    return spaces


word = getWord(words, usedWords)
remLetters = len(word) 
life = 6

spaces = []
for i in word:
    spaces += '_'

print(f"Word={word}")


while endOfGame == False:   
    
    # print(f"Spaces={spaces}")
    guess = input("Guess the letter: ")
    os.system('cls')
    if guess in word:
        
        print(f"Correct!, letter {guess} is present")
        spaces = replaceSpace(spaces, guess, word)
        print(f"Spaces={spaces}")
        c = word.count(guess)
        remLetters -= c
    
    else:
        print("Wrong")
        print(spaces)

        life -= 1
    
    if remLetters == 0 or life == 0:
        endOfGame = True

    
    

if life > 0:
    print("!Yay! you won")
else:
    print("OHH NO, you lost")