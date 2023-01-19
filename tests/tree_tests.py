import unittest
from SearchTree import SearchTree
from Node import Node

class MyTestCase(unittest.TestCase):
    def test_node(self):
        search_tree = SearchTree()
        node1 = search_tree.new_node("Node 1", 50, 0, True)
        node2 = search_tree.new_node("Node 2", 10, 30, True)
        node3 = search_tree.new_node("Node 3", 70, 30, True)

        node1.add_child(node2)
        node1.add_child(node3)

        self.assertEqual(node1.id, 'Node 1')
        self.assertEqual(node1.child_nodes[0].id, 'Node 2')
        self.assertEqual(node1.child_nodes[1].id, 'Node 3')

    def test_something(self):
        search_tree = SearchTree()
        # create_node(Node Name (String), X co-oridinate (Integer), Y co-oridinate (Integer), Accessible (Bool))
        node1 = search_tree.new_node("Node 1", 50, 0, True)
        node2 = search_tree.new_node("Node 2", 10, 30, True)
        node3 = search_tree.new_node("Node 3", 70, 30, True)
        node4 = search_tree.new_node("Node 4", 40, 200, True)
        node5 = search_tree.new_node("Node 5", 200, 160, True)
        node6 = search_tree.new_node("Node 6", 300, 430, True)
        node7 = search_tree.new_node("Node 7", 400, 490, True)

        node1.add_child(node2)
        node1.add_child(node3)
        node2.add_child(node1)
        node2.add_child(node4)
        node3.add_child(node4)
        node3.add_child(node5)
        node4.add_child(node2)
        node4.add_child(node6)
        node5.add_child(node3)
        node5.add_child(node6)
        node6.add_child(node7)
        node6.add_child(node5)
        node7.add_child(node6)
        node7.add_child(node3)

        # prints tree
        for node in search_tree.nodes:
            node_text = node.id
            node_text += " Child Nodes = "
            for child in node.child_nodes:
                node_text += child.id + " "
            print(node_text)

        print("")
        print("Path")
        path = search_tree.get_path("Node 1", "Node 7")
        node_text = ""
        for node in path:
            node_text += node.id + " "
        print(node_text)
        self.assertEqual("Node 1 Node 3 Node 5 Node 6 Node 7 ", node_text)


if __name__ == '__main__':
    unittest.main()
