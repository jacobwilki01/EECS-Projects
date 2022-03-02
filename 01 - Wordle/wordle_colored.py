import random
from termcolor import *

def letter_count(word):
    count = {}
    for letter in set(word):
        count[letter] = 0
    for letter in word:
        count[letter] += 1
    
    return count

def guess(word, guess):
    guessed, final = [], []
    count, correct = 0, 0
    delimiter = ""
    counted = letter_count(word)
    for char in guess:
        temp = True
        if char == word[count]:
            guessed.append(colored(char.upper(),"green"))
            temp = False
            correct += 1
            counted[char] -= 1
        else:
            for item in word:
                if item == char and counted[char] > 0:
                    guessed.append(colored(item.upper(),"yellow"))
                    temp = False
                    counted[char] -= 1
            if temp:
                guessed.append(char.upper())
        count += 1

    final.append(delimiter.join(guessed))
    final.append(correct)
    return final
    
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
    count = 0
    guesses = []
    while True:
        choice = input("Guess: ")
        if valid(choice, words, allowed):
            if count < 5:
                guesses.append(guess(word.lower(), choice.lower()))
                for item in guesses:
                    print(item[0])
                if guesses[count][1] == 5:
                    break
                count += 1
            else:
                guesses.append(guess(word.lower(), choice.lower()))
                for item in guesses:
                    print(item[0])
                if guesses[count][1] == 5:
                    break
                else:
                    print(f"The word was: {word.upper()}.")
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