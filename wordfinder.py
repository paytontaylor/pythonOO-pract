"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    ...
    def __init__(self, path):

        file = open(path)
        self.words = self.parse(file)

        print(f"{len(self.words)} words read")

    def parse(self, file):
        """ Produces a list of words from the dict_file """

        return [w.strip() for w in file]

    def random(self):
        """ Chooses a random word from file """

        random = random.choice(self.words)    

    def parse(self, file):
        """Parse dict_file -> list of words, skipping blanks/comments."""

        return [w.strip() for w in file if w.strip() and not w.startswith("#")]