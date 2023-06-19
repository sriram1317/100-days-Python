import random
import os

words = ["zorilla","plundering","apple","banana","helicopter","bottle","cup","top","phone"]
usedLetters = []
life = 6
endOfGame = False
spaces = []



def getWord():
    word = random.choice(words)
    words.remove(word)
    return word

def replaceSpaces(spaces, word, guess):
    for i in range(0,len(word)):
        if guess == word[i]:
            spaces[i] = guess
    return spaces


word = getWord()
remLetters = len(word)

for i in word:
    spaces += '_'

print(f"Word = {word}")

      
while (life > 0 or remLetters > 0) and endOfGame == False:
    print(f"remLetters = {remLetters}")
    print(f"Life = {life}")
    print(f"Spaces = {spaces}")
    guess = input("Guess a letter: ").lower()[0]

    if guess in word:
        print(f"Spaces = {spaces}")
        print(f"Correct! letter {guess} is present in the word!")
        
        spaces = replaceSpaces(spaces, word, guess)
        if guess in usedLetters:
            print(f"you have already guessed: {guess}, try again")
            continue
        num = word.count(guess)
        remLetters -= num

        usedLetters += guess
        

        
        print(f"remletters={remLetters}")
        
    else:
        print(f"Wrong guess, the letter {guess} is not present")
        print(f"Spaces = {spaces}")
        life -= 1

    if remLetters == 0 or life == 0:
        endOfGame = True

if life > 0:
    print("!Yay! you won")
else:
    os.system('cls')
    print(f"OHH NO, you lost, the word was '{word}'")
    