import random

def guess(word, guess):
    count = 0
    green = []
    for letter in guess:
        if letter == word[count]:
            green.append(letter)
        else:
            green.append("_")
        count += 1
    
    yellow = []
    for x in set(guess):
        for y in set(word):
            if x == y:
                yellow.append(x)

    temp = []
    for letter in yellow:
        for right in green:
            if letter == right:
                temp.append(letter)
    for letter in set(temp):
        yellow.remove(letter)

    correct = 0
    for letter in green:
        print(letter,end="")
        if letter != "_":
            correct += 1
    if len(yellow) > 0:
        print("\nLetters in the incorrect slot: ",end="")
        for letter in yellow:
            print(letter,end=", ")
    elif correct != 5:
        print("\nLetters in the incorrect slot: None.",end="")

    if correct == 5:
        return True
    else:
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