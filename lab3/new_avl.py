from random import sample

class Node_AVL():
    def __init__(self, value, left_child=None, right_child=None, height=1, balance=0):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.height = height
        self.balance = balance


class AVL_tree():
    def __init__(self, numbers=None):
        if numbers is None:
            self.root = None
        else:
            self.root = Node_AVL(numbers[0])
        try:
            for num in numbers[1:]:
                self.add_node(self.root, num)
        except Exception:
            pass

    def add_node(self, current_node, number):
        if current_node is None:
            return Node_AVL(number)
        if number >= current_node.value:
            current_node.right_child = self.add_node(current_node.right_child, number)
        else:
            current_node.left_child = self.add_node(current_node.left_child, number)
        self.update_node_height_balance(current_node)
        if current_node.balance > 1:
            if current_node.right_child.value <= number:
                current_node = self.rotate_left(current_node)
            else:
                current_node.right_child = self.rotate_right(current_node.right_child)
                current_node = self.rotate_left(current_node)
        if current_node.balance < -1:
            if current_node.left_child.value <= number:
                current_node.left_child = self.rotate_left(current_node.left_child)
                current_node = self.rotate_right(current_node)
            else:
                current_node = self.rotate_right(current_node)
        return current_node

    def search(self, number):
        current_node = self.root
        while True:
            if number > current_node.value:
                if current_node.right_child:
                    current_node = current_node.right_child
                else:
                    return None
            elif number < current_node.value:
                if current_node.left_child:
                    current_node = current_node.left_child
                else:
                    return None
            else:
                return current_node

    def rotate_right(self, node):
        temp = node.left_child.right_child
        switched_node = node.left_child
        node.left_child.right_child = node
        node.left_child = temp
        self.update_node_height_balance(node)
        self.update_node_height_balance(switched_node)
        if node == self.root:
            self.root = switched_node
        return switched_node

    def rotate_left(self, node):
        temp = node.right_child.left_child
        switched_node = node.right_child
        node.right_child.left_child = node
        node.right_child = temp
        self.update_node_height_balance(node)
        self.update_node_height_balance(switched_node)
        if node == self.root:
            self.root = switched_node
        return switched_node

    def update_node_height_balance(self, node):
        l_height = 0
        r_height = 0
        if node.left_child is not None:
            l_height = node.left_child.height
        if node.right_child is not None:
            r_height = node.right_child.height
        node.height = 1 + max(r_height, l_height)
        node.balance = r_height - l_height

    def delete(self, number, node="root"):
        if node == "root":
            node = self.root
        if node is None:
            return node
        if number > node.value:
            node.right_child = self.delete(number, node.right_child)
        elif number < node.value:
            node.left_child = self.delete(number, node.left_child)
        else:
            children = [node.left_child, node.right_child]
            if children == [None, None]:
                node = None
            elif None not in children:
                i_predecessor = self.find_inorder_predecessor(node)
                node.value = i_predecessor.value
                node.left_child = self.delete(node.value, node.left_child)
            elif children[0] is None:
                node = node.right_child
            elif children[1] is None:
                node = node.left_child
        if node is None:
            return node
        self.update_node_height_balance(node)
        if node.balance > 1:
            l_height = 0
            r_height = 0
            if node.right_child.left_child is not None:
                l_height = node.right_child.left_child.height
            if node.right_child.right_child is not None:
                r_height = node.right_child.right_child.height
            if r_height >= l_height:
                node = self.rotate_left(node)
            else:
                node.left_child = self.rotate_right(node.right_child)
                node = self.rotate_left(node)
        if node.balance < -1:
            l_height = 0
            r_height = 0
            if node.left_child.left_child is not None:
                l_height = node.left_child.left_child.height
            if node.left_child.right_child is not None:
                r_height = node.left_child.right_child.height
            if r_height >= l_height:
                node.left_child = self.rotate_left(node.left_child)
                node = self.rotate_right(node)
            else:
                node = self.rotate_right(node)
        return node

    def find_inorder_predecessor(self, node):
        current_node = node.left_child
        while current_node.right_child is not None:
            current_node = current_node.right_child
        return current_node


if __name__ == "__main__":
    # numbers = [3,3,3,3,4,5,6,7,7,54,1,4,234,123]
    # deleted = [3,4,234,3,6,7,1,4,123,1]
    numbers = sample(range(15000), 1000)
    deleted = sample(numbers, 1000)
    tree = AVL_tree(numbers)
    for num in deleted:
        tree.delete(num)