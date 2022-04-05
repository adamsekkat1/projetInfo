from modules.open_digraph_entity import * 
import inspect 
import tests.open_digraph_test

#a=open_digraph.empty() 
#a.add_node()
#a.add_node()
#a=open_digraph([1,2],[3,4],[node(1,"",[],[2]),node(2,"",[1],[])])
#print(a)
#print(a.new_id(9))
#a=open_digraph([1,2],[3,4],[node(1,"",[],[2]),node(2,"",[1],[])])

#print(dir(open_digraph))
#affiche code source :
#l=inspect.getsource(open_digraph.copy)
#print(l)

#l=inspect.getfile(open_digraph.copy)
#print(l)
#print(inspect.getmembers(open_digraph_entity))
tests.open_digraph_test.GraphTest()
