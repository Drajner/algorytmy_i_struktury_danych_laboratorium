from bst_tree import BST, Node
from random import sample


class AVL(BST):
    def __init__(self, numbers):
        self.root = Node_AVL(numbers[0])
        for number in numbers[1:]:
            new_node = Node_AVL(number)
            self.add_node(new_node)

    def balance(self, node):
        current_node = node
        node_balanced = False
        while current_node is not None and not node_balanced:
            heights = current_node.get_child_heights()
            current_node.height = 1 + max(heights)
            balance = heights[1] - heights[0]
            if balance == 2:
                if current_node.right_child.value <= node.value:
                    current_node.rotate_left()
                else:
                    current_node.right_child.rotate_right()
                    current_node.rotate_left()
                node = current_node
                node_balanced = True
            if balance == -2:
                if current_node.left_child.value <= node.value:
                    current_node.left_child.rotate_left()
                    current_node.rotate_right()
                else:
                    current_node.rotate_right()
                node_balanced = True
                node = current_node
            current_node = current_node.parent
        self.update_root()

    def update_root(self):
        if self.root.parent is not None:
            current_node = self.root.parent
            while current_node.parent is not None:
                current_node = current_node.parent
            self.root = current_node

    def add_node(self, new_node):
        super().add_node(new_node)
        self.balance(new_node)

    def delete_node(self, number):
        node_to_delete = self.search(number)
        if self.root.left_child is None and self.root.right_child is None:
            self.root = None
            return
        if self.root.left_child is None or self.root.right_child is None:
            if self.root == node_to_delete:
                root_changed = node_to_delete.delete()
                self.root = root_changed
            else:
                node_to_delete.delete()
            return
        node_to_balance = node_to_delete.delete_AVL()
        current_node = node_to_balance
        while current_node is not None:
            heights = current_node.get_child_heights()
            current_node.height = 1 + max(heights)
            balance = heights[1] - heights[0]
            if balance == 2:
                try:
                    l_child_height = current_node.right_child.left_child.height
                except AttributeError:
                    l_child_height = 0
                try:
                    r_child_height = current_node.right_child.right_child.height
                except AttributeError:
                    r_child_height = 0
                if l_child_height <= r_child_height:
                    current_node.rotate_left()
                else:
                    current_node.right_child.rotate_right()
                    current_node.rotate_left()
            if balance == -2:
                try:
                    l_child_height = current_node.left_child.left_child.height
                except AttributeError:
                    l_child_height = 0
                try:
                    r_child_height = current_node.left_child.right_child.height
                except AttributeError:
                    r_child_height = 0
                if l_child_height <= r_child_height:
                    current_node.left_child.rotate_left()
                    current_node.rotate_right()
                else:
                    current_node.rotate_right()
            current_node = current_node.parent
        self.update_root()


class Node_AVL(Node):
    def __init__(self, value, left_node=None, right_node=None, parent=None, height=1):
        super().__init__(value, left_node, right_node, parent)
        self.height = height

    def rotate_left(self):
        r_child = self.right_child
        r_child.parent = self.parent  # here
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

    def delete_AVL(self):
        i_pred = super().delete()
        if i_pred is not None:
            return i_pred.parent
        if self.right_child and self.left_child:
            return self
        if self.left_child:
            return self.left_child
        if self.right_child:
            return self.right_child
        return self.parent


if __name__ == "__main__":
    # numbers = sample(range(0, 150), 50)
    # print(numbers)
    # deleted = sample(numbers, 50)
    # print(deleted)
    numbers = [12, 1, 6, 14, 0, 11, 7, 10, 8, 4, 4,4,4, 4]
    deleted = [4, 0, 6, 12, 10, 11, 14, 8, 1, 7,4,4]
    tree = AVL(numbers)
    print(tree)
    for num in deleted:
        tree.delete_node(num)
    print(tree)
