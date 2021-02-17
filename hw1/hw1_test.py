import math

import hw1


def assert_equals(expected, received):
    """
    Checks received against expected, throws an AssertionError
    if they don't match. If expected or recieved are floats,
    will do an approximate check.
    """
    # You don't need to understand how this function works
    # just look at its documentation!
    if type(expected) == 'float' or type(received) == 'float':
        match = math.isclose(expected, received)
    else:
        match = expected == received

    assert match, f'Failed: Expected {expected}, but received {received}'


def test_funky_sum():
    """
    Tests the function funky_sum
    """
    print('Testing funky_sum')

    # Notice that we have to start the function calls with "hw1." since
    # they live in another file

    # Cases from the made up "spec" for this problem
    assert_equals(1, hw1.funky_sum(1, 2, 0))
    assert_equals(2, hw1.funky_sum(1, 2, 1))
    assert_equals(1.5, hw1.funky_sum(1, 2, 0.5))
    assert_equals(1.33, hw1.funky_sum(1, 2, 0.33))

    # edge cases to test the 0 check
    assert_equals(1, hw1.funky_sum(1, 2, -1))
    assert_equals(1, hw1.funky_sum(1, 2, -0.1))
    assert_equals(1.01, hw1.funky_sum(1, 2, 0.01))

    # edge cases to test the 1 check
    assert_equals(2, hw1.funky_sum(1, 2, 2))
    assert_equals(2, hw1.funky_sum(1, 2, 2.1))
    assert_equals(1.99, hw1.funky_sum(1, 2, 0.99))


def main():
    test_funky_sum()
    # Make sure you add the calls to all of your other functions here!


if __name__ == '__main__':
    main()
