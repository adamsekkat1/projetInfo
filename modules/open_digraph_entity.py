from modules.node import node
from modules.open_digraph_basic import open_digraph_basic
from modules.open_digraph_compositions_mx import open_digraph_compositions_mx
from modules.open_digraph_graphviz import open_digraph_graphviz
from modules.open_digraph_manipulations_mx import open_digraph_manipulations_mx
from modules.open_digraph_matrix_mx import open_digraph_matrix_mx
from modules.open_digraph_well_form_mx import open_digraph_well_form_mx


class open_digraph_entity(open_digraph_basic, open_digraph_compositions_mx, open_digraph_manipulations_mx, open_digraph_matrix_mx, open_digraph_well_form_mx, open_digraph_graphviz):
    def __init__(self, inputs, outputs, nodes):
        '''
        inputs: int list; the ids of the input nodes
        outputs: int list; the ids of the output nodes
        nodes: node iter;
        '''
        self.inputs = inputs
        self.outputs = outputs
        # self.nodes: <int,node> dict
        self.nodes = {node.id: node for node in nodes}