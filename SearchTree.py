from Node import Node
from SearchAlgorithms import a_star_search

class SearchTree:
    def __init__(self):
        self.nodes = []

    def add_node(self, new_node):
        self.nodes.append(new_node)

    def new_node(self, id, x, y, accessible):
        new_node = Node()
        new_node.id = id
        new_node.x = x
        new_node.y = y
        new_node.accessible = accessible
        self.add_node(new_node)

        return new_node

    def get_path(self, start_node, target_node):
        path = []

        path = a_star_search(start_node, target_node, self.nodes)

        return path

