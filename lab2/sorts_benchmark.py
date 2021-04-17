from sorts import bubble_sort, selection_sort, quick_sort, merge_sort
import os
import timeit


def get_table_of_words(num_of_words):
    iterator = 0
    table = []
    folder_name = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(folder_name, 'tadeusz.txt')
    with open(file_name, "r", encoding="utf8") as file:
        file_text = file.readlines()
        for line in file_text:
            words = line.split()
            for word in words:
                if iterator == num_of_words:
                    return table
                table.append(word)
                iterator += 1
    return table


def get_times():
    print('dupa')
    tests_not_finished = True
    num_of_words = 1000
    results = {'Bubble': [], 'Selection': [], 'Merge': [], 'Quick': []}
    while(tests_not_finished):
        table_of_words = get_table_of_words(num_of_words)
        results['Bubble'].append(timeit.timeit('sorts.bubble_sort(table)', setup="import sorts; from __main__ import get_table_of_words; num = %i;table = get_table_of_words(num)" % (num_of_words,), number=100))
        print(results['Bubble'])
        results['Selection'].append(timeit.timeit('sorts.selection_sort(table)', setup="import sorts; from __main__ import get_table_of_words; num = %i;table = get_table_of_words(num)" % (num_of_words,), number=100))
        print(results['Selection'])
        results['Merge'].append(timeit.timeit('sorts.merge_sort(table)', setup="import sorts; from __main__ import get_table_of_words; num = %i;table = get_table_of_words(num)" % (num_of_words,), number=100))
        print(results['Merge'])
        results['Quick'].append(timeit.timeit('sorts.quick_sort(table)', setup="import sorts; from __main__ import get_table_of_words; num = %i;table = get_table_of_words(num)" % (num_of_words,), number=100))
        print(results['Quick'])
        num_of_words += 1000
        print(num_of_words)
        if num_of_words > 10000:
            tests_not_finished = False
    return results


result = get_times()
