import sys
import os
root = os.path.normpath(os.path.join(__file__, './../..'))
sys.path.append(root)# allows us to fetch files from the project root
import unittest
from modules.open_digraph_entity import *


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
    id_ = graph.get_node_ids()[0]
    graph.add_input_node(id_)
    assert graph.is_well_formed()
    graph.add_output_node(id_)
    assert graph.is_well_formed()
    graph.add_node(children={id_:1})
    assert graph.is_well_formed()
    graph.remove_node_by_id(graph.get_outputs_ids()[0])
    assert graph.is_well_formed()
    graph.add_output_node(id_)
    graph.add_edge(3,0) 
    assert graph.is_well_formed()
    graph.remove_edge(3, 0)
    assert graph.is_well_formed()
    graph.add_input_node(0)
    assert graph.is_well_formed()
    graph.add_output_node(id_)
    assert graph.is_well_formed()

    id_old = graph.get_node_ids()
    graph.shift_indices(5)
    id_new = graph.get_node_ids()
    #print(id_new, id_old)
    for i in range(len(id_old)):
        assert (id_new[i] == (5 + id_old[i]))

    graph.save_as_dot_file("test.dot")
    g = open_digraph_entity.empty()
    g.from_dot_file("test.dot")
    assert graph.is_equal(g)

    g1 = open_digraph_entity.empty()
    g2 = open_digraph_entity.empty()
    g1.add_node()
    g2.add_node()
    g1.add_input_node(0)
    g2.add_input_node(0)
    g1.add_node()
    g2.add_node()
    g1.add_edge(0, 2)
    g2.add_edge(2, 0)
    assert g1.is_well_formed()
    assert g2.is_well_formed()
    graph.display()
    g1.display()
    g2.display()
    graph.iparallel_l([g1])
    graph.is_well_formed()
    graph.display()
    graph.iparallel_l([g2])
    graph.is_well_formed()
    graph.display()



    







