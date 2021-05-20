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


def get_prefix_suffix_table(word):
    word_length = len(word)
    ps_talbe = [0]*word_length
    i = 0
    for j in range(1, word_length):
        if word[i] == word[j]:
            ps_talbe[j] = i + 1
            i += 1
        else:
            i = ps_talbe[i-1]
            if word[j] == word[i]:
                ps_talbe[j] = i + 1
                i += 1
            else:
                ps_talbe[j] = 0
                i = 0
    return ps_talbe


def find_KMP(string, text):
    ps_table = get_prefix_suffix_table(string)
    found_occurrences = []
    word_length = len(string)
    i = 0
    j = 0
    while j != word_length and i < len(text):
        if text[i] == string[j]:
            i += 1
            j += 1
        elif j != 0:
            j = ps_table[j - 1]
        else:
            i += 1
        if j == word_length:
            found_occurrences.append(i - j)
            j = ps_table[j-1]
    return found_occurrences


def find_KR(string, text):
    found_occurrences = []
    return found_occurrences


a = get_prefix_suffix_table("AAAA")

b = get_prefix_suffix_table("ABCDE")

c = get_prefix_suffix_table("AABAACAABAA")

d = get_prefix_suffix_table("AAACAAAAAC")

e = get_prefix_suffix_table("AAABAAA")

print(a)
print(b)
print(c)
print(d)
print(e)
