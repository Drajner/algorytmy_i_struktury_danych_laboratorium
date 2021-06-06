from search_algorithms import find_N, find_KMP, find_KR
import os
import timeit
from matplotlib import pyplot


def get_whole_text():
    words = ""
    folder_name = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(folder_name, 'tadeusz.txt')
    with open(file_name, "r", encoding="utf8") as file:
        for line in file:
            line_words = line.split()
            for word in line_words:
                words += word
                words += ' '
    words = words.strip()
    return words


def get_words(num_of_words):
    iterator = 0
    words = ""
    folder_name = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(folder_name, 'tadeusz.txt')
    with open(file_name, "r", encoding="utf8") as file:
        file_text = file.readlines()
        for line in file_text:
            line_words = line.split()
            for word in line_words:
                if iterator == num_of_words:
                    return words
                words += word
                words += ' '
                iterator += 1
    words = words.strip()
    return words


def get_times(test_number):
    results = {"naive_algorithm": [], "KMP_algorithm": [], "KR_algorithm": []}
    text = '"' + get_whole_text() + '"'
    for i in range(1, 11):
        string = '"' + get_words(i*100) + '"'
        find_N_setup = f"""
from search_algorithms import find_N
text = {text}
string = {string}
"""

        find_KMP_setup = f"""
from search_algorithms import find_KMP
text = {text}
string = {string}
"""

        find_KR_setup = f"""
from search_algorithms import find_KR
text = {text}
string = {string}
"""

        results['naive_algorithm'].append(timeit.timeit("find_N(string, text)", setup=find_N_setup, number=test_number))
        results['KMP_algorithm'].append(timeit.timeit("find_KMP(string, text)", setup=find_KMP_setup, number=test_number))
        results['KR_algorithm'].append(timeit.timeit("find_KR(string, text)", setup=find_KR_setup, number=test_number))
        print("text")
        print(text[:1000])
        print("string")
        print(string[:1000])
        print(find_N(string, text))
    return results


def plot_data(x_axis, y_axis, x_label="", y_label="", col="b-"):
    pyplot.plot(x_axis, y_axis, col, linewidth=2)
    pyplot.ylabel(y_label)
    pyplot.xlabel(x_label)
    pyplot.xticks(x_axis)


if __name__ == "__main__":
    test_number = 1
    results = get_times(test_number)
    search_test = ['naive_algorithm', 'KMP_algorithm', 'KR_algorithm']
    legend = ["Algorytm N", "Algorytm KMP", "Algorytm KR"]
    for test in search_test:
        col = "b-"
        if test == 'KMP_algorithm':
            col = "r-"
        if test == 'KR_algorithm':
            col = "g-"
        y_axis = results[test]
        x_axis = [i*100 for i in range(1, 11)]
        x_label = "Liczba wyszukiwanych słów"
        y_label = "Czas [s]"
        plot_data(x_axis, y_axis, x_label, y_label, col)
    pyplot.title("Wyszukiwanie słów w tekście")
    pyplot.legend(legend)
    pyplot.savefig("lab5/" + "search_diagram" + ".png")
    pyplot.clf()
