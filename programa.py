import sys

class Grafo:
	
    def __init__(self, qtd_vertices):
        self.arestas = {}
        self.vertices = set()
        self.qtd_vertices = qtd_vertices

    def addAresta(self, origem, destino, peso = 0): #Função para adicionar aresta
        if not self.jaExisteEstaAresta(origem, destino): #Verifica se a aresta já não existe
            self.arestas[(origem, destino)] = peso #Se não existe, eu insiro
            if origem not in self.vertices: #Se o vértice de origem não existir no grafo, insere ele
                self.vertices.add(origem)
            if destino not in self.vertices: #Se o vértice de destino não existir no grafo, insere ele
                self.vertices.add(destino)

    def jaExisteEstaAresta(self, origem, destino): #Função que verifica se a aresta já existe
        if (origem, destino) in self.arestas or (destino, origem) in self.arestas:
            return True
        else:
            return False
    
    def addAresta_Vice_Versa(self): #Função que é chamada depois que inserimos todas as arestas, para que exista aresta de ida e aresta de volta (Grafo não direcionado)
        for key in self.arestas.keys():
            if (key[1], key[0]) not in self.arestas.keys():
                 G_aux[(key[1], key[0])] = self.arestas[key]
        self.arestas.update(G_aux)
    
    def ehCompleto(self): #Função que verifica se o grafo é completo. Após inserir as arestas, chamar esta função, se não for completo, deve alertar e mandar isnerir mais arestas 
        for e in self.vertices:
            for i in self.vertices:
                if e != i:
                    if (e, i) not in self.arestas.keys():
                        return False
        return True

if __name__ == "__main__":
    
    G_aux = {}
    Completo = True
    
    print("Digite a quantidade de vertices: ")
    qtd_vertices = int(input())    
    grafo = Grafo(qtd_vertices)
    
    for e in range(1, qtd_vertices + 1):
        print("Nomeie o %dº vertice" % (e))
        vertice = input()
        grafo.vertices.add(vertice)
        
    lista_vertices = sorted(list(grafo.vertices))

    for e in range(0, grafo.qtd_vertices):
        print("Insira as arestas do vertice o %s e seu peso no formato Destino-Peso. Vertice Origem: %s. Digite 0 para finalizar" % (lista_vertices[e], lista_vertices[e]))

        InsereAresta = True

        while InsereAresta == True:    

            aresta = input()

            if aresta == "0": #Não pode inserir
                InsereAresta = False
            else: #Pode inserir 
                grafo.addAresta(lista_vertices[e], aresta[0], aresta[2])
    
    grafo.addAresta_Vice_Versa() 
    #print(grafo.arestas.items())
    
    #if grafo.ehCompleto() == False:
    #    print("Este grafo não é completo, então não é possível encontrar um caminho mínimo")
    #else:
    #    print("Ótimo! Este grafo é completo. Vamos encontrar um caminho mínimo")