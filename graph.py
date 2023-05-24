class Graph:

    def __init__(self):
        self.matrix_ady: list[list] = []
        self.nodo: dict = {}

    def create_a_new_graph(self, number):
        pass

    def show_an_existing_graph(self):
        pass

    def add_a_new_node(self, matrix):
        print("Enter the number of nodes to add")
        n = int(input())
        temp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                temp[i][j] = matrix[i][j]

        matrix = [[0 for _ in range(n + len(matrix))] for _ in range(n + len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i < len(temp) and j < len(temp):
                    matrix[i][j] = temp[i][j]
                else:
                    matrix[i][j] = 0

        showOptions()

    def find_a_path_a_between_two_nodes(self):
        pass


def showOptions():
    graph = Graph()
    options = """
              "1. Create a new graph" \
              "2. Show an existing graph" \
              "3. Add a new node" \
              "4. Find a path a between two nodes"""
    print(options)
    option = int(input("enter option"))
    if option == 1:
        number = int(input("enter the number of nodes"))
        graph.create_a_new_graph(number)
    elif option == 2:
        graph.show_an_existing_graph()
    elif option == 3:
        graph.add_a_new_node(graph.matrix_ady)
    elif option == 4:
        graph.find_a_path_a_between_two_nodes()
    else:
        print("enter a correct option")
        showOptions()



