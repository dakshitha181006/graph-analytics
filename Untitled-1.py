from collections import defaultdict

class DirectedGraph:
    def __init__(self):
        self.adj_list = defaultdict(list)   # adjacency list
        self.vertices = set()

    def add_vertex(self, v):
        self.vertices.add(v)
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, u, v):
        self.vertices.add(u)
        self.vertices.add(v)
        self.adj_list[u].append(v)

    def in_degree(self):
        in_deg = {v: 0 for v in self.vertices}
        for u in self.adj_list:
            for v in self.adj_list[u]:
                in_deg[v] += 1
        return in_deg

    def out_degree(self):
        out_deg = {v: len(self.adj_list[v]) for v in self.vertices}
        return out_deg

    def display_graph(self):
        print("\nAdjacency List:")
        for v in sorted(self.vertices, key=str):
            print(f"  {v} -> {self.adj_list[v]}")

    def display_degrees(self):
        in_deg = self.in_degree()
        out_deg = self.out_degree()

        print("\nVertex\tIn-Degree\tOut-Degree")
        for v in sorted(self.vertices, key=str):
            print(f"{v}\t{in_deg[v]}\t\t{out_deg[v]}")

        max_in = max(in_deg.values())
        max_out = max(out_deg.values())

        max_in_vertices = [v for v in in_deg if in_deg[v] == max_in]
        max_out_vertices = [v for v in out_deg if out_deg[v] == max_out]

        print(f"\nVertex/Vertices with highest In-Degree ({max_in}): {max_in_vertices}")
        print(f"Vertex/Vertices with highest Out-Degree ({max_out}): {max_out_vertices}")


def main():
    g = DirectedGraph()

    # --- Input vertices ---
    n = int(input("Enter number of vertices: "))
    print(f"Enter {n} vertex names/labels (space-separated): ")
    vertex_names = input().split()
    for v in vertex_names:
        g.add_vertex(v)

    # --- Input edges ---
    e = int(input("Enter number of directed edges: "))
    print("Enter each edge as: source destination")
    for _ in range(e):
        u, v = input().split()
        g.add_edge(u, v)

    # --- Output ---
    g.display_graph()
    g.display_degrees()


if __name__ == "__main__":
    main()