class Node_AVL():
    def __init__(self, value, left_child=None, right_child=None, height=1, balance=0):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.height = height
        self.balance = balance


class AVL():
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
        i = 1
        while current_node is not None and current_node.value != number:
            i += 1
            if number >= current_node.value:
                current_node = current_node.right_child
            else:
                current_node = current_node.left_child
        return current_node, i

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

    def delete_node(self, number, node="root"):
        if self.root is None:
            return
        if node == "root":
            node = self.root
        if self.root.left_child is None and self.root.right_child is None:
            if self.root.value == number:
                self.root = None
        if node is None:
            return node
        if number > node.value:
            node.right_child = self.delete_node(number, node.right_child)
        elif number < node.value:
            node.left_child = self.delete_node(number, node.left_child)
        else:
            children = [node.left_child, node.right_child]
            if children == [None, None]:
                node = None
            elif None not in children:
                i_predecessor = self.find_inorder_predecessor(node)
                node.value = i_predecessor.value
                node.left_child = self.delete_node(node.value, node.left_child)
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
                node.right_child = self.rotate_right(node.right_child)
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
        i = 1
        while current_node.right_child is not None:
            current_node = current_node.right_child
            i += 1
            if i > 16:
                print(i)
        return current_node

    def __str__(self):
        if self.root is None:
            return ""
        return self.stringify(self.root)

    def stringify(self, node, recurence_depth=0):
        returning_string = ""
        additional_string1 = '>'
        additional_string1 *= recurence_depth
        if node.right_child is not None:
            returning_string = returning_string + self.stringify(node.right_child, recurence_depth+1)
        returning_string = returning_string + additional_string1 + str(node.value) + '\n'
        if node.left_child is not None:
            returning_string = returning_string + self.stringify(node.left_child, recurence_depth+1)
        return returning_string
