class Game:
    def __init__(self,word):
        self.limit = 6
        self.misses = 0
        self.guesses = []
        self.board = [
        "  |---|    ",#0
        "  |        ",#1
        "  |        ",#2
        "  |        ",#3
        "  |        ",#4
        "",           #5
        "",           #6
        ""]           #7
        self.word = word.lower()
        for _ in range(0,len(self.word)):
            self.board[6] += "_ "
        self.board_print()
    def guess(self,guess):
        self.guesses.append(guess)
        located = []
        for x in range(0,len(self.word)):
            if self.word[x] == guess.lower():
                located.append(x)
        if len(located) == 0:
            self.misses += 1
            print("Letter is not in word!")
            if self.misses == 1:
                self.board[1] = "  |   o    "
            elif self.misses == 2:
                self.board[2] = "  |   |    "
            elif self.misses == 3:
                self.board[2] = "  |  /|    "
            elif self.misses == 4:
                self.board[2] = "  |  /|\   "
            elif self.misses == 5:
                self.board[3] = "  |  /     "
            elif self.misses == 6:
                self.board[3] = "  |  / \   "
        else:
            print("Letter is in word!")
            temp = self.board[6].split()
            temp_ = ""
            if len(located) == 1:
                pass
            else:
                pass
            for item in temp:
                temp_ += f"{item} "
            self.board[6] = temp_
        self.board_print()
    def board_print(self):
        for line in self.board:
            print(line)

game = Game("Hello")
while game.misses < 6:
    game.guess(input("Guess: "))