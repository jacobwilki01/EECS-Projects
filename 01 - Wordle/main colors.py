import random
from termcolor import *

def guess(word, guess):
    guessed = []
    count = 0
    for char in guess:
        temp = True
        if char == word[count] and temp:
            guessed.append(colored(char.upper(),"green"))
            temp = False
        elif temp:
            guessed.append(char.upper())
            temp = False
        count += 1
    
    for char in guessed:
        print(char,end="")

    return False
    
def valid(word, words, valid):
    if len(word) != 5:
        print("Invalid length!")
        return False

    check = False
    for option in words:
        if option == word:
            check = True
    for option in valid:
        if option == word:
            check = True

    if not check:
        print("Invalid word.")
    return check

def game(words,allowed):
    word = random.choice(words)
    print(word)
    count = 0
    while True:
        choice = input("\nGuess: ")
        if valid(choice, words, allowed):
            if count < 5:
                count += 1
                if guess(word.lower(), choice.lower()):
                    print(f"\n{word} is correct! It took you {count} guesses!")
                    break
            else:
                if guess(word.lower(), choice.lower()):
                    print(f"\n{word} is correct! It took you 6 guesses!")
                else:
                    print(f"\nYou just missed it. The word was: {word}.")
                break
    if input("Play again? [y/n]: ").lower() == "y":
        return True
    else:
        return False

def main():
    word_file = open("words.txt","r")
    valid_file = open("valid.txt","r")
    words = []
    valid = []
    for line in word_file:
        words.append(line.strip())
    for line in valid_file:
        valid.append(line.strip())

    while True:
        if not game(words,valid):
            break

if __name__ == "__main__":
    main()