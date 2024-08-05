INF = float("infinity")

# Define graph as dictionary representing adjacency list.
graph = {
    "U": {"V": 6, "W": 7},
    "V": {"U": 6, "X": 10},
    "W": {"U": 7, "X": 1},
    "X": {"W": 1, "V": 10}
}
# [('U', 0), ('V', 6), ('W', 7), ('X', 8)]


# graph = {
#     "A": {"B": 6, "D": 1},
#     "B": {"A": 6, "C": 5, "D": 2, "E": 2},
#     "C": {"B": 5, "E": 5},
#     "D": {"A": 1, "B": 2, "E": 1},
#     "E": {"B": 2, "C": 5, "D": 1}
# }
# [('A', 0), ('B', 3), ('C', 7), ('D', 1), ('E', 2)]


unvisited_min_distances = {vertex: INF for vertex in graph}
visited_vertices = {}
current_vertex = "U"  # The start node.
unvisited_min_distances[current_vertex] = 0

print(unvisited_min_distances)