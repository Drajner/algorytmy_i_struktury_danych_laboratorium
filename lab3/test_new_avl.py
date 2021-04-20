from new_avl import AVL_tree


def test_AVL():
    tree = AVL_tree([1, 2, 3, 4])
    assert tree.root.value == 2
    assert tree.root.right_child.value == 3
    assert tree.root.right_child.right_child.value == 4
    assert tree.root.left_child.value == 1


def test_AVL_1():
    tree = AVL_tree([1, 2, 1.5, 4])
    assert tree.root.value == 1.5
    assert tree.root.right_child.value == 2
    assert tree.root.right_child.right_child.value == 4
    assert tree.root.left_child.value == 1


def test_AVL_2():
    tree = AVL_tree([3, 2, 1, 4])
    assert tree.root.value == 2
    assert tree.root.right_child.value == 3
    assert tree.root.right_child.right_child.value == 4
    assert tree.root.left_child.value == 1


def test_AVL_3():
    tree = AVL_tree([3, 0.5, 1, 4])
    assert tree.root.value == 1
    assert tree.root.right_child.value == 3
    assert tree.root.right_child.right_child.value == 4
    assert tree.root.left_child.value == 0.5


def test_AVL_4():
    tree = AVL_tree([3, 0.5, 1, 4, 0.4])
    assert tree.root.value == 1
    assert tree.root.right_child.value == 3
    assert tree.root.right_child.right_child.value == 4
    assert tree.root.left_child.value == 0.5
    assert tree.root.left_child.left_child.value == 0.4


def test_AVL_5():
    tree = AVL_tree([3, 0.5, 1, 4, 0.4, 0.75])
    assert tree.root.value == 1
    assert tree.root.right_child.value == 3
    assert tree.root.right_child.right_child.value == 4
    assert tree.root.left_child.value == 0.5
    assert tree.root.left_child.left_child.value == 0.4
    assert tree.root.left_child.right_child.value == 0.75


def test_AVL_6():
    tree = AVL_tree([3, 0.5, 1, 4, 0.4, 0.75, 5])
    assert tree.root.value == 1
    assert tree.root.right_child.value == 4
    assert tree.root.right_child.left_child.value == 3
    assert tree.root.right_child.right_child.value == 5
    assert tree.root.left_child.value == 0.5
    assert tree.root.left_child.left_child.value == 0.4
    assert tree.root.left_child.right_child.value == 0.75


def test_AVL_7():
    tree = AVL_tree([3, 0.5, 1, 4, 0.4, 0.75, 5, 3])
    assert tree.root.value == 1
    assert tree.root.right_child.value == 4
    assert tree.root.right_child.left_child.value == 3
    assert tree.root.right_child.left_child.right_child.value == 3
    assert tree.root.right_child.right_child.value == 5
    assert tree.root.left_child.value == 0.5
    assert tree.root.left_child.left_child.value == 0.4
    assert tree.root.left_child.right_child.value == 0.75


def test_AVL_8():
    tree = AVL_tree([3, 0.5, 1, 4, 0.4, 0.75, 5, 3, 3])
    assert tree.root.value == 1
    assert tree.root.right_child.value == 4
    assert tree.root.right_child.left_child.value == 3
    assert tree.root.right_child.left_child.left_child.value == 3
    assert tree.root.right_child.left_child.right_child.value == 3
    assert tree.root.right_child.right_child.value == 5
    assert tree.root.left_child.value == 0.5
    assert tree.root.left_child.left_child.value == 0.4
    assert tree.root.left_child.right_child.value == 0.75


def test_AVL_9():
    tree = AVL_tree([3, 0.5, 1, 4, 0.4, 0.75, 5, 3, 3, 3])
    assert tree.root.value == 1
    assert tree.root.right_child.value == 3
    assert tree.root.right_child.left_child.value == 3
    assert tree.root.right_child.left_child.left_child.value == 3
    assert tree.root.right_child.right_child.value == 4
    assert tree.root.right_child.right_child.right_child.value == 5
    assert tree.root.right_child.right_child.left_child.value == 3
    assert tree.root.left_child.value == 0.5
    assert tree.root.left_child.left_child.value == 0.4
    assert tree.root.left_child.right_child.value == 0.75


def test_AVL_10():
    tree = AVL_tree([3, 0.5, 1, 4, 0.4, 0.75, 5, 3, 3, 3, 6])
    assert tree.root.value == 3
    assert tree.root.right_child.value == 4
    assert tree.root.right_child.left_child.value == 3
    assert tree.root.right_child.right_child.value == 5
    assert tree.root.right_child.right_child.right_child.value == 6
    assert tree.root.right_child.right_child.left_child is None
    assert tree.root.left_child.value == 1
    assert tree.root.left_child.left_child.value == 0.5
    assert tree.root.left_child.left_child.left_child.value == 0.4
    assert tree.root.left_child.left_child.right_child.value == 0.75
    assert tree.root.left_child.right_child.value == 3
    assert tree.root.left_child.right_child.left_child.value == 3


