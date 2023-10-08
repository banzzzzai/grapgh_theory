class GraphColoring:
    def __init__(self, adjacency_matrix):
        self.adjacency_matrix = adjacency_matrix
        self.num_nodes = len(adjacency_matrix)
        self.color_assignment = [-1] * self.num_nodes
        self.num_colors = 0

    def is_safe(self, node, color):
        for neighbor in range(self.num_nodes):
            if self.adjacency_matrix[node][neighbor] == 1 and self.color_assignment[neighbor] == color:
                return False
        return True

    def color_graph(self, node):
        if node == self.num_nodes:
            return True

        for color in range(self.num_colors):
            if self.is_safe(node, color):
                self.color_assignment[node] = color

                if self.color_graph(node + 1):
                    return True

                self.color_assignment[node] = -1

        return False

    def solve(self):
        while not self.color_graph(0):
            self.num_colors += 1

    def get_coloring(self):
        return self.color_assignment

if __name__ == "__main__":

    graph = [
        [0, 1, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 1, 0, 0],
        [1, 0, 0, 1, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0],
    ]

    graph_coloring = GraphColoring(graph)
    graph_coloring.solve()
    color_assignment = graph_coloring.get_coloring()

    print("Раскраска вершин графа:")
    for node, color in enumerate(color_assignment):
        print(f"Вершина {node + 1} - Цвет {color + 1}")
