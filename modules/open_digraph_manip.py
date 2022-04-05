
class open_digraph_manip:

	def get_neighbours(self,u,direction):
		if direction == 1:
			return [self.get_nodes_from_id(nid) for nid in u.get_parent_ids()]
		if direction == -1:
			return [self.get_nodes_from_id(nid) for nid in u.get_children_ids()]
		return [self.get_nodes_from_id(nid) for nid in u.get_parent_ids()]+[self.get_nodes_from_id(nid) for nid in u.get_children_ids()]


	def dijkstra(self,src,direction=None):
		Q = [src]
		dist = {src:0}
		prev = {}
		while len(Q) > 0:
			u = Qmin(Q,dist.get)
			Q.remove(u)
			neighbours = get_neighbours(u,direction)
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
			u = Qmin(Q,dist.get)
			if tgt is not None:
				if tgt == u:
					return dist,prev
			Q.remove(u)
			neighbours = get_neighbours(u,direction)
			for v in neighbours:
				if v not in dist:
					Q.append(v)
				if v not in dist or dist[v] > dist[u]+1:
					dist[v] = dist[u]+1
					prev[v] = u
		return dist,prev

	def shortest_path(self,u,v):
		dist, prev = self.dijkstra_with_tgt(u,tgt=v)
		return dist[tgt]

	def find_ancestors(self,u,res=[]):
		#je suis vraiment pas sûr pour cette fonction
		r = u.get_parent_nodes()
		if len(r) == 0:
			return res + r
		for parent in r:
			r += self.find_ancestors(parent,r)
		return r

	def find_common_ancestors(self,u,v):
		u_ancestors = self.find_ancestors(u)
		v_ancestors = self.find_ancestors(v)
		return list(set(u_ancestors) & set(v_ancestors))

	def common_ancestor_paths(self,u,v):
		common_ancestors = self.find_common_ancestors(u,v)
		res = {}
		for com in common_ancestors:
			dist, prev = self.dijkstra(com,direction=1)
			res[com] = (dist[u],dist[v])
		return res








