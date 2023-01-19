from calculations import get_distance

def a_star_search(start_node, target_node, search_tree):
    path = []
    closed = 0

    closed_list = []
    for node in search_tree:
        if node.id == start_node:
            closed_list.append(node)
            closed = closed + 1
            search_tree.remove(node)


    path_node = None
    target_found = False
    while not target_found:
        for node in search_tree:
            prev = -1
            for closed_node in closed_list:
                if node is closed_node:
                    continue
                if node in closed_node.child_nodes:
                    if node.id is target_node:
                        path_node = node
                        target_found = True
                        break
                    if get_distance(closed_node.x, closed_node.y, node.x, node.y) < prev or prev is -1:
                        prev = get_distance(closed_node.x, closed_node.y, node.x, node.y)
                        path_node = node

        closed_list.append(path_node)

    for item in closed_list:
        print (item.id)

    path = closed_list
    return path