import sys
import os
from tabnanny import verbose

from modules.open_digraph_Karnaugh import open_digraph_Karnaugh
root = os.path.normpath(os.path.join(__file__, './../..'))
sys.path.append(root)# allows us to fetch files from the project root
import unittest
from modules.open_digraph_entity import *
from modules.bool_circ import *


class InitTest(unittest.TestCase):
    def test_init_node(self):
        n0 = node(0, 'i', {}, {1:1})
        self.assertEqual(n0.id, 0)
        self.assertEqual(n0.label, 'i')
        self.assertEqual(n0.parents, {})
        self.assertEqual(n0.children, {1:1})
        self.assertIsInstance(n0, node)
        
    def test_init_open_digraph_basic(self):
        graph = open_digraph_entity([0],[0],[node(1,"",[],[2,3]),node(2,"",[1],[4]),node(3,"",[1],[4]),node(4,"",[2,3],[])])
        self.assertIsInstance(graph,open_digraph_entity)
    
class CopyTest(unittest.TestCase):
    def test_copy(self):
        x=open_digraph_entity.empty()
        self.assertIsNot(x.copy(),x)
        
if __name__ == '__main__': # the following code is called only when
    unittest.main() # precisely this file is run

def GraphTest():
    nbfichier = 0
    graph = open_digraph_entity.empty()
    assert graph.is_well_formed()
    graph.add_node()
    assert graph.is_well_formed()
    graph.add_node()
    assert graph.is_well_formed()
    graph.add_edge(0, 1)
    assert graph.is_well_formed()
    graph.add_node()
    assert graph.is_well_formed()
    graph.add_node()
    assert graph.is_well_formed()
    graph.add_edge(0, 2)
    assert graph.is_well_formed()
    graph.add_edge(3, 1)
    assert graph.is_well_formed()
    graph.add_edge(2,1)
    assert graph.is_well_formed()

    #graph.save_as_dot_file('graph.dot')
    #graph.from_dot_file()


    #id_old = graph.get_node_ids()
    #graph.shift_indices(5)
    #id_new = graph.get_node_ids()
    #print(id_new, id_old)
    #for i in range(len(id_old)):
    #    assert (id_new[i] == (5 + id_old[i]))

    graph.save_as_dot_file("test.dot")
    g = open_digraph_entity.empty()
    g.from_dot_file("test.dot")
    assert graph.is_equal(g)

    #graph.display()
    assert ({0: 0, 1: 1, 2: 1, 3: 2}, {1: 0, 2: 0, 3: 1}) == graph.dijkstra(0)
    #print(graph.dijkstra_with_tgt(0,2))
    #print(graph.shortest_path(0,2))
    assert {0: (1, 1)} == graph.common_ancestor_paths(1, 2)
    
    #test tri topologique
    assert [[0, 3], [2], [1]] == graph.tri_topologique()
    
    #test profondeur
    assert 3 == graph.profondeur()
    assert 0 == graph.profondeur_noeud_graphe(0)
    assert 2 == graph.profondeur_noeud_graphe(1)

    #test distance max
    assert ({0: 0, 2: 1, 1: 2}, {2: 0, 1: 2}) == graph.dist_chemin_max(0,1)

   #g1 = open_digraph_entity.empty()
    #g2 = open_digraph_entity.empty()
    #g1.add_node()
    #g2.add_node()
    #g1.add_input_node(0)
    #g2.add_input_node(0)
    #g1.add_node()
    #g2.add_node()
    #g1.add_edge(0, 2)
    #g2.add_edge(2, 0)
    #assert g1.is_well_formed()
    #assert g2.is_well_formed()
    #graph.display()
    #g1.display()
    #g2.display()
    #graph.iparallel_l([g1])
    #graph.is_well_formed()
    #graph.display()
    #graph.iparallel_l([g2])
    #graph.is_well_formed()
    #graph.display()

    #bool_circ
    #bc = bool_circ.parse_parenthese_exo3("((x0)&((x1)&(x2)))|((x1)&(~(x2)))")
    #bc.display(verbose=True)

    bc = bool_circ.parse_parenthese_exo5("((x0)&((x1)&(x2)))|((x1)&(~(x2)))", "((x0)&(~(x1)))|(x2)")
    #bc.display(verbose=True)

    kar = open_digraph_Karnaugh.karnaugh('1111')
    assert kar.is_well_formed()
    #kar.display(verbose=True)
    
    #bool_circ.generate_random_bool_circ_exo2(22,input=6, output=6).display(verbose=True)
    #bool_circ.adder(0).display(verbose=True)
    #bool_circ.adder(1).display(verbose=True)
    #bool_circ.adder(2).display(verbose=True)
    #bool_circ.adder(2).is_well_formed()
    #bool_circ.graphe_a_partir_dun_registre(11, n=16).display(verbose=True)
    """
    g1 = open_digraph_entity.empty()
    g1.add_node(label='^')
    for i in range(6):
        g1.add_node(label='0')
        g1.add_edge(i + 1, 0)
    
    g1.add_node(label='1')
    g1.add_edge(list(g1.nodes.keys())[-1], 0)
    boolc = bool_circ(g1)
    boolc.display(verbose=True)
    boolc.tr_porte_OU_exclusif(0)
    boolc.display(verbose=True)
    """
    
    bc = bool_circ.generate_random_bool_circ_exo2(10, 1, 3)
    bc.display(verbose=True)
    for i in range(50):
        for id in list(bc.nodes.keys()):
            bc.tr_copies(id)
            bc.tr_element_neutre(id)
            bc.tr_porte_ET(id)
            bc.tr_porte_NON(id)
            bc.tr_porte_OU(id)
            bc.tr_porte_OU_exclusif(id)
    bc.display(verbose=True)
    print(len(bc.nodes))
    
<<<<<<< HEAD
 






=======
>>>>>>> 6a65053e5da58c30ff980d84fd658aa2665d57f4
