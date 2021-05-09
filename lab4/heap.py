class Heap:
    def __init__(self, values, heap_width):
        self.width = heap_width
        self.values = [0]
        self.number_of_values = 0
        for value in values:
            self.add(value)

    """def heapify(self, index):
        max_child = 0
        max_child_index = 0
        for i in range(heap_width):
           if(self.values[index] < self.values[2*index+i]):
           if(self.values[2*index+i] > max_child):
               max_child = self.values[2*index+i]
               max_child_index = i
        if()
        if(self.values[index] < self.values[2*index+i]):
            if"""

    def add(self, new_value):
        self.values.append(new_value)
        self.number_of_values += 1
        new_place = self.number_of_values
        parent_place = (new_place + self.width - 2) // self.width
        while (new_place != 1 and new_value > self.values[parent_place]):
            self.values[new_place] = self.values[parent_place]
            self.values[parent_place] = new_value
            new_place = parent_place
            parent_place = (new_place + self.width - 2) // self.width


    """def remove_top(self):
        self.values[1] = 0
        parent_place = 1
        child_place = (parent_place * self.width)-(self.width - 2)
        print(self.values)
        while child_place < len(self.values):
            max_child = 0
            max_child_place = 0
            for i in range(self.width):
                try:
                    if(self.values[child_place+i] > max_child):
                        max_child = self.values[child_place+i]
                        max_child_place = child_place+i
                except IndexError:
                    continue
            self.values[parent_place] = max_child
            parent_place = max_child_place
            self.values[parent_place] = 0
            child_place = (parent_place * self.width)-(self.width - 2)
            print(self.values)
        if()"""

    def remove_root(self):
        self.values[1] = self.values[len(self.values)-1]
        self.values.pop()
        parent_place = 1
        child_place = (parent_place * self.width)-(self.width - 2)
        not_end_of_procedure = True
        while child_place < len(self.values) and not_end_of_procedure:
            max_child = 0
            max_child_place = 0
            for i in range(self.width):
                try:
                    if(self.values[child_place+i] > max_child):
                        max_child = self.values[child_place+i]
                        max_child_place = child_place+i
                except IndexError:
                    continue
            if(max_child > self.values[parent_place]):
                temp = self.values[parent_place]
                self.values[parent_place] = max_child
                parent_place = max_child_place
                self.values[parent_place] = temp
                child_place = (parent_place * self.width)-(self.width - 2)
            else:
                not_end_of_procedure = False


    def print(self):
        enter_moment = 1
        iterator = 1
        while iterator < len(self.values):
            string = ""
            for i in range(enter_moment):
                if(iterator >= len(self.values)):
                    break
                if( i % self.width == 0):
                    string += "| "
                string += str(self.values[iterator]) + ' '
                iterator += 1
            enter_moment *= self.width
            string += "|"
            print(string)



heap_ass = Heap([10, 9, 5, 1, 8, 7, 6, 4, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 2)
print(heap_ass.values)
print("")
print("")
heap_ass.remove_root()
print(heap_ass.values)
heap_ass.print()
