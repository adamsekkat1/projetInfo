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

	def get_id(self):
		return self.id

	def get_label(self):
		return self.label 

	def get_parents_ids(self):
		return self.parents.keys()

	def get_children_ids(self):
		return self.children.keys() 

	def set_id(self , x):
		self.id = x 

	def set_label(self , x):
		self.label = x 

	def set_parents_ids(self , ids):
		for n in ids:
			self.parents[n] = 1

	def set_children_ids(self , ids):
		for n in ids:
			self.children[n] = 1

    def add_child_id(self, id_):
    	if self.children[id_] != 0:
        	self.children[id_] += 1
        else:
        	self.children[id_] = 0

    def add_parent_id(self, x):
        self.parents.append(x)

    def remove_parent_once(self,idp):
        self.parents[idp] -= 1
        self.test1_id_below_0(idp)

    def remove_child_once(self,idch):
    	self.children[idch] -= 1
    	self.test2_id_below_0(idch)

    def test1_id_below_0(self,id):
    	if self.parents[id] <= 0:
    		self.parents.pop(id)

    def test2_id_below_0(self,id):
    	if self.children[id] <= 0:
    		self.children.pop(id)

    def remove_parent_id(self,idp):
    	self.parents.pop(idp)

    def remove_child_id(self,idch):
    	self.children.pop(idch)

    def add_parent_id(self, id_):
        if self.parents[id_] != 0:
        	self.parents[id_] += 1
        else:
        	self.parents[id_] = 0
        	

	def __str__(self):
		return str(self.id)

	def __repr__(self):
		return repr(self.id)

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

	def get_inputs_ids(self):
		return self.inputs 

	def get_outputs_ids(self):
		return self.output 

	def get_id_node_map(self):
		return self.nodes 

	def get_nodes(self):
		return [node for node in self.nodes.values()] 

	def get_node_ids(self):
		return list(self.nodes.keys())

	def get_node_by_id(self,id):
		return self.nodes.get(id)

	def get_nodes_by_ids(self, ids):
		return [self.get_node_by_id(id) for id in ids]

	def set_input_ids(self,x):
		self.inputs = x 

	def set_outputs_ids(self,x):
		self.outputs = x 

	def add_input_id(self,newinput):
		#self.inputs = x
		self.inputs.append(newinput)

	def add_output_id(self,newoutput):
		#self.outputs = x
		self.outputs.append(newoutput)


	def __str__(self):
		return "input:"+",".join([str(i) for i in self.inputs])+"\noutput:"+",".join([str(i) for i in self.outputs])
		

	def __repr__(self):
		return "input:"+",".join([repr(i) for i in self.inputs])+"\noutput:"+",".join([repr(i) for i in self.outputs])

	@classmethod
	def empty(self):
		return open_digraph([],[],[])

	def copy(self):
		return open_digraph(self.inputs.copy(),self.outputs.copy(),self.nodes.copy())

	def new_id(self):
		a = self.get_node_ids()
		z = 0
		while True:
            if z not in a:
                return z
            z += 1
        

    def add_edge(self,src,tgt):
        self.nodes[src].add_child_id(tgt)
        self.nodes[tgt].add_parent_id(src)
        
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

    def inputs_graph(self):
    	for Ninput in self.inputs:
    		if self.nodes.get(Ninput,True):
    			return False 
    	return True 

    def outputs_graph(self):
    	for Noutput in self.outputs:
    		if self.nodes.get(Noutput,True):
    			return False 
    	return True 

    def input_1_children(self):
    	for Ninput in self.inputs:
    		n = self.get_node_by_id()
    		l=n.get_parents_ids()
    		d=n.get_children_ids()
    		if len(l) != 0 or len(d)!= 1 :
    			return False
    	return True 

    def output_1_parent(self):
    	for Noutput in self.outputs:
    		n=self.get_node_by_id()
    		l=n.get_parents_ids()
    		d=n.get_children_ids()
    		if len(l) != 1 or len(d) != 0 :
    			return False 
    	return True 

    def cle_pointe_noeud(self):
    	for key,node in self.nodes:
    		if key != node.get_id():
    			return False 
    	return True

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

    def is_well_formed(self):
    	if(inputs_graph() and outputs_graph() and input_1_children() and output_1_parent() and cle_pointe_noeud() and multiplicite_vice_versa()):
    		return True 
        
    def remove_edge(self,src,tgt):
    	self.get_node_by_id(src).remove_parent_once(tgt)
    	self.get_node_by_id(tgt).remove_child_once(src)

    def remove_parallel_edge(self, src, tgt):
    	self.get_node_by_id(src).remove_parent_id(tgt)
    	self.get_node_by_id(tgt).remove_child_id(src)

    def remove_node_by_id(self,nid):
    	node = self.get_node_by_id(nid)
    	[self.remove_parallel_edges(nid,par) for par in node.get_parents_ids()]
    	[self.remove_parallel_edges(child,nid) for child in node.get_children_ids()]

    def remove_edges(self,pairs=[]):
    	for pair in pairs:
    		self.remove_edge(pair[0],pair[1])

    def remove_parallel_edges(self,pairs=[]):
    	for pair in pairs:
    		self.remove_parallel_edges(pair[0],pair[1])

    def remove_nodes_by_id(self,ids):
    	for nid in ids:
    		self.remove_nodes_by_id(nid)




