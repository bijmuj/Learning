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
        self.spaces = len(self.word)

    def make_list(self):
        """
        Pretty inefficient way to get the word list in
        """
        wordlist = open("words.txt", 'r')
        self.wlist = wordlist.readlines()
        wordlist.close()

    def get_word(self):
        """
        Generate random index and get the word at that index in lower case
        Currently no of words in list is hardcoded in(854)
        """
        index = random.randint(0, 855)
        self.word = list(self.wlist[index].lower())
        self.word = self.word[:-1]

    def check(self, letter):
        """
        Checks if the letter is part of the word and/or has been used previously

        Arguments:
            letter {char} -- [single letter]
        """
        if letter in self.word and not letter in self.used_letters:
            self.used_letters.append(letter)
            # return 1
        elif letter in self.used_letters:
            pass
            # return 2
        else:
            self.attempts -= 1
            self.used_letters.append(letter)
            # return 0

    def update(self):
        """
        edited ver of print_word to use woth pygame
        """
        spaces = self.spaces
        # print("Attemps remaining:", self.attempts)
        # print(self.wrong)
        for i in self.word:
            if i in self.used_letters:
                # print(i, " ", end='')
                spaces -= 1
            else:
                print("_ ", end='')
        if spaces == 0:
            self.spaces = 0
        print()
