"""
This module imports the AStar class from the a_star module and the Graph and
Node classes from the graph module.
The Astar class is used to execute the A* algorithm and the Graph and Node
classes are used to represent the graph.
The Graph class is used to represent the graph.
"""
from a_star import AStar
from graph import Graph, Node


def graph13():
    """
    This function is the entry point of the program.
    it is responsible for instantiating the necessargity components and
    executing
    the program of graph and nodes and edges.
    """
    # Create graph
    graph = Graph()
    # Add vertices
    graph.add_node(Node("S", (1, 1)))
    graph.add_node(Node("B", (1, 2)))
    graph.add_node(Node("C", (1, 4)))
    graph.add_node(Node("D", (2, 1)))
    graph.add_node(Node("E", (2, 2)))
    graph.add_node(Node("F", (2, 3)))
    graph.add_node(Node("G", (2, 4)))
    graph.add_node(Node("H", (3, 1)))
    graph.add_node(Node("I", (3, 4)))
    graph.add_node(Node("J", (4, 1)))
    graph.add_node(Node("K", (4, 2)))
    graph.add_node(Node("T", (4, 3)))
    graph.add_node(Node("L", (4, 4)))

    # Add edges
    graph.add_edge("S", "B", 4)
    graph.add_edge("S", "D", 5)
    graph.add_edge("B", "E", 1)
    graph.add_edge("C", "G", 1)
    graph.add_edge("D", "E", 2)
    graph.add_edge("D", "H", 3)
    graph.add_edge("E", "F", 6)
    graph.add_edge("F", "G", 4)
    graph.add_edge("G", "I", 3)
    graph.add_edge("H", "J", 1)
    graph.add_edge("I", "L", 4)
    graph.add_edge("J", "K", 6)
    graph.add_edge("K", "T", 2)
    graph.add_edge("T", "L", 3)

    # Execute the algorithm
    alg = AStar(graph, "S", "T")
    path, path_length = alg.search()
    print(" -> ".join(path))
    print(f"Length of the path: {path_length}")


# if __name__ == "__main__":
#     run()

# S -> D -> H -> J -> K -> T
# Length of the path: 17


def simple_test_case_with_solution():
    """
    This function is the entry point of the program.
    it is responsible for instantiating the necessary components and executing
    the program with node and edge with solution.
    """
    # Create a new Graph object
    graph = Graph()

    graph.add_node(Node("S", (1, 1)))
    graph.add_node(Node("A", (1, 2)))
    graph.add_node(Node("B", (1, 3)))
    graph.add_node(Node("C", (2, 3)))
    graph.add_node(Node("D", (3, 3)))
    graph.add_node(Node("E", (3, 2)))
    graph.add_node(Node("T", (3, 1)))

    # Add edges
    graph.add_edge("S", "A", 2)
    graph.add_edge("A", "B", 1)
    graph.add_edge("B", "C", 2)
    graph.add_edge("C", "D", 2)
    graph.add_edge("D", "E", 1)
    graph.add_edge("E", "T", 1)

    # Execute the algorithm
    alg = AStar(graph, "S", "T")
    path, path_length = alg.search()
    print(" -> ".join(path))
    print(f"Length of the path: {path_length}")


def simple_test_case_without_solution():
    """
    This function is the entry point of the program for the simple test case
    without solution node and edge."""
    # Create a new Graph object
    graph = Graph()
    graph.add_node(Node("S", (1, 1)))
    graph.add_node(Node("A", (1, 2)))
    graph.add_node(Node("B", (1, 3)))
    graph.add_node(Node("C", (2, 3)))
    graph.add_node(Node("D", (3, 3)))
    graph.add_node(Node("T", (3, 1)))

    # Add edges
    graph.add_edge("S", "A", 4)
    graph.add_edge("A", "B", 5)
    graph.add_edge("B", "C", 1)
    graph.add_edge("C", "D", 1)

    # Execute the algorithm
    alg = AStar(graph, "S", "T")
    if alg.search() is None:
        print("No path")
    else:
        path, path_length = alg.search()
        if path:
            print(" -> ".join(path))
            print(f"Length of the path: {path_length}")
        else:
            print("No path found")


def main():

    """
    This function is the entry point of the program for the Main function.
    It is responsible for instantiating the necessary components and executing
    the program of graph13(), simple_test_case_with_solution,
    simple_test_case_without_solution.
    """
    print(graph13())
    print(simple_test_case_with_solution())
    print(simple_test_case_without_solution())


if __name__ == "__main__":
    main()
