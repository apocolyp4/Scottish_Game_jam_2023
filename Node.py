
class Node:
    def __init__(self):
        self.id = -1
        self.accessible = True
        self.x = 0
        self.y = 0
        self.child_nodes = []

    def add_child(self, new_node):
        self.child_nodes.append(new_node)