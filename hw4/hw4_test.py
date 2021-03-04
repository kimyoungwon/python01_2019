from cse163_utils import assert_equals
from document import Document
from search_engine import SearchEngine


# This file is left blank for you to fill in with your tests!

doc = Document('test_dir1/1.txt')
dic = SearchEngine('test_dir1')


def test_term_frequency():
    """
    Tests the function: term_frequency
    """
    print('Testing term_frequency')

    assert_equals(0.2, doc.term_frequency('cute'))
    assert_equals(0.2, doc.term_frequency('I'))


def test_get_words():
    """
    Tests the function: get_words
    """
    print('Testing get_words')

    assert_equals(['i', 'love', 'a', 'cute', 'cat'], doc.get_words())


def test_document():
    """
    Tests the class: document
    """
    print('Testing document')

    assert_equals('test_dir1/1.txt', Document('test_dir1/1.txt').get_fname())


def test_create_term_list():
    """
    Tests the function: _create_term_list
    """
    print('Testing _create_term_list')

    assert_equals(['i', 'love', 'a', 'cute', 'cat'],
                  doc._create_term_list('test_dir1/1.txt'))


def test_calculate_idf():
    """
    Tests the function: _calculate_idf
    """
    print('Testing _calculate_idf')

    assert_equals(0, dic._calculate_idf('i'))
    assert_equals(0.4054651081081644, dic._calculate_idf('cute'))


def test_search():
    """
    Tests the function: search
    """
    print('Testing search')

    assert_equals(['test_dir1/3.txt'], dic.search('ugly'))
    assert_equals(['test_dir1/2.txt', 'test_dir1/1.txt'], dic.search('cute'))
    assert_equals(['test_dir1/1.txt', 'test_dir1/2.txt', 'test_dir1/3.txt'],
                  dic.search('I love'))


def test_individual_words():
    """
    Tests the function: _individual_words
    """
    print('Testing _individual_words')

    assert_equals(['i', 'love', 'you'], dic._individual_words('I love you'))
    assert_equals(['i', 'like'], dic._individual_words('I like'))


def main():
    test_document()
    test_term_frequency()
    test_get_words()
    test_create_term_list()
    test_calculate_idf()
    test_individual_words()
    test_search()


if __name__ == '__main__':
    main()
