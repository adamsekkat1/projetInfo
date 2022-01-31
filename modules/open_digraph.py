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
	def set_id(self , x):
		self.id = x 

	'''
		Un setter qui remplace le label du noeud par le label passé en paramètre.
		@param x, un string
	'''
	def set_label(self , x):
		self.label = x 

	'''
		Un setter qui ajoute aux parents, ceux dont les identifiants sont passés en paramètres.
		@param ids, une liste de int
	'''
	def set_parents_ids(self , ids):
		for n in ids:
			self.parents[n] = 1

	'''
		Un setter qui ajoute aux enfants, ceux dont les identifiants sont passés en paramètres.
		@param ids, une liste de int
	'''
	def set_children_ids(self , ids):
		for n in ids:
			self.children[n] = 1

	'''
		Un setter qui ajoute aux parents, ceux dont les identifiants sont passés en paramètres.
		@param ids, une liste de int
	'''
	'''
	def add_child_id(self, x):
		if x in self.child.keys():
			self.children[x] += 1
		else:
			self.children[x] = 1
	'''
	def add_child_id(self, id_):
		if self.children[id_] != 0:
			self.children[id_] += 1
		else:
			self.children[id_] = 0

	'''
		Une fonction qui permet de rajouter un parent au noeud à l'aide de l'id du parent fourni en paramètres.
		@param x, un int
	'''
	'''
	def add_parent_id(self, x):
		if x in self.parents.keys():
			self.parents[x] += 1
		else:
			self.parents[x] = 1
	'''
	def add_parent_id(self, id_):
		if self.parents[id_] != 0:
			self.parents[id_] += 1
		else:
			self.parents[id_] = 0
	
	'''
		Retire une fois une occurence de l'id du parent donné en paramètre.
		@param idp, un int
	'''
	def remove_parent_once(self,idp):
		self.parents[idp] -= 1
		self.test1_id_below_0(idp)

	'''
		Retire une fois une occurence de l'id de l'enfant donné en paramètre.
		@param idp, un int
	'''
	def remove_child_once(self,idch):
		self.children[idch] -= 1
		self.test2_id_below_0(idch)

	'''
		Test si l'occurence de l'id du parent donné en paramètre est strictement supérieur à 0, dans ce cas il sera retiré de l'attribut.
		@param id, un int
	'''
	def test1_id_below_0(self,id):
		if self.parents[id] <= 0:
			self.parents.pop(id)

	'''
		Test si l'occurence de l'id de l'enfant donné en paramètre est strictement supérieur à 0, dans ce cas il sera retiré de l'attribut.
		@param id, un int
	'''
	def test2_id_below_0(self,id):
		if self.children[id] <= 0:
			self.children.pop(id)

	'''
		Retire toute occurence avec le parent dont l'id est passé en paramètre.
		@param idp, un int
	'''
	def remove_parent_id(self,idp):
		self.parents.pop(idp)

	'''
		Retire toute occurence avec l'enfant dont l'id est passé en paramètre.
		@param idp, un int
	'''
	def remove_child_id(self,idch):
		self.children.pop(idch)
        	

	def __str__(self):
		return str(self.id)

	def __repr__(self):
		return repr(self.id)

	'''
		Retourne une copie du noeud.
		@return un noeud
	'''
	def copy(self):
		return node(self.id,self.label,self.parents.copy(),self.children.copy())



