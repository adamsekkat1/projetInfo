

class open_digraph_basic:  # for open directed graph
    
    """def __init__(self, inputs, outputs, nodes):
        '''
        inputs: int list; the ids of the input nodes
        outputs: int list; the ids of the output nodes
        nodes: node iter;
        '''
        self.inputs = inputs
        self.outputs = outputs
        # self.nodes: <int,node> dict
        self.nodes = {node.id: node for node in nodes}"""

    '''
        Un getter qui renvoie la liste des indentifiants des noeuds en inputs.
        @return une list de int
    '''

    def get_inputs_ids(self):
        return self.inputs

    '''
        Un getter qui renvoie la liste des indentifiants des noeuds en outputs.
        @return une list de int
    '''

    def get_outputs_ids(self):
        return self.outputs

    '''
        Un getter qui renvoie l'attribut nodes, un dictionnaire contennant les noeuds, accessible via leur identifiant.
        @return un dictionnaire
    '''

    def get_id_node_map(self):
        return self.nodes

    '''
        Un getter qui renvoie la liste des noeuds.
        @return un list de node
    '''

    def get_nodes(self):
        # Je propose qu'on mette juste return self.nodes.values(), cette fonction renvoyant deja une list
        return [node for node in self.nodes.values()]
    '''
        Un getter qui renvoie la liste des noeuds.
        @return un list de node
    '''

    def get_node_ids(self):
        # return self.nodes.keys() suffirait également à mon avis
        return list(self.nodes.keys())

    '''
        Un getter qui renvoie un noeud, identifié par son id passé en paramètre.
        @param id, un int
        @return un node
    '''

    def get_node_by_id(self, id_):
        # il manque le second paramètre j'ai l'impression, vaudrait mieux à mon avis juste mettre return self.nodes[id], pour que l'erreur soit soulevé si jamais l'id n'est pas reconnu
        return self.nodes.get(id_)

    '''
        Un getter qui renvoie une liste des noeuds identifié par les id passé en paramètre.
        @param ids, une list de int
        @return une list de node
    '''

    def get_nodes_by_ids(self, ids):
        return [self.get_node_by_id(id_) for id_ in ids]

    '''
        Un setter qui affecte à l'attribut inputs la valeur passé en paramètre.
        @param x un int list
    '''

    def set_input_ids(self, x):
        self.inputs = x

    '''
        Un setter qui affecte à l'attribut outputs la valeur passé en paramètre.
        @param x un int list
    '''

    def set_outputs_ids(self, x):
        self.outputs = x

    '''
        Ajoute un l'identifiant passé en paramètre à la liste des inputs.
        @param newinput, un int
    '''

    def add_input_id(self, newinput):
        # self.inputs = x
        if newinput not in self.inputs:
            self.inputs.append(newinput)

    '''
        Ajoute un l'identifiant passé en paramètre à la liste des outputs.
        @param newoutput, un int
    '''

    def add_output_id(self, newoutput):
        # self.outputs = x
        if newoutput not in self.outputs:
            self.outputs.append(newoutput)

    '''
    Renvoit l'ensemble des informations sur les noeuds, plus la liste des inputs et des outputs
    '''
    def __str__(self):
        return "\n".join([str(n) for n in self.nodes.values()])+"\n\rinputs:"+str(self.inputs)+"\n\routputs:"+str(self.outputs)

        # return "input:"+",".join([str(i) for i in self.inputs])+"\noutput:"+",".join([str(i) for i in self.outputs])
    def __repr__(self):
        return str(self)
        #return "input:"+",".join([repr(i) for i in self.inputs])+"\noutput:"+",".join([repr(i) for i in self.outputs])

    @classmethod
    def empty(cls):
        return cls([], [], [])

    '''
        Une fonction qui renvoie une copie du graph.
        @return un open_digraph
    '''

    def copy(self):
        return self.__class__(self.inputs.copy(), self.outputs.copy(), self.nodes.copy())