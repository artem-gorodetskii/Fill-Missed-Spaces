from typing import Set, List, Tuple, Dict

from .tokenizer import Tokenizer


class SpacePredictor(object):
    r"""This class reconstructs a string with missed spaces. 
    """
    def __init__(self, vocabulary_path: str, punctuation: Set[str]):
        r"""
        Args:
            vocabulary_path: path to vocabulary.
            punctuation: set with punctuation marks.
        """
        super(SpacePredictor, self).__init__()

        self.vocabulary_path = vocabulary_path
        self.punctuation = punctuation

        # Initialize Tokenizer
        self.__tokenizer = Tokenizer(vocabulary_path)
        
    def __reconstruct(self, s: str, tokens: List[str]) -> Tuple:
        r"""Utility method. Reconstructs a string with missed spaces.
        Args:
            s: input string.
            tokens: list with string tokens.
        Returns:
            tuple (reconstructed string, list of missed spaces indices)
        """ 
        # missed spaces positions
        missed_spaces = []
        # reconstructed string characters
        characters = []

        # reconstruct the string using concatenated tokens
        concat_tokens = ' '.join(tokens)
        i, j = 0, 0
    
        while i < len(s) and j < len(concat_tokens):

            if s[i] != concat_tokens[j] and s[i] in self.punctuation:
                characters.append(s[i])
                i += 1

            elif s[i] != concat_tokens[j] and concat_tokens[j] == ' ':
                missed_spaces.append(len(characters))
                characters.append(concat_tokens[j])
                j += 1

            else:
                characters.append(s[i])
                i += 1
                j += 1

        # append remaining characters
        while i < len(s):
            characters.append(s[i])
            i += 1
        
        reconstructed_s = ''.join(characters)
    
        return reconstructed_s, missed_spaces
        
    def predict(self, s: str) -> Dict:
        r"""Reconstructs a string with missed spaces.
        Args:
            s: input string.
        Returns:
            dictionary ('text': reconstructed string, 
                        'missed_spaces': list of missed spaces indices)
        """
        # calculate tokens
        tokens = self.__tokenizer.tokenize(s)

        # reconstruct the string
        reconstructed_s, missed_spaces = self.__reconstruct(s, tokens)

        result = {'text': reconstructed_s,
                  'missed_spaces': missed_spaces}
        
        return result
    