class open_digraph: # for open directed graph
	def __init__(self, inputs, outputs, nodes):
		'''
		inputs: int list; the ids of the input nodes
		outputs: int list; the ids of the output nodes
		nodes: node iter;
		'''
		self.inputs = inputs
		self.outputs = outputs
		self.nodes = {node.id:node for node in nodes} # self.nodes: <int,node> dict

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
		return self.output 

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
		return [node for node in self.nodes.values()] # Je propose qu'on mette juste return self.nodes.values(), cette fonction renvoyant deja une list
	'''
		Un getter qui renvoie la liste des noeuds.
		@return un list de node
	'''
	def get_node_ids(self):
		return list(self.nodes.keys()) #return self.nodes.keys() suffirait également à mon avis

	'''
		Un getter qui renvoie un noeud, identifié par son id passé en paramètre.
		@param id, un int
		@return un node
	'''
	def get_node_by_id(self,id):
		return self.nodes.get(id) #il manque le second paramètre j'ai l'impression, vaudrait mieux à mon avis juste mettre return self.nodes[id], pour que l'erreur soit soulevé si jamais l'id n'est pas reconnu

	'''
		Un getter qui renvoie une liste des noeuds identifié par les id passé en paramètre.
		@param ids, une list de int
		@return une list de node
	'''
	def get_nodes_by_ids(self, ids):
		return [self.get_node_by_id(id) for id in ids]

	'''
		Un setter qui affecte à l'attribut inputs la valeur passé en paramètre.
		@param x un int list
	'''
	def set_input_ids(self,x):
		self.inputs = x 

	'''
		Un setter qui affecte à l'attribut outputs la valeur passé en paramètre.
		@param x un int list
	'''
	def set_outputs_ids(self,x):
		self.outputs = x 

	'''
		Ajoute un l'identifiant passé en paramètre à la liste des inputs.
		@param newinput, un int
	'''
	def add_input_id(self,newinput):
		#self.inputs = x
		self.inputs.append(newinput)

	'''
		Ajoute un l'identifiant passé en paramètre à la liste des outputs.
		@param newoutput, un int
	'''
	def add_output_id(self,newoutput):
		#self.outputs = x
		self.outputs.append(newoutput)




	def __str__(self):
		return "input:"+",".join([str(i) for i in self.inputs])+"\noutput:"+",".join([str(i) for i in self.outputs])
		

	def __repr__(self):
		return "input:"+",".join([repr(i) for i in self.inputs])+"\noutput:"+",".join([repr(i) for i in self.outputs])

	@classmethod
	def empty(self):
		'''
			Une fonction qui crée un graph vide.
			@return un open_digraph
		'''
		return open_digraph([],[],[])

	'''
		Une fonction qui renvoie une copie du graph.
		@return un open_digraph
	'''
	def copy(self):
		return open_digraph(self.inputs.copy(),self.outputs.copy(),self.nodes.copy())

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
	def add_edge(self,src,tgt):
		self.nodes[src].add_child_id(tgt)
		self.nodes[tgt].add_parent_id(src)
    
	'''
		Une fonction qui rajoute un noeud au graph.
		@param optionnels, label un string, parents et children des list de int
	'''
	def add_node(self,label='',parents=[],children=[]):
		id_ = self.new_id()
		n = node(id,label,parents,children)
		if children == []:
			self.add_output_id(id_)
		if parents == []:
			self.add_input_id(id_)
		for p in parents:
			self.nodes[p].add_child_id(id_)
		for c in children:
			self.nodes[c].add_parent_id(id)
			self.nodes[id] = n 
	
	'''
		Une fonction qui permet de créer un noeud en input, qui pointera vers le noeud identifié par l'id passé en paramètre.
		@param _id un int
		@return l
	'''
	def add_input_node(self,_id):
		ID = self.new_id()
		n = node(ID,label='',parents=[],children=[])
		l=add_input_id(ID)  
		ID = _id
		return l 

	'''
		Une fonction qui permet de créer un noeud en output, sur lequel pointera le noeud identifié par l'id passé en paramètre.
		@param _id un int
		@return l
	'''
	def add_output_node(self,_id):
		ID = self.new_id()
		n = node(ID,label='',parents=[],children=[])
		l=add_output_id(ID)  
		ID = _id
		return l 

	#j'ai pas très bien compris la fonction d'Adam mais je propose une alternative ici en bas selon ce que j'ai compris de la question
	'''	
	def add_input_node(self,_id):
		self.add_node(self,label='',parents=[],children=[_id])

	def add_output_node(self,_id):
		self.add_node(self,label='',parents=[_id],children=[])
	'''


	'''
		Une fonction qui vérifie que les input listé dans l'attribut inputs correspondent bien à des noeuds existants
		@return un booléen
	'''
	def inputs_graph(self):
		for Ninput in self.inputs:
			if not bool(self.nodes.get(Ninput,0)):
				return False 
		return True 

	'''
		Une fonction qui vérifie que les output listé dans l'attribut outputs correspondent bien à des noeuds existants
		@return un booléen
	'''
	def outputs_graph(self):
		for Noutput in self.outputs:
			if not bool(self.nodes.get(Noutput,0)):
				return False 
		return True 

	'''
		Une fonction qui verifie pour chaque noeud en input possède bien 0 parent et au moin un enfant.
		@return un boolean
	'''
	def input_1_children(self):
		for Ninput in self.inputs:
			n = self.get_node_by_id()
			l=n.get_parents_ids()
			d=n.get_children_ids()
			if len(l) != 0 or len(d)!= 1 :
				return False
		return True 
	'''
		Une fonction qui verifie pour chaque noeud en output possède bien 0 enfant et au moin un parent.
		@return un boolean
	'''
	def output_1_parent(self):
		for Noutput in self.outputs:
			n=self.get_node_by_id()
			l=n.get_parents_ids()
			d=n.get_children_ids()
			if len(l) != 1 or len(d) != 0 :
				return False 
		return True 

	'''
		Verifie que la clé permettant d'acceder à chaque noeud correspond bien à son identifiant
		@return un booleen
	'''
	def cle_pointe_noeud(self):
		for key,node in self.nodes:
			if key != node.get_id():
				return False 
		return True

	'''
		Verifie que que la multiplicité pour chaque arrête est bien cohérente.
		@return un booléen
	'''
	def multiplicite_vice_versa(self):
		for y in self.nodes :
			parents=y.get_parents_ids()
			parentnodes=self.get_nodes_by_ids(parents)
			for parent in parentnodes:
				if y.get_id() in parent.get_children_ids():
					if y.parents[parent] != parent.children[y.get_id()]:
						return False
				else:
					return False

	'''
		Vérifie que le graph est cohérent.
		@return un booléen
	'''
	def is_well_formed(self):
		if(inputs_graph() and outputs_graph() and input_1_children() and output_1_parent() and cle_pointe_noeud() and multiplicite_vice_versa()):
			return True 
		return False
	
	'''
		Une méthode qui retire une occurence entre le parent et l'enfant passé en paramètre.
		@src, tgt deux int
	'''
	def remove_edge(self,src,tgt):
		self.get_node_by_id(src).remove_parent_once(tgt)
		self.get_node_by_id(tgt).remove_child_once(src)

	'''
		Une méthode qui retire toute occurence entre le parent et l'enfant passé en paramètre.
		@src, tgt deux int
	'''
	def remove_parallel_edge(self, src, tgt):
		self.get_node_by_id(src).remove_parent_id(tgt)
		self.get_node_by_id(tgt).remove_child_id(src)

	'''
		Retire toutes les arêtes impliquant le noeud indentifié par l'id passé en paramètre.
		@param nid un int
	'''
	def remove_node_by_id(self,nid):
		node = self.get_node_by_id(nid)
		[self.remove_parallel_edges(nid,par) for par in node.get_parents_ids()]
		[self.remove_parallel_edges(child,nid) for child in node.get_children_ids()]

	'''
		Une méthode qui retire une occurence entre chaque couples parent-enfant passé en paramètre.
		@param pairs une list de list de int
	'''
	def remove_edges(self,pairs=[]):
		for pair in pairs:
			self.remove_edge(pair[0],pair[1]) #si on a le temps plus tard, je propose qu'on améliore en remplaçant pairs par une liste de paire

	'''
		Une méthode qui retire toutes les occurences entre chaque couples parent-enfant passé en paramètre.
		@param pairs une list de list de int
	'''
	def remove_parallel_edges(self,pairs=[]):
		for pair in pairs:
			self.remove_parallel_edges(pair[0],pair[1])

	'''
		Retire toutes les arêtes impliquant les noeuds indentifiés par les id passé en paramètre.
		@param ids une list de int
	'''
	def remove_nodes_by_id(self,ids):
		for nid in ids:
			self.remove_node_by_id(nid)




