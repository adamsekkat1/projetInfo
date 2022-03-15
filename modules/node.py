class node:
    def __init__(self, identity, label, parents, children):
        '''
        identity: int; its unique id in the graph
        label: string;
        parents: int->int dict; maps a parent node's id to its multiplicity
        children: int->int dict; maps a child node's id to its multiplicity
        '''
        self.id = identity
        self.label = label
        self.parents = parents
        self.children = children
    

    def __init__(self, identity, label, parents, children):
        '''
        identity: int; its unique id in the graph
        label: string;
        parents: int->int dict; maps a parent node's id to its multiplicity
        children: int->int dict; maps a child node's id to its multiplicity
        '''
        self.id = identity
        self.label = label
        self.parents = parents
        self.children = children

    '''
        Un getter qui renvoie l'attribut id, l'identifiant du noeud.
        @return un int
    '''

    def get_id(self):
        return self.id

    '''
        Un getter qui renvoie le label du noeud.
        @return un string
    '''

    def get_label(self):
        return self.label

    '''
        Un getter qui renvoie les identifiants des parents du noeud.
        @return une list de int
    '''

    def get_parents_ids(self):
        return self.parents.keys()

    '''
        Un getter qui renvoie les identifiants des enfants du noeud.
        @return une list de int
    '''

    def get_children_ids(self):
        return self.children.keys()

    '''
        Un setter qui remplace l'identifiant du noeud par l'identifiant passé en paramètre.
        @param x, un int
    '''

    def set_id(self, x):
        self.id = x

    '''
        Un setter qui remplace le label du noeud par le label passé en paramètre.
        @param x, un string
    '''

    def set_label(self, x):
        self.label = x

    '''
        Un setter qui ajoute aux parents, ceux dont les identifiants sont passés en paramètres.
        @param ids, une liste de int
    '''

    def set_parents_ids(self, ids):
        for n in ids:
            self.parents[n] = 1

    '''
        Un setter qui ajoute aux enfants, ceux dont les identifiants sont passés en paramètres.
        @param ids, une liste de int
    '''

    def set_children_ids(self, ids):
        for n in ids:
            self.children[n] = 1

    '''
        Un setter qui ajoute aux parents, ceux dont les identifiants sont passés en paramètres.
        @param ids, une liste de int
    '''

    def add_child_id(self, x):
        if x in self.children.keys():
            self.children[x] += 1
        else:
            self.children[x] = 1

    '''
        Une fonction qui permet de rajouter un parent au noeud à l'aide de l'id du parent fourni en paramètres.
        @param x, un int
    '''

    def add_parent_id(self, x):
        if x in self.parents.keys():
            self.parents[x] += 1
        else:
            self.parents[x] = 1

    '''
        Retire une fois une occurence de l'id du parent donné en paramètre.
        @param idp, un int
    '''

    def remove_parent_once(self, idp):
        self.parents[idp] -= 1
        self.test1_id_below_0(idp)

    '''
        Retire une fois une occurence de l'id de l'enfant donné en paramètre.
        @param idp, un int
    '''

    def remove_child_once(self, idch):
        self.children[idch] -= 1
        self.test2_id_below_0(idch)

    '''
        Test si l'occurence de l'id du parent donné en paramètre est strictement supérieur à 0, dans ce cas il sera retiré de l'attribut.
        @param id, un int
    '''

    def test1_id_below_0(self, id_):
        if self.parents[id_] <= 0:
            self.parents.pop(id_)

    '''
        Test si l'occurence de l'id de l'enfant donné en paramètre est strictement supérieur à 0, dans ce cas il sera retiré de l'attribut.
        @param id, un int
    '''

    def test2_id_below_0(self, id_):
        if self.children[id_] <= 0:
            self.children.pop(id_)

    '''
        Retire toute occurence avec le parent dont l'id est passé en paramètre.
        @param idp, un int
    '''

    def remove_parent_id(self, idp):
        self.parents.pop(idp)

    '''
        Retire toute occurence avec l'enfant dont l'id est passé en paramètre.
        @param idp, un int
    '''

    def remove_child_id(self, idch):
        self.children.pop(idch)

    '''
    renvoit les informations sur le noeud, le label, l'id, les parents et les enfants
    '''
    def __str__(self):
        return self.label+"[id="+str(self.get_id())+"]:"+str(self.parents)+"->"+str(self.children)

    def __repr__(self):
        return str(self)

    '''
        Retourne une copie du noeud.
        @return un noeud
    '''

    def copy(self):
        return node(self.id, self.label, self.parents.copy(), self.children.copy())

    '''

    '''
    def indegree(self):
        return len(self.parents.keys)

    def outdegree(self):
        return len(self.children.keys)

    def degree(self):
        return self.indegree()+self.outdegree()