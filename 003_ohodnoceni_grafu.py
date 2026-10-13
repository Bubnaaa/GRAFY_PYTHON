class Graf:
    def __init__(self):
        self.connection = {}

    def add_point(self, point):
        if point not in self.connection:
            self.connection[point] = []

    def add_connection(self, A, B, weight = None):
        self.add_point(A)
        self.add_point(B)

        self.connection[A].append((B, weight))
        if A != B:
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

g1 = Graf()
g1.add_connection("A", "B", 10)
print(g1.connection)
print("Loop:", g1.has_loop())
print("Weights:", g1.has_weights())

g2 = Graf()
g2.add_connection("A", "B")
print(g2.connection)
print("Loop:", g2.has_loop())
print("Weights:", g2.has_weights())