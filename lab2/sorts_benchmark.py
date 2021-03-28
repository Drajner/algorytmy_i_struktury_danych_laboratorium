from sorts import bubble_sort, selection_sort, quick_sort, merge_sort
import os
import timeit
from matplotlib import pyplot


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


def get_times(iter_times=1):
    tests_not_finished = True
    num_of_words = 1000
    results = {'Bubble': [], 'Selection': [], 'Merge': [], 'Quick': []}
    while(tests_not_finished):
        results['Bubble'].append(timeit.timeit('sorts.bubble_sort(table)', setup="import sorts; from __main__ import get_table_of_words; num = %i;table = get_table_of_words(num)" % (num_of_words,), number=iter_times))
        results['Selection'].append(timeit.timeit('sorts.selection_sort(table)', setup="import sorts; from __main__ import get_table_of_words; num = %i;table = get_table_of_words(num)" % (num_of_words,), number=iter_times))
        results['Merge'].append(timeit.timeit('sorts.merge_sort(table)', setup="import sorts; from __main__ import get_table_of_words; num = %i;table = get_table_of_words(num)" % (num_of_words,), number=iter_times))
        quick_temp_table = []
        for i in range(1, iter_times):
            quick_temp_table.append(timeit.timeit('sorts.quick_sort(table)', setup="import sorts; from __main__ import get_table_of_words; num = %i;table = get_table_of_words(num)" % (num_of_words,), number=1))
        results['Quick'].append(sum(quick_temp_table))
        num_of_words += 1000
        if num_of_words > 10000:
            tests_not_finished = False
    return results


def plot_data(x_axis, y_axis, x_label="", y_label=""):
    pyplot.plot(x_axis, y_axis, 'bo--', linewidth=2, markersize=12)
    pyplot.ylabel(y_label)
    pyplot.xlabel(x_label)
    pyplot.xticks(x_axis)


if __name__ == "__main__":
    iter_times = 10
    results = get_times(iter_times)
    for name in results:
        y_axis = results[name]
        x_axis = [i*1000 for i in range(1, 11)]
        x_label = "Liczba sortowanych słów"
        y_label = "Czas [s] posortowania n razy za pomocą " + name.lower() + " sort" + f" [n={iter_times}]"
        plot_data(x_axis, y_axis, x_label, y_label)
        pyplot.legend([name + " sort"])
        pyplot.savefig(name + ".png")
        pyplot.clf()
