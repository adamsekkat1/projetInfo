from modules.node import node


class open_digraph_manipulations_mx:
    '''
        Une fonction qui renvoie un identifiant non utilisé.
        @return un int
    '''

    def new_id(self):
        a = self.get_node_ids()
        z = 0
        while True:
            if z not in a:
                return z
            z += 1

    '''
        Une fonction qui rajoute un lien parent-enfant entre deux noeud d'id passé en paramètre
        @param scr et tgt, des int
    '''

    def add_edge(self, src, tgt):
        if self.nodes[src]  in self.inputs and sum([v for k,v in self.nodes[src].children.items()])>=1:
            print(f"Vous essayez de connecter un noeud[{tgt}] a un input[{src}] qui a deja un enfant")
            return None
            
        else:
            self.nodes[src].add_child_id(tgt)
        if self.nodes[tgt] in self.outputs and sum([v for k,v in self.nodes[tgt].parents])>=1:
            print("Vous essayez de connecter un  noeud[{src}] output[{tgt}] qui a deja un parent")
        else:
            self.nodes[tgt].add_parent_id(src)

    '''
        Une fonction qui rajoute un noeud au graph.
        @param optionnels, label un string, parents et children des list de int
    '''

    def add_node(self, label='', parents=None, children=None):
        if parents == None : 
            parents = {}
        if children == None : 
            children = {}
        id_ = self.new_id()
        n = node(id_, label, parents, children)
        
        '''
            Si un noeud n'a pas de parents, d'enfants on considère automatiquement que c'est un noeud d'input, d'output respectivement
            En théorie on peut avoir un noeud qui n'a pas de parents qui n'est pas un input mais en pratique ça n'a pas beaucoup de sens (et au pire on enlèvera ce bout de code)
            Si on enlève ce code, il ne faudra pas oublier de changer le code des fonctions add_input_node et add_output_node car elles en ont besoin
        '''
        #if children == []:
         #   self.add_output_id(id_)
        #if parents == []:
         #   self.add_input_id(id_)

        for p in parents.keys():
            self.nodes[p].add_child_id(id_)
        for c in children.keys():
            self.nodes[c].add_parent_id(id_)
        self.nodes[id_] = n

    '''
        Une fonction qui permet de créer un noeud en input, qui pointera vers le noeud identifié par l'id passé en paramètre.
        @param _id un int
        @return l
    '''

    def add_input_node(self, _id):
        if _id in self.get_outputs_ids():
            raise Exception(
                "Un noeud output ne peut pas avoir plus d'un parent!")
        self.add_node(children={_id:1})
        self.inputs.append(self.get_node_ids()[-1])

    '''
        Une fonction qui permet de créer un noeud en output, sur lequel pointera le noeud identifié par l'id passé en paramètre.
        @param _id un int
        @return l
    '''

    def add_output_node(self, _id):
        if _id in self.get_inputs_ids():
            raise Exception("Un noeud input ne peut pas avoir plus d'un enfant!")
        self.add_node(parents={_id:1})
        self.outputs.append(self.get_node_ids()[-1])

    '''
        Une méthode qui retire une occurence entre le parent et l'enfant passé en paramètre.
        @src, tgt deux int
    '''

    def remove_edge(self, src, tgt):
        self.get_node_by_id(src).remove_child_once(tgt)
        self.get_node_by_id(tgt).remove_parent_once(src)

    '''
        Une méthode qui retire toute occurence entre le parent et l'enfant passé en paramètre.
        @src, tgt deux int
    '''

    def remove_parallel_edge(self, src, tgt):
        #print('src = ', src, ', tgt = ', tgt)
        self.get_node_by_id(src).remove_parent_id(tgt) 
        self.get_node_by_id(tgt).remove_child_id(src)

    '''
        Retire toutes les arêtes impliquant le noeud indentifié par l'id passé en paramètre.
        @param nid un int
    '''

    def remove_node_by_id(self, nid):
        node = self.get_node_by_id(nid)
        list_ = list(node.get_parents_ids())
        for par in list_:
            self.get_node_by_id(par).remove_child_id(nid)
            node.remove_parent_id(par)
        
        l = list(node.get_children_ids())
        for child in l:
            self.get_node_by_id(child).remove_parent_id(nid)
            node.remove_child_id(child)

        if nid in self.outputs:
            self.outputs.remove(nid)
        if nid in self.inputs:
            self.inputs.remove(nid)
        self.nodes.pop(nid)

    '''
        Une méthode qui retire une occurence entre chaque couples parent-enfant passé en paramètre.
        @param pairs une list de list de int
    '''

    def remove_edges(self, pairs=[]):
        for pair in pairs:
            # si on a le temps plus tard, je propose qu'on améliore en remplaçant pairs par une liste de paire
            self.remove_edge(pair[0], pair[1])

    '''
        Une méthode qui retire toutes les occurences entre chaque couples parent-enfant passé en paramètre.
        @param pairs une list de list de int
    '''

    def remove_parallel_edges(self, pairs=[]):
        for pair in pairs:
            self.remove_parallel_edge(pair[0], pair[1])

    '''
        Retire toutes les arêtes impliquant les noeuds indentifiés par les id passé en paramètre.
        @param ids une list de int
    '''

    def remove_nodes_by_id(self, ids):
        for nid in ids:
            self.remove_node_by_id(nid)

    def fusion(self, id1, id2, label=0):
        if label == 1:
            self.get_node_by_id(id1).label = self.get_node_by_id(id2).label
        #print("id1 = ", id1)
        #print(self.get_node_by_id(id1))
        #print("id2 = ", id2)
        #print(self.get_node_by_id(id1))
        self.get_node_by_id(id1).children.update(self.get_node_by_id(id2).children)
        self.get_node_by_id(id1).parents.update(self.get_node_by_id(id2).parents)
        for c in self.get_node_by_id(id2).children:
            c = self.get_node_by_id(c)
            c.parents[id1] = c.parents[id2]
        for c in self.get_node_by_id(id2).parents:
            c = self.get_node_by_id(c)
            c.children[id1] = c.children[id2]
        self.remove_node_by_id(id2)
        
    def fusion_liste(self,l,label=0):
        for pair in l:
            id1 = pair[0]
            id2 = pair[1]
            if label == 1:
                self.get_node_by_id(id1).label = self.get_node_by_id(id2).label
            self.get_node_by_id(id1).children.update(self.get_node_by_id(id2).children)
            self.get_node_by_id(id1).parents.update(self.get_node_by_id(id2).parents)
            for c in self.get_node_by_id(id2).children:
                c = self.get_node_by_id(c)
                c.parents[id1] = c.parents[id2]
            for c in self.get_node_by_id(id2).parents:
                c = self.get_node_by_id(c)
                c.children[id1] = c.children[id2]
        
            self.remove_node_by_id(id2)