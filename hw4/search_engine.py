# uwnetid: 1724787

import os
import re
import math
from document import Document


class SearchEngine:
    '''
    The SearchEngine class deal with a number of documents at the same time.
    '''
    def __init__(self, dir):
        '''
        Makes an inverse index representing all documents in the specific
        directory and computed the TF-IDF of a specific term for each document.

        Take a directory name as an argument.
        '''
        self._docs = set()
        for filename in os.listdir(dir):
            doc = Document(dir + '/' + filename)
            self._docs.add(doc)

        self._inverse_index = self._create_inverse_index()
        self._total_n_doc = len(self._docs)

    def _create_inverse_index(self):
        '''
        Create an inver index for all documents in a given directory.
        '''
        inv_index = {}
        for doc in self._docs:
            for term in doc.get_words():
                if term not in inv_index.keys():
                    values = set()
                    values.add(doc)
                    inv_index[term] = values
                else:
                    inv_index[term].add(doc)
        return inv_index

    def _calculate_idf(self, term):
        '''
        Return the IDF score for the given term over all documents.

        Take a term as an argument
        '''
        if term not in self._inverse_index.keys():
            return 0
        elif term in self._inverse_index.keys():
            return math.log(self._total_n_doc/len(self._inverse_index[term]))

    def _individual_words(self, string):
        '''
        Split a string up into a list of individual words.

        Take a string as an argument.
        '''
        return ([word for word in re.split(r'\W+', string.lower())
                if len(word) >= 1])

    def search(self, string):
        '''
        Return a list of document names ordered by TFIDF scores
        in a descending order.

        Take a string as an argument
        '''
        words = self._individual_words(string)
        doc_TFIDF = []
        for term in words:
            if term not in self._inverse_index.keys():
                return None
            elif term in self._inverse_index.keys():
                for doc_name in self._inverse_index[term]:
                    self._TF = Document(doc_name.get_fname()).\
                        term_frequency(term)
                    self._IDF = self._calculate_idf(term)
                    TFIDF = self._TF * self._IDF
                    doc_TFIDF.append((doc_name.get_fname(), TFIDF))
        TFIDF_dict = {}
        for t in doc_TFIDF:
            if t[0] in TFIDF_dict:
                TFIDF_dict[t[0]] = TFIDF_dict[t[0]]+t[1]
            else:
                TFIDF_dict[t[0]] = t[1]
        return sorted(TFIDF_dict, key=TFIDF_dict.get, reverse=True)
