from bst_tree import BST
from avl_tree import AVL
import sys
import random
import timeit

sys.setrecursionlimit(10000)


def random_list(number):
    the_list = []
    for value in range(number):
        the_list.append(random.choice(range(1, 30000)))
    return the_list


def get_times():
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
        results['bst_create'].append(timeit.timeit("tree = BST(the_list[0:reps])", setup=setup_creation, number=1))
        results['avl_create'].append(timeit.timeit("tree = AVL(the_list[0:reps])", setup=setup_creation, number=1))
        results['bst_search'].append(timeit.timeit(execute_bst_search, setup=setup_bst, number=1))
        results['avl_search'].append(timeit.timeit(execute_avl_search, setup=setup_avl, number=1))
        results['bst_delete'].append(timeit.timeit(execute_bst_delete, setup=setup_bst, number=1))
        results['avl_delete'].append(timeit.timeit(execute_avl_delete, setup=setup_avl, number=1))
        if repetitions >= 10000:
            job_not_done = False
        repetitions += 1000
    return results


if __name__ == "__main__":
    print(get_times())
