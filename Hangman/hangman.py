import random


class Hangman():
    """
    hangman
    """

    def __init__(self):
        self.wlist = []
        self.make_list()
        self.word = []
        self.get_word()
        self.attempts = 6
        self.used_letters = []
        self.wrong = ""
        self.spaces = len(self.word)

    def make_list(self):
        """
        Pretty inefficient way to get the word list in
        """
        wordlist = open('words.txt', 'r')
        self.wlist = wordlist.readlines()

    def get_word(self):
        """
        Generate random index and get the word at that index in lower case
        Currently no of words in list is hardcoded in(854)
        """
        index = random.randint(0, 855)
        self.word = list(self.wlist[index].lower())
        self.word = self.word[:-1]
        # really should be using this to find upper limit for randint
        # def file_len(fname):
        #     with open(fname) as f:
        #         for i, l in enumerate(f):
        #             pass
        #     return i + 1
        # finds no of lines in file

    def print_word(self):
        """
        print 
        """
        spaces = self.spaces
        print("Attemps remaining:", self.attempts)
        print(self.wrong)
        for i in self.word:
            if i in self.used_letters:
                print(i, " ", end='')
                spaces -= 1
            else:
                print("_ ", end='')
        if spaces == 0:
            self.spaces = 0
        print()

    def check(self, letter):
        """
        Checks if the letter is part of the word and/or has been used previously

        Arguments:
            letter {char} -- [single letter]
        """
        if letter in self.word and not letter in self.used_letters:
            self.used_letters.append(letter)
        elif letter in self.used_letters:
            print("Letter already used\n")
        else:
            self.attempts -= 1
            self.used_letters.append(letter)
            self.wrong += letter
            print("Letter not present\n")

    def get_input(self):
        """
        Take input
        check lengh of input
        if right length call check
        """
        self.print_word()
        while self.attempts != 0 and self.spaces != 0:
            letter = input("Enter a letter:")
            if len(letter) != 1:
                print("Input single letter\n")
            else:
                try:
                    self.check(letter.lower())
                except AttributeError:
                    print("Enter an alphabet")
            self.print_word()
        if self.spaces == 0:
            print("You win\n")
        else:
            print("You lose\n")


if __name__ == "__main__":
    hangman = Hangman()
    hangman.get_input()
