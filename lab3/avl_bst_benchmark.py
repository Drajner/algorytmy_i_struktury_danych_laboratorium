import sys
import random
import timeit
from matplotlib import pyplot

sys.setrecursionlimit(10000)


def random_list(number):
    the_list = []
    for value in range(number):
        the_list.append(random.choice(range(1, 30000)))
    return the_list


def get_times(test_number):
    results = {'bst_create': [], 'bst_search': [], 'bst_delete': [], 'avl_create': [], 'avl_search': [], 'avl_delete': []}
    the_list = random_list(10000)
    job_not_done = True
    repetitions = 1000
    while job_not_done:
        setup_creation = f"""
from avl_tree import AVL
from bst_tree import BST
from __main__ import random_list
reps = {repetitions}
the_list = {the_list}
"""
        setup_bst = f"""
from bst_tree import BST
from __main__ import random_list
reps = {repetitions}
the_list = {the_list}
tree = BST(the_list)
"""
        setup_avl = f"""
from bst_tree import BST
from avl_tree import AVL
from __main__ import random_list
reps = {repetitions}
the_list = {the_list}
tree = AVL(the_list)
"""
        execute_bst_search = """
for value in the_list[0:reps]:
    tree.search(value)
"""
        execute_avl_search = """
for value in the_list[0:reps]:
    tree.search(value)
"""
        execute_bst_delete = """
for value in the_list[0:reps]:
    tree.delete_node(value)
"""
        execute_avl_delete = """
for value in the_list[0:reps]:
    tree.delete_node(value)
"""
        results['bst_create'].append(timeit.timeit("tree = BST(the_list[0:reps])", setup=setup_creation, number=test_number))
        results['avl_create'].append(timeit.timeit("tree = AVL(the_list[0:reps])", setup=setup_creation, number=test_number))
        results['bst_search'].append(timeit.timeit(execute_bst_search, setup=setup_bst, number=test_number))
        results['avl_search'].append(timeit.timeit(execute_avl_search, setup=setup_avl, number=test_number))
        results['bst_delete'].append(sum(timeit.repeat(execute_bst_delete, setup=setup_bst, repeat=test_number, number=1)))
        results['avl_delete'].append(sum(timeit.repeat(execute_avl_delete, setup=setup_avl, repeat=test_number, number=1)))
        if repetitions >= 10000:
            job_not_done = False
        repetitions += 1000
    return results


def plot_data(x_axis, y_axis, x_label="", y_label="", col="b-"):
    pyplot.plot(x_axis, y_axis, col, linewidth=2)
    pyplot.ylabel(y_label)
    pyplot.xlabel(x_label)
    pyplot.xticks(x_axis)


if __name__ == "__main__":
    test_number = 10
    results = get_times(test_number)
    creation = ["bst_create", "avl_create"]
    searching = ["bst_search", "avl_search"]
    deletion = ["bst_delete", "avl_delete"]
    tests = [creation, searching, deletion]
    for test_category in tests:
        for test in test_category:
            col = "b-"
            if test[:3] == "avl":
                col = "r-"
            y_axis = results[test]
            x_axis = [i*1000 for i in range(1, 11)]
            x_label = "Liczba elementów"
            y_label = "Czas [s]"
            plot_data(x_axis, y_axis, x_label, y_label, col)
        pyplot.title(f"Liczba powtórzeń {test_number}")
        pyplot.legend(test_category)
        pyplot.savefig("lab3/" + test_category[0][-6:] + ".png")
        pyplot.clf()
