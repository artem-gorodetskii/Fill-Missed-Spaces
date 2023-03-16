import gzip, re
from math import log

from typing import List, Tuple


class Tokenizer(object):
    r"""This class performs tokenization of an input string using 
        dynamic programming and unigram probabilistic model with 
        predefined vocabulary.
        Adapted from http://stackoverflow.com/a/11642687/2449774 and
        https://github.com/keredson/wordninja/blob/master/wordninja.py
        All rights reserved.
    """
    def __init__(self, vocabulary_path: str):
        r"""
        Args:
            vocabulary_path: path to vocabulary.
        """
        super(Tokenizer, self).__init__()

        # load vocabulary
        with gzip.open(vocabulary_path) as f:
            words = f.read().decode().split()
        
        self._wordcost = dict((k, log((i + 1) * log(len(words)))) for i, k in enumerate(words))
        self._maxword = max(len(x) for x in words)
        self._split_re = re.compile("[^a-zA-Z0-9']+")
   

    def tokenize(self, s: str) -> List[str]:
        r"""Applies dynamic programming to split a string into list of tokens.
        Args:
            s: input string.
        Returns:
            list of tokens.
        """
        l = [self.__tokenize(x) for x in self._split_re.split(s)]

        return [item for sublist in l for item in sublist]
    

    def __best_match(self, i: int, s: str, cost: List[float]) -> Tuple:
        r"""Utility method. Finds the best match for the i first characters, 
            assuming cost has been built for the i-1 first characters.
        Args:
            i: character index. 
            s: input string.
            cost: cost array.
        Returns:
            tuple (match_cost, match_length).
        """
        candidates = enumerate(reversed(cost[max(0, i - self._maxword) : i]))

        return min((c + self._wordcost.get(s[i - k - 1 : i].lower(), 9e999), k + 1) for k, c in candidates)


    def __tokenize(self, s: str) -> object:
        r"""Utility method. Applies dynamic programming 
            to recover the minimal-cost string.
        Args:
            s: input string.
        Returns:
            reversed iterator object with tokens.
        """
        # Initialize the cost array
        cost = [0]

        for i in range(1, len(s) + 1):
            c, k = self.__best_match(i, s, cost)
            cost.append(c)

        # Backtrack to recover the minimal-cost string
        out = []
        i = len(s)

        while i > 0:
            c, k = self.__best_match(i, s, cost)
            assert c == cost[i]

            # Apostrophe and digit handling
            newToken = True

            # ignore apostrophe
            if not s[i - k : i] == "'": 
                if len(out) > 0:
                    # re-attach split 's and split digits
                    if out[-1] == "'s" or (s[i - 1].isdigit() and out[-1][0].isdigit()):
                        # combine current token with previous token
                        out[-1] = s[i - k : i] + out[-1] 
                        newToken = False

            if newToken:
                out.append(s[i - k : i])

            i -= k
            
        return reversed(out)
    