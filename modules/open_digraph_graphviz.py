import os
import graphviz
import webbrowser
from modules.node import node

nbfichier = 0


class open_digraph_graphviz:
    def save_as_dot_file(self, path, verbose=True):
        t = "   "
        newline = "\n"
        src = ""
        file = open(path,"w")

        #on ajoute la premiere ligne
        src += "digraph G{"+newline

        #pour chaque noeud
        for n in self.nodes.values():
            #on fait un tab
            src += t
            #on ajoute l'id
            src += str(n.get_id())
            #si verbose est vrai on ajoute aussi le label
            if verbose:
                label = str(n.get_label())
                if len(label) > 0:
                    src += ' [label="'+label+'",'
                else:
                    src += "["
                
            else:
                src += "["
            src += "input="
            if n.get_id() in self.inputs:
                src += "true"
            else:
                src += "false"

            src += ",output="
            if n.get_id() in self.outputs:
                src += "true"
            else:
                src += "false"
            src += "]"
            #on ajoute un point virgule 
            src += ";"
            #on passe a la prochaine ligne
            src += newline


        for n in self.nodes.values():
            #on va ajouter les liens entre le noeud et les enfants
            for nid,number_of_conn in n.children.items():
                for _ in range(number_of_conn):
                    src += t
                    src += str(n.get_id())+"->"+str(nid)
                    src += ";"
                    src += newline

        #on ajoute l'acolade de fin 
        src += "}"

        #on enregistre le fichier et on le ferme
        file.write(src)
        file.close()

    def from_dot_file(self,filename):
        file = open(filename, "r").readlines()
        #on enleve la premiere et la derniere ligne
        file = file[1:]
        file = file[:-1]


        #en retire tous les chars dont on s'en fiche
        file = [f.strip(" ];\n") for f in file]

        #on récupère les nodes
        for f in file:
            ligne = f.partition("[")
            #print(ligne)


            #si la ligne est une ligne de declaration de node
            if ligne[1] != '':
                n = node(int(ligne[0]),"",{},{})
                l = ligne[-1].split(",")
                #si il y a un label on l'ajoute au noeud
                if l[0].startswith("label"):
                    n.set_label(l[0].split("=")[-1])
                    l = l[1:]
                self.nodes[n.get_id()] = n
                #si c'est un input ou un output on l'ajoute
                for s in l:
                    if s.startswith("input"):
                        if s.split("=")[-1] == "true":
                            self.inputs.append(n.get_id())
                    if s.startswith("output"):
                        if s.split("=")[-1] == "true":
                            self.outputs.append(n.get_id())

        for f in file:
            ligne = f.partition("[")
            if ligne[1] == '':
                l = ligne[0].split("->")
                self.nodes[int(l[0])].add_child_id(int(l[1]))
                self.nodes[int(l[1])].add_parent_id(int(l[0]))


    def display(self, verbose=False):
        global nbfichier
        self.save_as_dot_file("temporary" + str(nbfichier) + ".dot",verbose)
        os.system("dot -Tpdf temporary" + str(nbfichier) + ".dot -o temporary" + str(nbfichier) + ".pdf")
        #webbrowser.open_new(os.getcwd() + "temporary" + str(nbfichier) + ".pdf")
        nbfichier += 1
