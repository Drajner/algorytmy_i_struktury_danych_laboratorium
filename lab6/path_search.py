four_directions = {(0,1), (0,-1), (1,0), (-1,0)}
class Vertex_Queue():
    def __init__(self, list=None):
        self.list = []
        if list is not None:
            for vertex in list:
                self.add_vertex(vertex)

    def add_vertex(self, new_vertex):
        for index, vertex in enumerate(self.list):
            if new_vertex.path_cost <= vertex.path_cost:
                self.list.insert(index, new_vertex)
                return index
        self.list.append(new_vertex)
        return len(self.list)

    def pop(self):
        return self.list.pop(0)
    
    def empty(self):
        return not self.list


class Vertex():
    def __init__(self, entry_cost, cost, neighbours=None, vertex=None):
        self.path_cost = cost
        self.previous_vertex = vertex
        self.entry_cost = entry_cost
        if neighbours is None:
            self.neighbours = set()
        else:
            self.neighbours = neighbours

    def setCost(self, cost):
        self.path_cost = cost

    def setPVertex(self, vertex):
        self.previous_vertex = vertex

    def addNeighbour(self, negihbour):
        self.neighbours.add(negihbour)


def find_start_and_end(array):
    points = []
    for y_c, row in enumerate(array):
        for x_c, entry_cost in enumerate(row):
            if entry_cost == 0:
                points.append((x_c, y_c))
    return points

def create_graph(array):
    graph = []
    for row in array:
        graph_row = []
        for vertex_entry_cost in row:
            graph_row.append(Vertex(vertex_entry_cost, float("inf")))
        graph.append(graph_row)
    for y_c, row in enumerate(graph):
        for x_c, vertex in enumerate(row):
            for direction in four_directions:
                x_t = x_c + direction[0]
                y_t = y_c + direction[1]
                if x_t < 0 or y_t < 0 or y_t >= len(graph) or x_t >= len(graph[y_t]):
                    continue
                vertex.addNeighbour(graph[y_t][x_t])
    return graph
                
    

def shortest_path_d(graph, start, end):
    x_s, y_s = start
    starting_vertex = graph[y_s][x_s]
    starting_vertex.setCost(0)
    x_e, y_e = end
    end_vertex = graph[y_e][x_e]
    determine_cost(starting_vertex, Vertex_Queue(), end_vertex)
    path = set()
    path.add(starting_vertex)
    current_vertex = graph[y_e][x_e]
    while current_vertex != starting_vertex:
        path.add(current_vertex)
        current_vertex = current_vertex.previous_vertex
    return path
    

def determine_cost(current_vertex, queue, end_vertex, visited=None):
    if visited is None:
        visited = set()
    for neighbour in current_vertex.neighbours:
        new_path_cost = current_vertex.path_cost + neighbour.entry_cost
        if neighbour.path_cost > new_path_cost:
            neighbour.setCost(new_path_cost)
            neighbour.setPVertex(current_vertex)
            if neighbour not in visited:
                queue.add_vertex(neighbour)
    visited.add(current_vertex)
    if current_vertex == end_vertex:
        return
    if not queue.empty():
        next_vertex = queue.pop()
        while next_vertex in visited:
            next_vertex = queue.pop()
        determine_cost(next_vertex, queue, end_vertex, visited)


def visualized_path(array, graph, path):
    path_representation = []
    for y_c, row in enumerate(graph):
        representation_row = []
        for x_c, vertex in enumerate(row):
            if vertex in path:
                representation_row.append(array[y_c][x_c])
            else:
                representation_row.append(" ")
        path_representation.append(representation_row)
    return path_representation


def find_path_in_array(array):
    graph = create_graph(array)
    start, end = find_start_and_end(array)
    path = shortest_path_d(graph, start, end)
    g_path = visualized_path(array, graph, path)
    return g_path

if __name__ == "__main__":
    # array = [[0,2,1],
    #          [2,2,1],
    #          [2,1,0]]
    array = [[1,1,1,1,2,2],
             [1,0,4,1,2,2],
             [9,4,2,1,1,1],
             [9,9,6,4,1,1],
             [9,9,0,4,1,1],
             [9,9,1,1,1,1]]
    path = find_path_in_array(array)
    for row in path:
        print(row)