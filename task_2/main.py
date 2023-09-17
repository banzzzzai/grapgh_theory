class BronKerbosch:
    def __init__(self, graph_matrix):
        self.m = graph_matrix
        self.results = []

    def check(self, q_plus, q_minus):
        for i in q_minus:
            q = True
            for j in q_plus:
                if self.m[i][j]:
                    q = False
                    break
            if q:
                return False
        return True

    def extend(self, current_set, q_plus, q_minus):
        while q_plus and self.check(q_plus, q_minus):
            v = q_plus[0]
            current_set.append(v)

            new_q_plus = [i for i in q_plus if not self.m[i][v] and i != v]
            new_q_minus = [i for i in q_minus if not self.m[i][v] and i != v]

            if not new_q_plus and not new_q_minus:
                self.results.append(list(current_set))
            else:
                self.extend(current_set, new_q_plus, new_q_minus)

            q_plus.remove(v)
            current_set.remove(v)
            q_minus.append(v)

    def search(self):

        self.extend([], list(range(len(self.m))), [])

        return self.results


if __name__ == "__main__":

    graph_matrix = [
        [0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 1, 0, 0],
        [0, 1, 0, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 1, 0, 0],
        [1, 1, 0, 0, 1, 0, 1, 1],
        [0, 0, 0, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0]
    ]

    bk = BronKerbosch(graph_matrix)
    max_sets = bk.search()

    print("Максимальные независимые множества:")
    for max_set in max_sets:
        print(max_set)

    print(f"Число независимости графа: {len(max(max_sets, key=len))}")