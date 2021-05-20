from search_algorithms import find_N, find_KMP, find_KR
import random


def test_N_empty_word():
    word = str()
    text = "apple"
    res = find_N(word, text)
    assert(res == [])


def test_N_empty_text():
    word = "apple"
    text = str()
    res = find_N(word, text)
    assert(res == [])


def test_N_empty_word_and_text():
    word = str()
    text = str()
    res = find_N(word, text)
    assert(res == [])


def test_N_eq():
    word = "Apple"
    text = "Apple"
    res = find_N(word, text)
    assert(res == [0])


def test_N_word_longer():
    word = "Appleadsa"
    text = "Apple"
    res = find_N(word, text)
    assert(res == [])


def test_N_not_occurring():
    word = "Apple"
    text = "ABpple"
    res = find_N(word, text)
    assert(res == [])


def test_N_1():
    word = "Apple"
    text = "ABpple Apple, App, BApple"
    res = find_N(word, text)
    assert(res == [7, 20])


def test_N_2():
    word = "AB"
    text = "AAABAAABAAABBBABABABBBBB"
    res = find_N(word, text)
    assert(res == [2, 6, 10, 14, 16, 18])


def test_N_3():
    word = "AAA"
    text = "AAAAAAA AAAAA AAAA AAA AA A"
    res = find_N(word, text)
    assert(res == [0, 1, 2, 3, 4, 8, 9, 10, 14, 15, 19])


def test_KMP_empty_word():
    word = str()
    text = "apple"
    res = find_KMP(word, text)
    assert(res == [])


def test_KMP_empty_text():
    word = "apple"
    text = str()
    res = find_KMP(word, text)
    assert(res == [])


def test_KMP_empty_word_and_text():
    word = str()
    text = str()
    res = find_KMP(word, text)
    assert(res == [])


def test_KMP_eq():
    word = "Apple"
    text = "Apple"
    res = find_KMP(word, text)
    assert(res == [0])


def test_KMP_word_longer():
    word = "Appleadsa"
    text = "Apple"
    res = find_KMP(word, text)
    assert(res == [])


def test_KMP_not_occurring():
    word = "Apple"
    text = "ABpple"
    res = find_KMP(word, text)
    assert(res == [])


def test_KMP_1():
    word = "Apple"
    text = "ABpple Apple, App, BApple"
    res = find_KMP(word, text)
    assert(res == [7, 20])


def test_KMP_2():
    word = "AB"
    text = "AAABAAABAAABBBABABABBBBB"
    res = find_N(word, text)
    assert(res == [2, 6, 10, 14, 16, 18])


def test_KMP_3():
    word = "AAA"
    text = "AAAAAAA AAAAA AAAA AAA AA A"
    res = find_KMP(word, text)
    assert(res == [0, 1, 2, 3, 4, 8, 9, 10, 14, 15, 19])


def test_KR_empty_word():
    word = str()
    text = "apple"
    res = find_KR(word, text)
    assert(res == [])


def test_KR_empty_text():
    word = "apple"
    text = str()
    res = find_KR(word, text)
    assert(res == [])


def test_KR_empty_word_and_text():
    word = str()
    text = str()
    res = find_KR(word, text)
    assert(res == [])


def test_KR_eq():
    word = "Apple"
    text = "Apple"
    res = find_KR(word, text)
    assert(res == [0])


def test_KR_word_longer():
    word = "Appleadsa"
    text = "Apple"
    res = find_KR(word, text)
    assert(res == [])


def test_KR_not_occurring():
    word = "Apple"
    text = "ABpple"
    res = find_KR(word, text)
    assert(res == [])


def test_all():
    results = []
    alphabet = ["A", "B"]
    for i in range(0, 200):
        text = "".join(random.choice(alphabet) for i in range(0, 1000))
        word = "".join(random.choice(alphabet) for i in range(0, 3))
        results.append(find_KMP(word, text) == find_N(word, text) == find_KR(word, text))
    assert(all(results))
