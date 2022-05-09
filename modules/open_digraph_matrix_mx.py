import numpy as np
import random


class open_digraph_matrix_mx:
        
    def adjacency_matrix(self):
        d = from_id_to_index(self)
        M = np.zeros((len(self.get_node_ids()),len(self.get_node_ids())))
        for index,id_ in d:
            for c in id_.get_children_ids():
                M[index][d[c]] = id_.children[c]
        return M
    @classmethod
    def graph_from_adjency_matrix(cls, M):
        g = cls.empty()
        for ligne in range(len(M)) :
            g.add_node()

        for ligne in range(len(M)) :
            for j in range(len(M[ligne])):
                for _ in range(M[ligne][j]):
                    g.add_edge(ligne,j)
        return g 

    @classmethod
    def random_matrix(cls, n, bound, inputs=0, outputs=0, form="free"):
        '''
        Doc
        Bien pr´eciser ici les options possibles pour form !
        '''
        assert n >= inputs+outputs
        if form=="free":
            M=random_int_matrix(n,bound,null_diag=False)
        elif form=="DAG":
            M=random_triangular_int_matrix(n,bound)
        elif form=="oriented":
            M=random_oriented_int_matrix(n,bound)
        elif form=="loop-free":
            M=random_int_matrix(n,bound)
        elif form=="undirected":
            M=random_symetric_int_matrix(n, bound,null_diag=False)
        elif form=="loop-free undirected":
            M=random_symetric_int_matrix(n, bound)

        print(M)
        g =  cls.graph_from_adjency_matrix(M)
        for i in range(inputs):
            a = random.randint(0,n)
            while a in g.inputs:
                a = random.randint(0,n)
            g.add_input_id(a)

        for i in range(outputs):
            a = random.randint(0,n)
            while a in g.inputs or a in g.outputs :
                a = random.randint(0,n)
            g.add_output_id(a)
        return g 

def from_id_to_index(G):
    return {id_:i for id_,i in enumerate(G.get_node_ids())}

def random_int_list(n,bound):
    t=[]
    for i in range(n):
        s=random.randint(0, bound)
        t.append(s)
    return t 

def random_int_matrix(n,bound,null_diag=True):
    t=[]
    for i in range(n):
        t.append(random_int_list(n,bound))
        if(null_diag):
            t[i][i]=0
    return t 
def random_symetric_int_matrix(n,bound,null_diag=True):
    t=[]
    for i in range(n):
        t.append([])
        for j in range(n):
            t[i].append(0)
        if(null_diag):
            for j in range(i):
                t[i][j]=random.randint(0,bound)
                if(i != j):
                    t[j][i] = t[i][j]
        else :
            for j in range(i+1):
                t[i][j] = random.randint(0,bound)
                if(i != j):
                    t[j][i] = t[i][j]
    return t 

def random_oriented_int_matrix(n,bound,null_diag=True):
    M=[]
    for i in range(n):
        if null_diag:
            M.append(random_int_list(i,bound)+[0]*(n-i+1))
        else:
            M.append(random_int_list(i,bound)+[0]*(n-i))
    return M 

def random_triangular_int_matrix(n,bound,null_diag=True):
    M=[[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i>j:
                M[i][j] = 0 
            elif i == j and null_diag:
                M[i][j] = 0 
            else:
                M[i][j]=random.randint(0,bound)
    return M 








