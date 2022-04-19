from modules.open_digraph import open_digraph
from modules.open_digraph_entity import open_digraph_entity


class bool_circ(open_digraph_entity):
    valid_labels = ["|","&","~","","0","1","^"]
    def __init__(self,g):
        super().__init__(g.inputs, g.outputs, list(g.nodes.values()))
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

    def parse_parenthese(s):
        g = open_digraph_entity.empty()
        g.add_node()
        g.add_output_node(0)
        current_node = 0
        s2 = ''
        for c in s:
            if c == '(':
                n = g.get_node_by_id(current_node)
                n.label += s2
                g.add_node()
                nodes_id = g.get_node_ids()
                tmp = nodes_id[len(nodes_id) - 1]
                g.add_edge(tmp, current_node)
                current_node = tmp
                s2 = ''
            elif c == ')':
                n = g.get_node_by_id(current_node)
                n.label += s2
                current_node = list(n.get_children_ids())[0]
                s2 = ''
            else :
                s2 += c
        return bool_circ(g)

    def get_nodes_with_same_label(g):
        l = []
        res = []
        for n in g.get_nodes():
            if n.label not in bool_circ.valid_labels:
                l.append(n)
        #print(l)
        for n1 in l:
            for n2 in l:
                if n1 != n2:
                    if n1.label == n2.label:
                        if (n2,n1) not in res:
                            res.append((n1,n2))
        return res

    def parse_parenthese_exo3(s):
        g = open_digraph_entity.empty()
        g.add_node()
        g.add_output_node(0)
        current_node = 0
        s2 = ''
        for c in s:
            if c == '(':
                n = g.get_node_by_id(current_node)
                n.label += s2
                g.add_node()
                nodes_id = g.get_node_ids()
                tmp = nodes_id[len(nodes_id) - 1]
                g.add_edge(tmp, current_node)
                current_node = tmp
                s2 = ''
            elif c == ')':
                n = g.get_node_by_id(current_node)
                n.label += s2
                current_node = list(n.get_children_ids())[0]
                s2 = ''
            else :
                s2 += c
        
        #modification de g exo3
        l = []
        res = []
        for n in g.get_nodes():
            if n.label not in bool_circ.valid_labels:
                l.append(n)
        print(l)
        for n1 in l:
            for n2 in l:
                if n1 != n2:
                    if n1.label == n2.label:
                        if (n2,n1) not in res:
                            res.append((n1,n2))
       
        print(res)
        for pair in res:
            g.fusion(pair[0].id,pair[1].id)
        for pair in res:
            g.add_input_node(pair[0].id)
        for n in l:
            if sum([int(pair[0]==n) + int(pair[1]==n) for pair in res]) == 0:
                g.add_input_node(n.id)

        return bool_circ(g)


    def parse_parenthese_exo4(*args):
        graphs = []
        for s in args:
            graphs.append(bool_circ.parse_parenthese_exo3(s))
        g = open_digraph_entity.empty().iparallel(graphs)
        res = bool_circ.get_nodes_with_same_labels(g)
        

        



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
