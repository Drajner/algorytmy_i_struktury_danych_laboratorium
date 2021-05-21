polish_chars = {"Ą": 256, "Ć": 257, "Ę": 258, "Ł": 259,
                "Ń": 260, "Ó": 261, "Ś": 262, "Ź": 263,
                "Ż": 264, "ą": 265, "ć": 266, "ę": 267,
                "ł": 268, "ń": 269, "ó": 270, "ś": 271,
                "ź": 272, "ż": 273
                }
prime = 113
alphabet_size = 256 + 18


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


def char_value(char):
    if char in polish_chars:
        return polish_chars[char]
    return ord(char)


def hash_KR(p_value, weight, n_c, p_c=None):
    if p_c is None:
        n_value = (alphabet_size*(p_value)+char_value(n_c)) % prime
    else:
        a = alphabet_size*p_value % prime
        b = (-alphabet_size*char_value(p_c)*weight) % prime
        c = char_value(n_c) % prime
        n_value = (a+b+c) % prime
    return n_value


def find_KR(string, text):
    found_occurrences = []
    word_length = len(string)
    first_window = text[:word_length]
    weight = 1
    for i in range(0, word_length - 1):
        weight = (alphabet_size*weight) % prime
    hash_cword = 0
    hash_str = 0
    if not string or not text:
        return found_occurrences
    for i, j in zip(string, first_window):
        hash_cword = hash_KR(hash_cword, weight, j)
        hash_str = hash_KR(hash_str, weight, i)
    for i in range(0, len(text) - word_length + 1):
        if hash_cword == hash_str:
            for j in range(0, word_length):
                if text[i+j] != string[j]:
                    break
                elif j == word_length - 1:
                    found_occurrences.append(i)
        if i != len(text) - word_length:
            hash_cword = hash_KR(hash_cword, weight, text[i+word_length], text[i])
    return found_occurrences
