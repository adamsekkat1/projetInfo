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
		return self.parents 

	def get_children_ids(self):
		return self.children 

	def set_id(self , x):
		self.id = x 

	def set_label(self , x):
		self.label = x 

	def set_parents_ids(self , x):
		self.parents = x 

	def set_children_ids(self , x):
		self.children = x 


   



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

	def get_nodes_by_ids(self):
		return [node for node in self.nodes.values().id()] 

	def set_input_ids(self,x):
		self.inputs = x 

	def set_outputs_ids(self,x):
		self.outputs = x 

	def add_input_id(self,x,newinput):
		self.inputs = x 
		self.inputs.append(newinput)

	def add_output_id(self,x,newoutput):
		self.outputs = x
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

	def new_id(self,Nid) :
		a = self.get_node_ids()
		#j = False
		#for i in range(len(a)):
			#if (a[i] == Nid ) :
				#j =  True 
		#if (j != True ):
			#a.append(Nid) 
		if not (Nid in a):
			a.append(Nid)

		return a 
