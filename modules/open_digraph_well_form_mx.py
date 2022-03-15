class open_digraph_well_form_mx:
    '''
        Une fonction qui vérifie que les input listé dans l'attribut inputs correspondent bien à des noeuds existants
        @return un booléen
    '''
    def inputs_graph(self):
        for Ninput in self.inputs:
            if not bool(self.nodes.get(Ninput, 0)):
                return False
        return True

    '''
        Une fonction qui vérifie que les output listé dans l'attribut outputs correspondent bien à des noeuds existants
        @return un booléen
    '''

    def outputs_graph(self):
        for Noutput in self.outputs:
            if not bool(self.nodes.get(Noutput, 0)):
                return False
        return True

    '''
        Une fonction qui verifie pour chaque noeud en input possède bien 0 parent et au moins un enfant.
        @return un boolean
    '''

    def input_1_children(self):
        for Ninput in self.inputs:
            n = self.get_node_by_id(Ninput)
            l = n.get_parents_ids()
            d = n.get_children_ids()
            if len(l) != 0 or len(d) != 1:
                return False
        return True
    '''
        Une fonction qui verifie pour chaque noeud en output possède bien 0 enfant et au moin un parent.
        @return un boolean
    '''

    def output_1_parent(self):
        for Noutput in self.outputs:
            n = self.get_node_by_id(Noutput)
            l = n.get_parents_ids()
            d = n.get_children_ids()
            if len(l) != 1 or len(d) != 0:
                return False
        return True

    '''
        Verifie que la clé permettant d'acceder à chaque noeud correspond bien à son identifiant
        @return un booleen
    '''

    def cle_pointe_noeud(self):
        for key, node in self.nodes.items():
            if key != node.get_id():
                return False
        return True

    '''
        Verifie que que la multiplicité pour chaque arrête est bien cohérente.
        @return un booléen
    '''

    def multiplicite_vice_versa(self):
        for y in self.nodes.values():
            parents = y.get_parents_ids()
            parentnodes = self.get_nodes_by_ids(parents)
            for parent in parentnodes:
                if y.get_id() in parent.get_children_ids():
                    if y.parents[parent.get_id()] != parent.children[y.get_id()]:
                        return False
                else:
                    return False
        return True

    '''
        Vérifie que le graph est cohérent.
        @return un booléen
    '''

    def is_well_formed(self):
        if(self.inputs_graph() and self.outputs_graph() and self.input_1_children() and self.output_1_parent() and self.cle_pointe_noeud() and self.multiplicite_vice_versa()):
            return True
        return False

    def list_equal(self,l1,l2):
        return sorted(l1) == sorted(l2)

    def is_equal_in_and_out(self, graph):
        return self.list_equal(self.inputs,graph.inputs) and self.list_equal(self.outputs,graph.outputs)
    
    def is_same_node(self,n1,n2):
        return n1.id == n2.id and n1.parents == n2.parents and n1.children == n2.children#and n1.label == n2.label

    def is_equal_nodes(self, graph):
        a =   self.list_equal(self.get_node_ids(),graph.get_node_ids())
        b = all([self.is_same_node(self.nodes[n],graph.nodes[n]) for n in self.get_node_ids()])

        return a and b

    def is_equal(self,graph):
        return self.is_equal_in_and_out(graph) and self.is_equal_nodes(graph)