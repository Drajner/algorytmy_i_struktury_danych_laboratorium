from bst_tree import BST, Node


class AVL(BST):
    def __init__(self, numbers):
        self.root = Node_AVL(numbers[0])
        for number in numbers:
            if number == self.root.value:
                continue
            self.root.insert(Node_AVL(number))


class Node_AVL(Node):
    def __init__(self, value, left_node=None, right_node=None, parent=None, height=1):
        super().__init__(value, left_node, right_node, parent)
        self.height = height

    def insert(self, new_child):
        super().add_child(new_child)
        current_node = new_child
        while current_node is not None:
            heights = current_node.get_child_hights()
            current_node.height = 1 + max(heights)
            balance = heights[1] - heights[0]
            if balance == 2:
                if current_node.right_child.value < new_child.value:
                    current_node.rotate_left()
                else:
                    current_node.right_child.rotate_right()
                    current_node.rotate_left()
            if balance == -2:
                if current_node.left_child.value < new_child.value:
                    current_node.left_child.rotate_left()
                    current_node.rotate_right()
                else:
                    current_node.rotate_right()
            current_node = current_node.parent

    def rotate_left(self):
        r_child = self.right_child
        r_child.parent = self.parent
        if self.parent is not None:
            if self.value < self.parent.value:
                self.parent.left_child = r_child
            else:
                self.parent.right_child = r_child
        self.right_child = r_child.left_child
        self.parent = r_child
        r_child.left_child = self
        r_heights = r_child.get_child_hights()
        r_child.height = 1 + max(r_heights)
        heights = self.get_child_hights()
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
        self.parent = l_child
        l_child.right_child = self
        l_heights = l_child.get_child_hights()
        l_child.height = 1 + max(l_heights)
        heights = self.get_child_hights()
        self.height = 1 + max(heights)

    def get_child_hights(self):
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
    numbers = [10, 5, 15, 3, 4, 17, 18, 18, 123, 2,3,4,62324, 1]
    tree = AVL(numbers)
    print(tree)