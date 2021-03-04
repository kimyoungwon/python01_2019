def funky_sum(a, b, mix):
    """
    Returns a mixture between a and b.

    If mix is 0, returns a. If mix is 1, returns b. Otherwise returns a linear
    interpolation between them. If mix is outside the range of 0 and 1, it is
    capped at those numbers.
    """
    if mix < 0:
        return a
    elif mix > 1:
        return b
    else:
        return (1 - mix) * a + mix * b


def count_divisible_digits(n, m):
    """
    Returns the number of digits in n that are divisible by m.
    If m is 0, then count_divisible_digits should return 0.

    Takes two integer numbers n and m as an arguments.
    """
    total = 0
    n = abs(n)
    if m == 0:
        return 0
    else:
        while n > 0:
            digit = n % 10
            if digit % m == 0:
                total += 1
                n = n // 10
            else:
                total += 0
                n = n // 10
        return total


def is_relatively_prime(n, m):
    """
    Returns True if n and m are relatively prime to each other,
    returning False otherwise.

    Takes two integer numbers n and m as an arguments.
    """
    prime_list1 = []
    prime_list2 = []
    for i in range(1, n+1):
        if n % i == 0:
            prime_list1.append(i)
    for j in range(1, m+1):
        if m % j == 0:
            prime_list2.append(j)
    prime_list3 = list(set(prime_list1).intersection(prime_list2))
    return prime_list3 == [1]


def travel(direction, x, y):
    """
    Returns a string that indicates the new position
    after following the directions starting from the given x, y in the format '(x_new, y_new)'.

    Takes a string of North (N), East (E), South (S), West (W) directions,
    a starting location on a grid x, and a starting location on a grid y.
    The directions string will use 'N' to indicate increasing the y-coordinate,
    'E' to indicate increasing the x-coordinate, 'S' to indicate decreasing the y-coordinate,
    and 'W' to indicate decrease the x-coordinate.
    The case of the characters should be ignored.
    Any characters that are not 'N', 'E', 'W', or 'S' (ignoring letter-casing) should be ignored.
    """
    direction = direction.lower()
    for i in str(direction):
        if i == 'e':
            x = x + 1
        elif i == 'n':
            y = y + 1
        elif i == 'w':
            x = x - 1
        elif i == 's':
            y = y - 1
        else:
            None
    return str((x, y))


def swip_swap(source, c1, c2):
    """
    Returns the string source with all occurrences of c1 and c2 swapped.

    Takes a string source and characters c1 and c2.
    """
    result = ""
    for i in range(len(source)):
        if source[i] == c1:
            result += c2
        elif source[i] == c2:
            result += c1
        else:
            result += source[i]
    return result


def compress(string):
    """
    Returns a new string such that each character is followed by its count,
    and any adjacent duplicate characters are removed (replaced by the single character).
    Takes a string as an argument.
    """
    if len(string) == 0:
        return string

    string = list(string)
    ls = []
    before = string[0]
    count = 1

    for i in range(1, len(string)):
        if string[i] == before:
            count += 1
        else:
            ls.append(before)
            ls.append(str(count))
            before = string[i]
            count = 1
    ls.append(before)
    ls.append(str(count))
    return ''.join(ls)


def longest_line_length(file_name):
    """
    Returns the length of the longest line in the file.

    Takes a string file_name.
    """
    with open(file_name) as f:
        ls = []
        result = None
        for line in f.readlines():
            ls.append(len(line))
            result = max(ls)
        return result


def longest_word(file_name):
    """
    Returns the longest word in the file with which line it appears on.

    Takes a string file_name.
    """
    with open(file_name) as f:
        lines = f.readlines()
        if len(lines) > 0:
            line_number = 0
            word_number = 0
            for line in lines:
                words = line.split()
                line_number += 1
                for word in words:
                    if len(word) > word_number:
                        word_number = len(word)
                        longest_word = word
                        line_with_the_word = line_number
            return (str(line_with_the_word) + ': ' + longest_word)
        else:
            return None


def mode_digit(digits):
    """
    Returns the digit that appears most frequently in that number.
    The given number may be positive or negative,
    but the most frequent digit returned should always be non-negative.
    If there is a tie for the most frequent digit,
    the digit with the greatest value should be returned.

    Takes an integer number n.
    """
    counts = [0] * 10
    if digits == 0:
        counts[0] += 1
    else:
        digits = abs(digits)
        while digits > 0:
            digit = digits % 10
            counts[digit] += 1
            digits //= 10
    max_count = 1
    result = 0
    for i in range(len(counts)):
        count = counts[i]
        if (count >= max_count):
            max_count = count
            result = i
    return result
