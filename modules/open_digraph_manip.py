
class open_digraph_manip:

	def get_neighbours(self,u,direction):
		u = self.get_node_by_id(u)
		if direction == 1:
			return list(u.get_parents_ids())
		if direction == -1:
			return list(u.get_children_ids())
		return list(u.get_parents_ids())+list(u.get_children_ids())



	def dijkstra(self,src,direction=None):
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








