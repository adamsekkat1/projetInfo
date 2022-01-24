from modules.open_digraph import * 
import inspect 


#a=open_digraph.empty() 
a=open_digraph([1,2],[3,4],[node(1,"",[],[2]),node(2,"",[1],[])])
#print(a)
print(a.new_id(9))
#print(dir(open_digraph))
#affiche code source :
#l=inspect.getsource(open_digraph.copy)
#print(l)

#l=inspect.getfile(open_digraph.copy)
#print(l)

