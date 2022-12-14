class BST:  # uses first number from numbers as root
    def __init__(self, numbers):
        self.root = Node(numbers[0])
        for number in numbers[1:]:
            new_child = Node(number)
            self.add_node(new_child)

    def add_node(self, new_child):
        current_node = self.root
        while not new_child.parent:
            if new_child.value >= current_node.value:
                if current_node.right_child is not None:
                    current_node = current_node.right_child
                else:
                    current_node.right_child = new_child
                    new_child.parent = current_node
            elif new_child.value < current_node.value:
                if current_node.left_child is not None:
                    current_node = current_node.left_child
                else:
                    current_node.left_child = new_child
                    new_child.parent = current_node
        return new_child

    def search(self, number):
        current_node = self.root
        while current_node is not None and current_node.value != number:
            if number >= current_node.value:
                current_node = current_node.right_child
            else:
                current_node = current_node.left_child
        return current_node

    def delete_node(self, number):
        if self.root is None:
            return
        node_to_delete = self.search(number)
        if self.root.left_child is None and self.root.right_child is None:
            self.root = None
            return
        root_changed = node_to_delete.delete()
        if root_changed:
            if root_changed.parent is None:
                self.root = root_changed

    def __str__(self):
        if self.root is None:
            return ""
        return self.root.stringify()


class Node:
    def __init__(self, value, left_node=None, right_node=None, parent=None):
        self.value = value
        self.left_child = left_node
        self.right_child = right_node
        self.parent = parent

    def add_child(self, new_child):
        if new_child.value >= self.value and self.right_child is None:
            self.right_child = new_child
            new_child.parent = self
        if new_child.value < self.value and self.right_child is None:
            self.left_child = new_child
            new_child.parent = self

    def search(self, number):
        if number == self.value:
            return self
        if number > self.value:
            return self.right_child
        if number < self.value:
            return self.left_child

    def delete(self):
        children = [self.left_child, self.right_child]
        if children == [None, None]:
            if self.parent.left_child == self:
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif None not in children:
            i_predecessor = self.inorder_predecessor()
            self.value = i_predecessor.value
            i_predecessor.delete()
            return i_predecessor
        elif self.right_child is None:
            if self.parent is not None:
                if self.parent.left_child == self:
                    self.parent.left_child = self.left_child
                    self.left_child.parent = self.parent
                else:
                    self.parent.right_child = self.left_child
                    self.left_child.parent = self.parent
            else:
                self.left_child.parent = None
                return self.left_child
        else:
            if self.parent is not None:
                if self.parent.left_child == self:
                    self.parent.left_child = self.right_child
                    self.right_child.parent = self.parent
                else:
                    self.parent.right_child = self.right_child
                    self.right_child.parent = self.parent
            else:
                self.right_child.parent = None
                return self.right_child

    def inorder_predecessor(self):
        current_node = self.left_child
        while current_node.right_child is not None:
            current_node = current_node.right_child
        return current_node

    def stringify(self, recurence_depth=0):
        returning_string = ""
        additional_string1 = '>'
        additional_string1 *= recurence_depth
        if self.right_child is not None:
            returning_string = returning_string + self.right_child.stringify(recurence_depth+1)
        returning_string = returning_string + additional_string1 + str(self.value) + '\n'
        if self.left_child is not None:
            returning_string = returning_string + self.left_child.stringify(recurence_depth+1)
        return returning_string
