import graphviz


def save_as_dot_file(self, path, verbose=False):
        dot = graphviz.Digraph()
        if verbose:
            for node in self.nodes:
                dot.node(node.id,str(node.id)+":"+node.label)
        else:
                dot.node(node.id,node.label)
        for node in self.nodes:
            for c in node.get_children_ids():
                dot.edge(node.id,c)
        open(path,"wb").write(dot.source)