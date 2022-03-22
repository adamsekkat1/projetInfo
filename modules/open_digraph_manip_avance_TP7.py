class open_digraph_manip_avance_TP7:
	def get_neighbours(self,u,direction):
		"""
		Une fonction qui retourne les voisins du noeud d'id passé en paramètre en fonction de 
		la direction. Les parents si 1, et si -1 les enfants, sinon on rend les deux.
		@param u un int et direction un boolean
		@return une list de int 
		"""
		u = self.get_node_by_id(u)
		if direction == 1:
			return list(u.get_parents_ids())
		if direction == -1:
			return list(u.get_children_ids())
		return list(u.get_parents_ids())+list(u.get_children_ids())



	def dijkstra(self,src,direction=None):
		"""
		Algorithme qui rend le chemin le plus court et les distances 
		entre un noeud src, d'id donné en param, et tous les autres noeuds du graph, en fonction
		de la direction, que les ancêtres si 1 et les descendants si -1.
		@param src un int, direction un boolean
		@return une paire de deux dict
		"""
		Q = [src]
		dist = {src:0}
		prev = {}
		
		while len(Q) > 0:
			u = min(Q,key=dist.get)

			Q.remove(u)
			neighbours = self.get_neighbours(u,direction)
			for v in neighbours:
				if v not in dist:
					Q.append(v)
				if v not in dist or dist[v] > dist[u]+1:
					dist[v] = dist[u]+1
					prev[v] = u
		return dist,prev

	def dijkstra_with_tgt(self,src,tgt=None,direction=None):
		Q = [src]
		dist = {src:0}
		prev = {}
		
		while len(Q) > 0:
			#print(dist)
			u = min(Q,key=dist.get)
			if tgt is not None:
				if tgt == u:
					return dist, prev

			Q.remove(u)
			neighbours = self.get_neighbours(u,direction)
			for v in neighbours:
				if v not in dist:
					Q.append(v)
				if v not in dist or dist[v] > dist[u]+1:
					dist[v] = dist[u]+1
					prev[v] = u
		return dist,prev

	def shortest_path(self,u,v):
		dist, prev = self.dijkstra_with_tgt(u,tgt=v)
		return dist[v]

	def find_ancestors(self,u,res=[]):
		#je suis vraiment pas sûr pour cette fonction
		r = list(self.get_node_by_id(u).get_parents_ids())
		if len(r) == 0:
			return res
		for parent in r:
			r = self.find_ancestors(parent,r)
		return r

	def find_common_ancestors(self,u,v):
		u_ancestors = self.find_ancestors(u)
		v_ancestors = self.find_ancestors(v)
		return list(set(u_ancestors) & set(v_ancestors))

	def common_ancestor_paths(self,u,v):
		common_ancestors = self.find_common_ancestors(u,v)
		print(common_ancestors)
		res = {}
		for com in common_ancestors:
			dist, prev = self.dijkstra(com, direction=-1)
			print(dist)
			res[com] = (dist[u],dist[v])
		return res

	def chercher_noeuds_sans_parents(self):
		n = []
		for noeud in self.nodes.values():
			parents = noeud.get_parents_ids()
			if len(parents) == 0:
				n.append(noeud)
		return n 

	def effacer_parents_dans_noeuds(self,parents):
		for parent in parents:
			for id_,n in self.nodes.items():
				if parent.id in n.get_parents_ids():
					self.nodes[id_].remove_parent_id(parent.id)

	def effacer_noeuds(self,noeuds):
		for n in noeuds:
			del self.nodes[n.id]


	def tri_topologique(self):
		tri = []
		g = self.copy() #on travaillera sur ce graphe
		while len(g.nodes) > 0:
			noeud_sans_parents = g.chercher_noeuds_sans_parents() #sous forme de noeud
			tri.append(noeud_sans_parents)
			g.effacer_parents_dans_noeuds(noeud_sans_parents) 
			g.effacer_noeuds(noeud_sans_parents)

		return [[n.id for n in l ]for l in tri]

	def profondeur_noeud_graphe(self,n):
		tri = self.tri_topologique()
		for t in tri:
			if n in t:
				return tri.index(t)
		

	def profondeur(self):
		return len(self.tri_topologique())

	def dist_chemin_max(self,u,v):
		print(self)
		tri = self.tri_topologique()
		prof_u = self.profondeur_noeud_graphe(u)
		dist = {u:0}
		prev = {}
		for l in tri[prof_u+1:]:
			for w in l:
				
				p = list(self.get_node_by_id(w).get_parents_ids())
				print("node:",w)
				print("parents:",p)
				r =  any([parent in dist for parent in p])
				print("dist:",dist," parents dans dist:",r)
				p = [parent for parent in p if parent in dist]
				if r:
					#prev[w] = list(dist.keys())[list(dist.values()).index(max(p,key=dist.get))]
					dist[w] = dist[max(p,key=dist.get)]+1
					prev[w] = max(p,key=dist.get)
						
				if v == w:
					return dist,prev
		return dist,prev






