from modules.open_digraph_entity import open_digraph_entity
import math

def to_bin(s, nb_variable):
    res = bin(s)[2:]
    for i in range (int(nb_variable - len(res))):
        res = '0' + res
    return res
    

class open_digraph_Karnaugh(open_digraph_entity):
    def karnaugh(s):
        res = open_digraph_entity.empty()
        nb_variable = math.log(len(s), 2)
        for i in range(int(nb_variable)):
            res.add_node()
        res.add_node(label='|')
        id_out = len(res.nodes.keys()) - 1
        for j in range(len(s)):
            if(s[j] == '1'):
                indice = to_bin(j, nb_variable)
                res.add_node(label='&')
                tmp = len(res.nodes.keys()) - 1
                for i in range(len(indice)):
                    if(indice[i] == '0'):
                        res.add_node(label='~')
                        res.add_edge(i, len(res.nodes.keys()) - 1)
                        res.add_edge(len(res.nodes.keys()) - 1, tmp)
                    else:
                        res.add_edge(i, tmp)
                res.add_edge(tmp, id_out)
        return res

        
                    


