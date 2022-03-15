from modules.open_digraph_basic import open_digraph_basic


class bool_circ(open_digraph_basic):
    valid_labels = ["|","&","~","","0","1","^"]
    def __init__(self,g):
        super().__init__()
        self = g.copy()
        if not self.is_well_formed():
            raise Exception("Boolean circuit is not well formed.")

    def test_node_labels(self):
        for n in self.nodes.values:
            if n.label not in bool_circ.valid_labels:
                return False
        return True

    def test_copy_nodes_valid(self):
        for n in self.nodes.values:
            if n.label == "":
                if n.indegree() != 1:
                    return False
        return True

    def test_AND_nodes_valid(self):
        for n in self.nodes.values:
            if n.label == "&":
                if n.outdegree() != 1:
                    return False
        return True

    def test_OR_nodes_valid(self):
        for n in self.nodes.values:
            if n.label == "|":
                if n.outdegree() != 1:
                    return False
        return True

    def test_NOT_nodes_valid(self):
        for n in self.nodes.values:
            if n.label == "~":
                if n.outdegree() != 1 or n.indegree()!=1:
                    return False
        return True

    def is_well_formed(self):
        return (not is_cyclic(self)) and self.test_node_labels() and self.test_copy_nodes_valid() and self.test_AND_nodes_valid() and self.test_OR_nodes_valid() and self.test_NOT_nodes_valid()


def is_cyclic_aux(graph):
    if graph.nodes == {}:
        return False 
    n =  graph.find_leaf() 
    if n == None:            
        return True
    graph.remove_node_by_id(n)
    return is_cyclic_aux(graph)

def is_cyclic(graph):
    graph = graph.copy()
    return is_cyclic_aux(graph)
