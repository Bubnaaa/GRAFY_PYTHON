class Graf:
    def __init__(self):
        self.connection = {}

    def add_point(self, point):
        if point not in self.connection:
            self.connection[point] = []

    def add_connection(self, A, B):
        self.add_point(A)
        self.add_point(B)

        self.connection[A].append(B)
        if A != B:
            self.connection[B].append(A)

    def has_loop(self):
        for point, direction in self.connection.items():
            if point in direction:
                return True
        return False

g = Graf()
g.add_connection("A", "B")
g.add_connection("B", "B")
print(g.connection)
print("Loop:", g.has_loop())