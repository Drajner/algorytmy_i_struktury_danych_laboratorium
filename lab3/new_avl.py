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

    def delete(self, number):
        node_to_delete = self.search(number)
        children = [node_to_delete.left_child, node_to_delete.right_child]
        if children == [None, None]:
            pass
        if None not in children:
            pass
        if children[0] is None:
            pass
        if children[1] is None:
            pass
