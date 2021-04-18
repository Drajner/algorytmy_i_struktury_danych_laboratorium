from bst_tree import BST, Node
from random import sample


class AVL(BST):
    def __init__(self, numbers):
        self.root = Node_AVL(numbers[0])
        for number in numbers:
            if number == self.root.value:
                continue
            new_node = Node_AVL(number)
            self.root.add_child(new_node)
            self.balance(new_node)

    def balance(self, node):
        current_node = node
        while current_node is not None:
            heights = current_node.get_child_heights()
            current_node.height = 1 + max(heights)
            balance = heights[1] - heights[0]
            if balance == 2:
                if current_node.right_child.value <= node.value:
                    current_node.rotate_left()
                else:
                    current_node.right_child.rotate_right()
                    current_node.rotate_left()
            if balance == -2:
                if current_node.left_child.value <= node.value:
                    current_node.left_child.rotate_left()
                    current_node.rotate_right()
                else:
                    current_node.rotate_right()
            current_node = current_node.parent
        self.update_root()

    def update_root(self):
        if self.root.parent is not None:
            current_node = self.root.parent
            while current_node.parent is not None:
                current_node = current_node.parent
            self.root = current_node

    def add_node(self, number):
        new_node = Node_AVL(number)
        self.root.add_child(new_node)
        self.balance(new_node)

    def delete_node(self, number):
        node_to_delete = self.search(number)
        node_to_balance = node_to_delete.parent
        root_changed = node_to_delete.delete()
        if root_changed:
            self.root = root_changed
        else:
            self.balance(node_to_balance)


class Node_AVL(Node):
    def __init__(self, value, left_node=None, right_node=None, parent=None, height=1):
        super().__init__(value, left_node, right_node, parent)
        self.height = height

    def rotate_left(self):
        r_child = self.right_child
        r_child.parent = self.parent
        if self.parent is not None:
            if self.value < self.parent.value:
                self.parent.left_child = r_child
            else:
                self.parent.right_child = r_child
        self.right_child = r_child.left_child
        if self.right_child is not None:
            self.right_child.parent = self
        self.parent = r_child
        r_child.left_child = self
        r_heights = r_child.get_child_heights()
        r_child.height = 1 + max(r_heights)
        heights = self.get_child_heights()
        self.height = 1 + max(heights)

    def rotate_right(self):
        l_child = self.left_child
        l_child.parent = self.parent
        if self.parent is not None:
            if self.value < self.parent.value:
                self.parent.left_child = l_child
            else:
                self.parent.right_child = l_child
        self.left_child = l_child.right_child
        if self.left_child is not None:
            self.left_child.parent = self
        l_child.right_child = self
        self.parent = l_child
        l_heights = l_child.get_child_heights()
        l_child.height = 1 + max(l_heights)
        heights = self.get_child_heights()
        self.height = 1 + max(heights)

    def get_child_heights(self):
        l_child = self.left_child
        r_child = self.right_child
        heights = []
        for child in [l_child, r_child]:
            if child is None:
                heights.append(0)
            else:
                heights.append(child.height)
        return heights


if __name__ == "__main__":
    numbers = sample(range(0, 15000), 100)
    deleted_nums = sample(numbers, 90)
    tree = AVL(numbers)
    print(tree)
