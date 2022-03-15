import os
import graphviz
import webbrowser


class open_digraph_graphviz:
    def save_as_dot_file(self, path, verbose=False):
        dot = graphviz.Digraph()
        if verbose:
            for node_ in self.get_nodes():
                dot.node(str(node_.id),str(node_.id)+":"+node_.label)
        else:
            for node_ in self.get_nodes():
                dot.node(str(node_.id),node_.label)
        for node_ in self.get_nodes():
            for c in node_.get_children_ids():
                dot.edge(str(node_.id),str(c))
        open(path,"wt").write(dot.source)

    def dislay(self, verbose=False):
        self.save_as_dot_file("temporary.dot", verbose)
        os.system("dot -Tpdf temporary.dot -o temporary.pdf")
        webbrowser.open_new(os.getcwd() + "temporary.pdf")
