def find_N(string, text):
    found_occurrences = []
    word_length = len(string)
    for i in range(0, len(text)-word_length + 1):
        for j in range(0, word_length):
            if string[j] != text[i + j]:
                break
            if (j == word_length - 1):
                found_occurrences.append(i)
    return found_occurrences


def find_KMP(string, text):
    matching_table = []
    found_occurrences = []
    return found_occurrences


def find_KR(string, text):
    found_occurrences = []
    return found_occurrences
