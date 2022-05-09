from ast import operator
from cProfile import label
from modules.open_digraph import open_digraph
from modules.open_digraph_entity import open_digraph_entity
import copy
from modules.open_digraph_matrix_mx import *

class bool_circ(open_digraph_entity):
    valid_labels = ["|","&","~","","0","1","^"]
    operator_labels = ["|","&","^"]
    def __init__(self,g):
        super().__init__(g.inputs, g.outputs, list(g.nodes.values()))
        self = g.copy()
        self.variables = {}
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
        #print(l)
        for n1 in l:
            for n2 in l:
                if n1 != n2:
                    if n1.label == n2.label:
                        if (n2,n1) not in res:
                            res.append((n1,n2))
       
        #print(res)
        for pair in res:
            g.fusion(pair[0].id,pair[1].id)
        for pair in res:
            g.add_input_node(pair[0].id)
        for n in l:
            if sum([int(pair[0]==n) + int(pair[1]==n) for pair in res]) == 0:
                g.add_input_node(n.id)

        return bool_circ(g)


    def get_variables(g):
        return {n.label:n.id for n in g.get_nodes_by_ids(g.nodes) if n.label not in bool_circ.valid_labels}

    def remove_variable_labels(g):
        for n in g.get_nodes_by_ids(g.nodes):
            if n.label in list(g.variables.keys()):
                n.label = ""
        return g

    def parse_parenthese_exo4(*args):
        graphs = []
        for s in args:
            g = bool_circ.parse_parenthese_exo3(s)
            #g.display(verbose=True)
            graphs.append(g)
        g = open_digraph_entity.empty().parallel_l(graphs)
        #g.display(verbose=True)
        res = bool_circ.get_nodes_with_same_label(g)
        res = [[p[0].id,p[1].id] for p in res]
        l = copy.copy(res)
        for i in range(len(res)):
            id1 = res[i][0]
            id2 = res[i][1]
            for j in range(i+1,len(res)):
                if res[j][0] == id2:
                    l.pop(j)
        res = l 
        #print(res)
        for pair in res:
            g.fusion(pair[0],pair[1])
        for pair in res:
            g.remove_node_by_id(list(g.get_node_by_id(pair[0]).parents.keys())[0])

        return bool_circ(g)

        
    def parse_parenthese_exo5(*args):
        graphs = []
        for s in args:
            g = bool_circ.parse_parenthese_exo3(s)
            #g.display(verbose=True)
            graphs.append(g)
        g = open_digraph_entity.empty().parallel_l(graphs)
        #g.display(verbose=True)
        res = bool_circ.get_nodes_with_same_label(g)
        res = [[p[0].id,p[1].id] for p in res]
        l = copy.copy(res)
        for i in range(len(res)):
            id1 = res[i][0]
            id2 = res[i][1]
            for j in range(i+1,len(res)):
                if res[j][0] == id2:
                    l.pop(j)
        res = l 
        #print(res)
        for pair in res:
            g.fusion(pair[0],pair[1])
        for pair in res:
            g.remove_node_by_id(list(g.get_node_by_id(pair[0]).parents.keys())[0])

        g.variables = bool_circ.get_variables(g)
        g = bool_circ.remove_variable_labels(g)
        #print(g.variables)
        return bool_circ(g)

    def generate_random_bool_circ(n):
        g = open_digraph_entity.random_matrix(n, 1, form='DAG')
        n_sans_parent = []
        n_sans_enfant = []
        n_to_remove = []
        for n in g.nodes.values():
            if (len(n.parents.keys()) == 0):
                n_sans_parent.append(n.id)
            if (len(n.children.keys()) == 0):
                n_sans_enfant.append(n.id)
            if(len(n.parents.keys()) == len(n.children.keys()) and len(n.parents.keys()) == 1):
                n.label = '~'
            elif(len(n.parents.keys()) > 1 and len(n.children.keys()) == 1):
                n.label = random.choice(bool_circ.operator_labels)
            elif(len(n.parents.keys()) > 1 and len(n.children.keys()) > 1):
                n_to_remove.append(n.id)
                
        for i in n_to_remove:
            g.add_node()
            for j in g.nodes[i].parents.keys():
                g.add_edge(j, list(g.nodes.values())[-1].id)
            list(g.nodes.values())[-1].label = random.choice(bool_circ.operator_labels)
            g.add_node()
            for j in g.nodes[i].children.keys():
                g.add_edge(list(g.nodes.values())[-1].id, j)
            g.add_edge(list(g.nodes.values())[-2].id, list(g.nodes.values())[-1].id)
            g.remove_node_by_id(i)
        for i in n_sans_parent:
            g.add_input_node(i)
            list(g.nodes.values())[-1].label = 'in'
        for i in n_sans_enfant:
            g.add_output_node(i)
            list(g.nodes.values())[-1].label = 'out'
        return g

    def generate_random_bool_circ_exo2(n, input=1, output=1):
        g = open_digraph_entity.random_matrix(n, 1, form='DAG')
        n_sans_parent = []
        n_sans_enfant = []
        n_to_remove = []
        for n in g.nodes.values():
            if (len(n.parents.keys()) == 0):
                n_sans_parent.append(n.id)
            if (len(n.children.keys()) == 0):
                n_sans_enfant.append(n.id)
            if(len(n.parents.keys()) == len(n.children.keys()) and len(n.parents.keys()) == 1):
                n.label = '~'
            elif(len(n.parents.keys()) > 1 and len(n.children.keys()) == 1):
                n.label = random.choice(bool_circ.operator_labels)
            elif(len(n.parents.keys()) > 1 and len(n.children.keys()) > 1):
                n_to_remove.append(n.id)
                
        for i in n_to_remove:
            g.add_node()
            for j in g.nodes[i].parents.keys():
                g.add_edge(j, list(g.nodes.values())[-1].id)
            list(g.nodes.values())[-1].label = random.choice(bool_circ.operator_labels)
            g.add_node()
            for j in g.nodes[i].children.keys():
                g.add_edge(list(g.nodes.values())[-1].id, j)
            g.add_edge(list(g.nodes.values())[-2].id, list(g.nodes.values())[-1].id)
            g.remove_node_by_id(i)
        for i in n_sans_parent:
            g.add_input_node(i)
            list(g.nodes.values())[-1].label = 'in'
        diff_inputs = len(n_sans_parent) - input
        #print("diff:"+str(diff_inputs))
        if(diff_inputs > 0):
            l = g.inputs[:diff_inputs+1]
            id1 = l[0]
            l = l[1:]
            g.fusion_liste([(id1,idn) for idn in l])

        if (diff_inputs < 0):
            for i in range(-diff_inputs):
                rid = random.choice(n_sans_parent)
                g.add_input_node(rid)
                list(g.nodes.values())[-1].label = 'in'
            for i in n_sans_parent:
                g.add_node()
                for j in g.nodes[i].parents.keys():
                    g.add_edge(j, list(g.nodes.values())[-1].id)
                list(g.nodes.values())[-1].label = random.choice(bool_circ.operator_labels)
                g.add_node()
                for j in g.nodes[i].children.keys():
                    g.add_edge(list(g.nodes.values())[-1].id, j)
                g.add_edge(list(g.nodes.values())[-2].id, list(g.nodes.values())[-1].id)
                g.remove_node_by_id(i)

        for i in n_sans_enfant:
            g.add_output_node(i)
            list(g.nodes.values())[-1].label = 'out'

        diff_outputs = len(n_sans_enfant) - output
        #print("diff:"+str(diff_outputs))
        if(diff_outputs > 0):
            l = g.outputs[:diff_outputs+1]
            id1 = l[0]
            l = l[1:]
            g.fusion_liste([(id1,idn) for idn in l])

        if (diff_outputs < 0):
            for i in range(-diff_outputs):
                rid = random.choice(n_sans_enfant)
                g.add_output_node(rid)
                list(g.nodes.values())[-1].label = 'out'
            for i in n_sans_enfant:
                g.add_node()
                for j in g.nodes[i].parents.keys():
                    g.add_edge(j, list(g.nodes.values())[-1].id)
                list(g.nodes.values())[-1].label = random.choice(bool_circ.operator_labels)
                g.add_node()
                for j in g.nodes[i].children.keys():
                    g.add_edge(list(g.nodes.values())[-1].id, j)
                g.add_edge(list(g.nodes.values())[-2].id, list(g.nodes.values())[-1].id)
                g.remove_node_by_id(i)
        return g

    '''
    n : int
    a, b, c : str 
    '''
    @classmethod
    def adder(self,n):
        #assert 2**n == len(a) == len(b)
        if n == 0:
            g = open_digraph_entity.empty()
            g.add_node()
            g.add_node()
            g.add_node()
            #g.add_input_node(0)
            #g.add_input_node(1)
            #g.add_input_node(2)

            g.add_node()
            g.add_edge(0,3)
            g.add_edge(1,3)
            g.get_node_by_id(3).label = "^"

            g.add_node()
            g.add_edge(0,4)
            g.add_edge(1,4)
            g.get_node_by_id(4).label = "&"

            g.add_node()
            g.add_edge(3,5)

            g.add_node()
            g.get_node_by_id(6).label = "^"
            g.add_edge(5,6)
            g.add_edge(2,6)

            g.add_node()
            g.get_node_by_id(7).label = "&"
            g.add_edge(5,7)
            g.add_edge(2,7)

            g.add_node()
            g.get_node_by_id(8).label = "|"
            g.add_edge(7,8)
            g.add_edge(4,8)

            g.add_input_node(0)
            g.add_input_node(1)
            g.add_input_node(2)

            g.add_output_node(6)
            g.add_output_node(8)

            return g 


        g1 = bool_circ.adder(n-1)
        g2 = bool_circ.adder(n-1)
        #print(g1.max_id())
        #print(g2.max_id())
        g1.iparallel_l([g2])
        #if n==1:
        g1.fusion(g2.max_id(),g1.max_id() - g2.max_id() + 2 * (n + 1), label=1)#g1.max_id()-2-n*g2.max_id())

        return g1   



    def half_adder(self,n,a,b):
        return self.adder(n,a,b,0) 

    @classmethod
    def graphe_a_partir_dun_registre(self, entier, n=8):
        formule_bin = bin(entier)[2:]
        g = open_digraph_entity.empty()
        zero_padding = n-len(formule_bin)
        while zero_padding>0:
            zero_padding -= 1
            g.add_node()
            g.get_node_by_id(g.get_node_ids()[-1]).label = "0" 
        for i in range(len(formule_bin)):
            g.add_node()
            g.get_node_by_id(g.get_node_ids()[-1]).label = formule_bin[i]

        #g.inputs = g.get_node_ids()  je sais pas si il faut faire ça ou pas ? 
        return g

    def tr_copies(self, id1, id2):
        n1 = self.get_node_by_id(id1)
        n2 = self.get_node_by_id(id2)
        for i in list(n2.get_children_ids()):
            self.add_node(label=n1.get_label(), parents=n1.parents, children={i : n2.children[i]})
        self.remove_node_by_id(id1)
        self.remove_node_by_id(id2)

    def tr_porte_NON(self, id1, id2):
        if(self.get_node_by_id(id2).label == '~'):
            self.fusion(id1, id2)
            n = self.get_node_by_id(id1)
            if (n.label == '0'):
                n.set_label('1')
            else :
                n.set_label('0')

    def tr_porte_ET(self, id):
        n = self.get_node_by_id(id)
        l = []
        if(n.label == '&'):
            for i in n.get_parents_ids():
                n1 = self.get_node_by_id(i)
                if n1.label == '0':
                    n.set_label('0')
                    l = list(n.get_parents_ids())
                    for par in l:
                        self.remove_parallel_edge(id, par)
                    self.remove_node_by_id(i)
                    return
                elif n1.label == '1':
                    l += [i]
            for n2 in l:
                self.remove_node_by_id(n2)

    def tr_porte_OU(self, id):
        n = self.get_node_by_id(id)
        l = []
        if(n.label == '|'):
            for i in n.get_parents_ids():
                n1 = self.get_node_by_id(i)
                if n1.label == '1':
                    n.set_label('1')
                    l = list(n.get_parents_ids())
                    for par in l:
                        self.remove_parallel_edge(id, par)
                    self.remove_node_by_id(i)
                    return
                elif n1.label == '0':
                    l += [i]
            for j in l:
                self.remove_node_by_id(j)

    def tr_porte_OU_exclusif(self, id):
        n = self.get_node_by_id(id)
        l = []
        compt1 = 0
        if(n.label == '^'):
            for i in n.get_parents_ids():
                n1 = self.get_node_by_id(i)
                if n1.label == '1':
                    l += [i]
                    compt1 += 1
                elif n1.label == '0':
                    l += [i]
            for n2 in l:
                self.remove_node_by_id(n2)
            if(compt1 % 2 == 1):
                self.add_node(label='~')
                tmp = self.get_node_by_id(list(self.nodes.keys())[-1])
                tmp.children = n.children
                l2 = list(n.get_children_ids())
                for child in l2:
                    self.remove_parallel_edge(id, child)
                self.add_edge(id, list(self.nodes.keys())[-1])


    




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

