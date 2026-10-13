class Graf:
    def __init__(self, directed = False):
        self.connection = {}
        self.directed = directed

    def add_point(self, point):
        if point not in self.connection:
            self.connection[point] = []

    def add_connection(self, A, B, weight = None):
        self.add_point(A)
        self.add_point(B)

        self.connection[A].append((B, weight))
        if not self.directed and A != B:
            self.connection[B].append((A, weight))

    def has_loop(self):
        for point, targets in self.connection.items():
            for target, _ in targets:
                if point == target:
                    return True
        return False

    def has_weights(self):
        for points_directory in self.connection.values():
            for finish, weight in points_directory:
                if weight is not None:
                    return True
        return False

    def is_directed(self):
        return self.directed

    def is_connected(self):
        if len(self.connection) <= 1:
            return True

        all_points = list(self.connection.keys())
        start = all_points[0]

        done = set()
        will_be_done = [start]

        while will_be_done:
            actual = will_be_done.pop()
            if actual not in done:
                done.add(actual)

                for neighbour, _ in self.connection[actual]:
                    will_be_done.append(neighbour)

        return len(done) == len(all_points)

g1 = Graf(directed=True)
g1.add_connection("A", "B")
g1.add_connection("B", "C")

print("\n ----PŘEHLED GRAFU 1----")
print("Smyčka:", g1.has_loop())
print("Ohodnocení:", g1.has_weights())
print("Orientace:", g1.is_directed())
print("Souvislost", g1.is_connected())
print("\n------------------")
print("Vizualizace:", g1.connection)


g2 = Graf(directed=False)
g2.add_connection("A", "B", 10)
g2.add_point("C")

print("\n ----PŘEHLED GRAFU 2----")
print("Smyčka:", g2.has_loop())
print("Ohodnocení:", g2.has_weights())
print("Orientace:", g2.is_directed())
print("Souvislost", g2.is_connected())
print("\n------------------")
print("Vizualizace:", g2.connection)
