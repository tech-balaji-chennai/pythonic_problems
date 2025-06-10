#Reverse Individual Words - 05 - Solution Code - Python

def find_length(str):
    count = 0

    for c in str:
        count += 1

    return count


def reverse(str, start, end):
    word = ""

    for i in range(end, start - 1, -1):  # reversed(range(start, end+1, 1))):
        word += str[i]

    return word


def reverse_words(str):
    wstart = 0
    len = find_length(str)  # len(str)
    rev_ind_words = ""

    for i in range(len):
        if str[i] == ' ':
            rev_ind_words += reverse(str, wstart, i - 1)
            rev_ind_words += ' '
            wstart = i + 1

    rev_ind_words += reverse(str, wstart, len - 1)
    return rev_ind_words


if __name__ == '__main__':
    str = input()

    result = reverse_words(str)
    print(result)
