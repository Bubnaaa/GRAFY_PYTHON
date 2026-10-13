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
        self.connection[B].append(A)

g = Graf()
g.add_connection("A", "B")
print(g.connection)