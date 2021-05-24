from heap import Heap
import random
import timeit
from matplotlib import pyplot

def get_list(number):
    elements = random.choices(range(0, 300000), k=number)
    return elements

def get_times(test_number):
    results = {"2-Heap_create": [], "3-Heap_create": [], "4-Heap_create": [], "2-Heap_delete": [], "3-Heap_delete": [], "4-Heap_delete": []}
    elements = get_list(100000)
    for i in [j*10000 for j in range(1, 11)]:
        creation_setup = f"""
from heap import Heap
elements = {elements}
i={i}
"""
        deletion_setup_2 = "\nhp = Heap(elements, 2)"
        deletion_setup_3 = "\nhp = Heap(elements, 3)"
        deletion_setup_4 = "\nhp = Heap(elements, 4)"
        deletion="""
for number in range(0, i):
    hp.remove_root()
"""
        results['2-Heap_create'].append(timeit.timeit("Heap(elements[0:i], 2)", setup=creation_setup, number=test_number))
        results['3-Heap_create'].append(timeit.timeit("Heap(elements[0:i], 3)", setup=creation_setup, number=test_number))
        results['4-Heap_create'].append(timeit.timeit("Heap(elements[0:i], 4)", setup=creation_setup, number=test_number))
        results['2-Heap_delete'].append(timeit.timeit(deletion, setup=creation_setup + deletion_setup_2, number=test_number))
        results['3-Heap_delete'].append(timeit.timeit(deletion, setup=creation_setup + deletion_setup_3, number=test_number))
        results['4-Heap_delete'].append(timeit.timeit(deletion, setup=creation_setup + deletion_setup_4, number=test_number))
    return results

def plot_data(x_axis, y_axis, x_label="", y_label="", col="b-"):
    pyplot.plot(x_axis, y_axis, col, linewidth=2)
    pyplot.ylabel(y_label)
    pyplot.xlabel(x_label)
    pyplot.xticks(x_axis)

if __name__ == "__main__":
    test_number = 1
    results = get_times(test_number)
    creation = ['2-Heap_create', '3-Heap_create', '4-Heap_create']
    deletion = ['2-Heap_delete', '3-Heap_delete', '4-Heap_delete']
    tests = [creation, deletion]
    for test_category in tests:
        legend = []
        for test in test_category:
            col = "b-"
            if test[0] == "3":
                col = "r-"
            if test[0] == "4":
                col = "g-"
            y_axis = results[test]
            x_axis = [i*1000 for i in range(1, 11)]
            x_label = "Liczba elementów"
            y_label = "Czas [s]"
            plot_data(x_axis, y_axis, x_label, y_label, col)
            legend.append(test[:6])
        operation_name = test_category[0][-6:]
        pyplot.title(f"{operation_name.title()} - liczba powtórzeń {test_number}")
        pyplot.legend(legend)
        pyplot.savefig("lab4/" + operation_name + ".png")
        pyplot.clf()