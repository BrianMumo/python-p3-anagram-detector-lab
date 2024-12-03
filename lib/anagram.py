# your code goes here!
class Anagram:
    def __init__(self, word):
        # Store the word in lowercase for case-insensitive matching
        self.word = word.lower()

    def match(self, words):
        # Sort the letters of the original word for comparison
        sorted_word = sorted(self.word)

        # Filter the list of words for anagrams
        return [w for w in words if sorted(w.lower()) == sorted_word]
