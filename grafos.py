#region Inicializacao do programa
print("Digite a quantidade de vertices: ")
qtd_vertices = int(input())

vertices = []
Grafo = {}

for e in range(1, qtd_vertices + 1):
    print("Nomeie o %dº vertice" % (e))
    vertice = str(input())
    vertices.append(vertice)
#endregion

def jaExisteEstaAresta(origem, destino, custo):
    if (origem, destino) in Grafo.keys() or (destino, origem) in Grafo.keys():
        return True
    else:
        return False

for e in range(0, len(vertices)):
    print("Insira as arestas do vertice o %s e seu peso no formato Destino-Peso. Vertice Origem: %s. Digite 0 para finalizar" % (vertices[e], vertices[e]))   
    
    InsereAresta = True
    
    while InsereAresta == True:    
        
        aresta = str(input())
        
        if aresta == "0": #Não pode inserir
            InsereAresta = False
        else: #Pode inserir 
            aux = (vertices[e], aresta[0]) # (origem, destino)
            aux_reverso = (aux[1], aux[0]) # (destino, origem)
            if not jaExisteEstaAresta(aux[0], aux[1], aresta[2]): # verifica se a aresta já existe        
                Grafo[aux] = int(aresta[2])# insere a aresta no formato (origem, destino) : peso
                Grafo[aux_reverso] = int(aresta[2]) # insere a aresta no formato (destino, origem) : peso
            else:
                print("A aresta ({0}, {1}) Já existe no grafo".format(aux[0], aux[1]))
                
print(Grafo) 