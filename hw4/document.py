# uwnetid: 1724787
import re


class Document:
    '''
    The Document class represents a document and stores term frequency
    in the document as well as a list of words in it. Words and ignores
    punctuation, the case of the words, and non-alphabetic characters.
    '''
    def __init__(self, filename):
        '''
        Initialize a new Document object and include functions to compute
        the term frequency of a single document to get a list of words
        in the document.

        Take a filename as an argument.
        '''

        self._filename = filename
        self._term_list = self._create_term_list(filename)
        self._total_n_words = sum(self._term_list.values())

    def _create_term_list(self, filename):
        '''
        Create a list of term in the document. Duplicated words are allowed,
        but case, punctuation, non-alphabetic character are ignored.

        Take a filename as an argument.
        '''
        terms = []
        with open(filename, encoding='utf-8') as f:
            tokens = f.read().split()
            for token in tokens:
                token = token.lower()
                token = re.sub(r'\W+', '', token)
                terms.append(token)
            term_dict = {x: terms.count(x) for x in terms}
            return term_dict

    def term_frequency(self, term):
        '''
        Returns the frequency of the term in the document.
        If there is no term in the document, the frequency will be 0.

        Takes a term as a argument.
        '''
        term = term.lower()
        if term not in self._term_list.keys():
            return 0
        else:
            self._tf = self._term_list[term]/self._total_n_words
            return self._tf

    def get_words(self):
        """
        Return document's text into a list of individual words.
        The list should include only one word.

        Take a filename.
        """
        keys_list = [k for k in self._term_list]
        return keys_list

    def get_fname(self):
        '''
        Returns the name of the document
        '''
        return self._filename
