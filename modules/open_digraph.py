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

	def set_parents_ids(self , nodes):
		for n in nodes:
			self.parents[n.get_id()] = n

	def set_children_ids(self , nodes):
		for n in nodes:
			self.children[n.get_id()] = n

    def add_child_id(self, node):
        self.children[node.get_id()] = node
        
    def add_parent_id(self, node):
        self.parents[node.get_id()] = node

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
		return open_digraph(self.inputs.copy(),self.outputs.copy(),[node for node in self.nodes.values()])

	def new_id(self) :
		a = self.get_node_ids()
		#j = False
		#for i in range(len(a)):
			#if (a[i] == Nid ) :
				#j =  True 
		#if (j != True ):
			#a.append(Nid)
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
            self.nodes[c].add_parent_id(id_)
        self.nodes[id_] = n 
