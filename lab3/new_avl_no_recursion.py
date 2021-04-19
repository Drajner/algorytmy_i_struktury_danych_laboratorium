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
        for num in numbers[1:]:
            self.add_node(Node_AVL(num))

    def add_node(self, node):
        if self.root is None:
            self.root = node
            return node
        current_node = self.root
        placed = False
        visited_nodes = []
        while not placed:
            visited_nodes.insert(0, current_node)
            if node.value >= current_node.value:
                if current_node.right_child:
                    current_node = current_node.right_child
                else:
                    current_node.right_child = node
                    placed = True
            else:
                if current_node.left_child:
                    current_node = current_node.left_child
                else:
                    current_node.left_child = node
                    placed = True

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

    def balance_tree(self, visited_nodes):
        pass

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
        deleted_node = self.search(number)
        if deleted_node is None:
            return
        children = [deleted_node.left_child, deleted_node.right_child]
        if children == [None, None]:
            pass