def test_AVL_11():
    tree = AVL_tree([3, 0.5, 1, 4, 0.4, 0.75, 5, 3, 3, 3, 6, 0.3, 0.25])
    assert tree.root.value == 3
    assert tree.root.right_child.value == 4
    assert tree.root.right_child.left_child.value == 3
    assert tree.root.right_child.right_child.value == 5
    assert tree.root.right_child.right_child.right_child.value == 6
    assert tree.root.right_child.right_child.left_child is None
    assert tree.root.left_child.value == 1
    assert tree.root.left_child.left_child.value == 0.5
    assert tree.root.left_child.left_child.left_child.value == 0.3
    assert tree.root.left_child.left_child.right_child.value == 0.75
    assert tree.root.left_child.right_child.value == 3
    assert tree.root.left_child.right_child.left_child.value == 3
    assert tree.root.left_child.left_child.left_child.left_child.value == 0.25
    assert tree.root.left_child.left_child.left_child.right_child.value == 0.4


def test_AVL_12():
    tree = AVL_tree([3, 0.5, 1, 4, 0.4, 0.75, 5, 3, 3, 3, 6, 0.3, 0.25, 0.45])
    assert tree.root.value == 3
    assert tree.root.right_child.value == 4
    assert tree.root.right_child.left_child.value == 3
    assert tree.root.right_child.right_child.value == 5
    assert tree.root.right_child.right_child.right_child.value == 6
    assert tree.root.right_child.right_child.left_child is None
    assert tree.root.left_child.value == 1
    assert tree.root.left_child.left_child.value == 0.4
    assert tree.root.left_child.left_child.left_child.value == 0.3
    assert tree.root.left_child.left_child.right_child.value == 0.5
    assert tree.root.left_child.left_child.right_child.left_child.value == 0.45
    assert tree.root.left_child.left_child.right_child.right_child.value == 0.75
    assert tree.root.left_child.left_child.left_child.left_child.value == 0.25
    assert tree.root.left_child.right_child.value == 3
    assert tree.root.left_child.right_child.left_child.value == 3


def test_AVL_deletion():
    tree = AVL_tree([3, 0.5, 1, 4, 0.4, 0.75, 5, 3, 3, 3, 6, 0.3, 0.25, 0.45])
    tree.delete(0.75)
    assert tree.root.value == 3
    assert tree.root.right_child.value == 4
    assert tree.root.right_child.left_child.value == 3
    assert tree.root.right_child.right_child.value == 5
    assert tree.root.right_child.right_child.right_child.value == 6
    assert tree.root.right_child.right_child.left_child is None
    assert tree.root.left_child.value == 1
    assert tree.root.left_child.left_child.value == 0.4
    assert tree.root.left_child.left_child.left_child.value == 0.3
    assert tree.root.left_child.left_child.right_child.value == 0.5
    assert tree.root.left_child.left_child.right_child.left_child.value == 0.45
    assert tree.root.left_child.left_child.right_child.right_child is None
    assert tree.root.left_child.left_child.left_child.left_child.value == 0.25
    assert tree.root.left_child.right_child.value == 3
    assert tree.root.left_child.right_child.left_child.value == 3


def test_AVL_deletion_1():
    tree = AVL_tree([3, 0.5, 1, 4, 0.4, 0.75, 5, 3, 3, 3, 6, 0.3, 0.25, 0.45])
    tree.delete(0.75)
    tree.delete(0.45)
    assert tree.root.value == 3
    assert tree.root.right_child.value == 4
    assert tree.root.right_child.left_child.value == 3
    assert tree.root.right_child.right_child.value == 5
    assert tree.root.right_child.right_child.right_child.value == 6
    assert tree.root.right_child.right_child.left_child is None
    assert tree.root.left_child.value == 1
    assert tree.root.left_child.left_child.value == 0.4
    assert tree.root.left_child.left_child.left_child.value == 0.3
    assert tree.root.left_child.left_child.right_child.value == 0.5
    assert tree.root.left_child.left_child.right_child.left_child is None
    assert tree.root.left_child.left_child.right_child.right_child is None
    assert tree.root.left_child.left_child.left_child.left_child.value == 0.25
    assert tree.root.left_child.right_child.value == 3
    assert tree.root.left_child.right_child.left_child.value == 3


def test_AVL_deletion_2():
    tree = AVL_tree([3, 0.5, 1, 4, 0.4, 0.75, 5, 3, 3, 3, 6, 0.3, 0.25, 0.45])
    tree.delete(0.75)
    tree.delete(0.45)
    tree.delete(0.5)
    assert tree.root.value == 3
    assert tree.root.right_child.value == 4
    assert tree.root.right_child.left_child.value == 3
    assert tree.root.right_child.right_child.value == 5
    assert tree.root.right_child.right_child.right_child.value == 6
    assert tree.root.right_child.right_child.left_child is None
    assert tree.root.left_child.value == 1
    assert tree.root.left_child.left_child.value == 0.3
    assert tree.root.left_child.left_child.left_child.value == 0.25
    assert tree.root.left_child.left_child.right_child.value == 0.4
    assert tree.root.left_child.right_child.value == 3
    assert tree.root.left_child.right_child.left_child.value == 3
