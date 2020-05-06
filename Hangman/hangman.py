import random
import os


def clear():
    return os.system('cls')


def make_list():
    """
    Pretty inefficient way to get the word list in I think?
    """
    wordlist = open('words.txt', 'r')
    return wordlist.readlines()


class Hangman():
    """
    hangman
    """

    def __init__(self):
        self.word, self.spaces = self.get_word()
        self.attempts = 6
        self.used_letters = []
        self.wrong = ""

    def get_word(self):
        """
        Generate random index and get the word at that index in lower case
        Currently no of words in list is hardcoded in(854)
        """
        wlist = make_list()
        index = random.randint(0, 855)
        word = list(wlist[index].lower())[:-1]
        return word, len(word)

    def print_word(self):
        """
        Pretty self explanatory
        """
        print("Attemps remaining:", self.attempts)
        print(self.wrong)
        for letter in self.word:
            if letter in self.used_letters:
                print(letter, " ", end='')
            else:
                print("_ ", end='')
        print()

    def check(self, letter):
        """
        Checks if the letter is part of the word and/or has been used previously

        Arguments:
            letter {char} -- [single letter]
        """
        if letter in self.used_letters:
            print("Letter already used\n")
        else:
            self.used_letters.append(letter)
            if letter not in self.word:
                self.attempts -= 1
                self.wrong += letter
                print("Letter not present\n")
            else:
                self.spaces -= self.word.count(letter)

    def get_input(self):
        """
        Take input
        check lengh of input
        if right length call check
        """
        self.print_word()
        while self.attempts and self.spaces:
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
            # a bit janky but works
            print("Word is: {0}".format("".join(self.word)))
            print("You lose\n")


if __name__ == "__main__":
    hangman = Hangman()
    hangman.get_input()
