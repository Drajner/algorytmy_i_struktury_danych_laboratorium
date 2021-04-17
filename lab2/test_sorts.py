from sorts import merge_sort, bubble_sort, selection_sort, quick_sort
from sorts_benchmark import get_table_of_words


def test_merge_sort():
    word_numbers = [i*1000 for i in range(1, 11)]
    for number in word_numbers:
        m_table = merge_sort(get_table_of_words(number))
        assert m_table == sorted(get_table_of_words(number))


def test_selection_sort():
    word_numbers = [i*1000 for i in range(1, 11)]
    for number in word_numbers:
        s_table = selection_sort(get_table_of_words(number))
        assert s_table == sorted(get_table_of_words(number))


def test_bubble_sort():
    word_numbers = [i*1000 for i in range(1, 11)]
    for number in word_numbers:
        b_table = bubble_sort(get_table_of_words(number))
        assert b_table == sorted(get_table_of_words(number))


def test_quick_sort():
    word_numbers = [i*1000 for i in range(1, 11)]
    for number in word_numbers:
        q_table = quick_sort(get_table_of_words(number))
        assert q_table == sorted(get_table_of_words(number))

