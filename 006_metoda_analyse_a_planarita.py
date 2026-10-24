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

g1 = Graf()
g_both_ways = Graf(directed=False)

g_both_ways.add_connection("A", "B", 10)
g1.add_connection("A", "B", 10)
g1.add_connection("A", "C", 5)

print(g1.connection)
print("Loop:", g1.has_loop())
print("Weights:", g1.has_weights())
print("Direction:", g_both_ways.connection)
print("Connected:", g1.is_connected())

g2 = Graf()
g_one_way = Graf(directed=True)

g_one_way.add_connection("A", "B")
g2.add_connection("A", "B")
g2.add_point("C")

print(g2.connection)
print("Loop:", g2.has_loop())
print("Weights:", g2.has_weights())
print("Direction:", g_one_way.connection)
print("Connected:", g2.is_connected())
