class open_digraph_compositions_mx:
    def find_leaf(self):
        for idn,n in self.nodes:
            if n.get_children_ids() == []:
                return idn 
        return None

    def min_id(self):
        return min(self.get_node_ids())

    def max_id(self):
        return max(self.get_node_ids())



    def shift_indices(self,n):
        self.nodes = {ids+n:val for ids,val in self.nodes.items()}
        for node_ in self.nodes.values():
            node_.id += n
            node_.children = {ids+n:val for ids, val in node_.children.items()}
            node_.parents = {ids+n:val for ids, val in node_.parents.items()}
        self.inputs = [ids+n for ids in self.inputs]
        self.outputs = [ids+n for ids in self.outputs]

    '''
    def iparallel(self,g):
        self.shift_indices(g.max_id())
        self.nodes.update(g.nodes)
        self.inputs += g.inputs
        self.outputs += g.outputs

    def parallel(self,g):
        j = self.copy()
        j.iparallel(g)
        return j
    '''
    

    def iparallel_l(self,l):
        for g in l:
            self.shift_indices(g.max_id())
            self.nodes.update(g.nodes)
            self.inputs += g.inputs
            self.outputs += g.outputs

    def parallel_l(self,l):
        j = self.copy()
        j.iparallel_l(l)
        return j
    

    def icompose(self,g):
        if len(self.outputs) != len(g.inputs):
            raise Exception("Il faut que le nombre d'entrées de g soit égal au nombre de sorties de l'instance")
        self.shift_indices(g.max_id())
        for x in range(len(self.outputs)):
            g.get_node_by_id(g.inputs[x]).add_parent_id(self.outputs[x])

        for x in range(len(self.outputs)):
            self.get_node_by_id(self.outputs[x]).add_child_id(g.inputs[x])
        self.outputs = g.outputs

    def compose(self,g):
        j = self.copy()
        j.icompose(g)
        return j

    def id_in_components(self,idn,components):
        for l in components:
            if idn in l:
                return l
        return None

    def connected_components(self):
        components = []
        for idn,n in self.nodes:
            l = self.id_in_components(idn,components)
            if l is None:
                l = []
                l.append(idn)
                l+= n.get_children_ids()
                l+= n.get_parents_ids()
                components.append(l)
            else:
                for child in idn.get_children_ids():
                    if child not in l:
                        l.append(child)
                for parent in idn.get_parents_ids():
                    if parent not in l:
                        l.append(parent)
        dic = {}
        for idn,n in self.nodes:
            dic[idn] = components.index(self.id_in_components(idn,components))
        return len(components), dic

    def get_open_digraphs(self):
        num, dic = self.connected_components()
        l = []
        for n in range(num):
            g = open_digraph_entity.empty()
            for idn,val in dic.keys():
                if val== n:
                    g.nodes[idn] = self.get_node_by_id(idn)
                    if idn in self.inputs:
                        g.inputs.append(idn)
                    if idn in self.outputs:
                        g.outputs.append(idn)
            l.append(g)
        return l


