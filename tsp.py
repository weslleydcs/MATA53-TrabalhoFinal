import sys

class Grafo:
    
    def __init__(self): #Construtor do grafo
        self.arestas = {}
        self.vertices = set()
    
    def retornaFormatoAresta(self): #Função que retorna o formato de aresta escolhida pelo usuário
        return self.tipoAresta
    
    def addAresta(self, origem, destino, peso = 0): #Função para adicionar aresta
        if not self.jaExisteEstaAresta(origem, destino): #Verifica se a aresta já não existe
            self.arestas[(origem, destino)] = peso #Se não existe, eu insiro esta aresta      
            self.vertices.add(origem) #Trabalhando com conjuntos, salvo o vértice caso não exista
            self.vertices.add(destino) #Se o vértice já existir nem insere pois conjunto não insere elemento igual

    def jaExisteEstaAresta(self, origem, destino): #Função que verifica se a aresta já existe
        if (origem, destino) in self.arestas or (destino, origem) in self.arestas:
            return True
        else:
            return False
    
    def qtd_Vertices(self): #Função para retornar a quantidade de vértices
        return len(self.vertices)
    
    def addAresta_Vice_Versa(self): #Necessária para que exista aresta de ida e aresta de volta Não Direcionado
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
    InsereAresta = True
    EntradaChar = False
    EntradaInt = False
    
    grafo = Grafo()
    
    print("=== TSP : Caixeiro Viajante ===")
    print("--- Digite 1 para inserir no formato (CHAR, CHAR) ---")
    print("--- Digite 2 para inserir no formato (INT, INT) ---")
    
    formato_aresta = int(input())
    
    if formato_aresta == 1: #Se optar por char, transforma o tipo dele em str
        EntradaChar = True
        print("O formato de aresta escolhido foi (CHAR, CHAR)")
    if formato_aresta == 2:
        EntradaInt = True
        print("O formato de aresta escolhido foi (INT, INT)")
    
    print("--- Insira as arestas e seu peso(inteiro) no formato Origem-Destino-Peso. Digite FIM para não inserir mais arestas---")
    
    #Origem-Destino-Peso
    #0       2       4 
    
    while InsereAresta == True:
        
        aresta = input()
        
        if aresta == "FIM": #Tratamento para parar de inserir arestas
            InsereAresta = False
    
        elif EntradaInt == True and aresta[0].isalpha() or EntradaInt == True and aresta[2].isalpha(): #Se optar por int e digitar char
            print("O formato de aresta escolhido foi (INT, INT)")
            
        elif EntradaChar == True and aresta[0].isdigit() or EntradaChar == True and aresta[2].isdigit(): #Se optar por char e digitar int
            print("O formato de aresta escolhido foi (CHAR, CHAR)")
            
        else:
            grafo.addAresta(aresta[0], aresta[2], aresta[4])
    
    grafo.addAresta_Vice_Versa()
    
    print(grafo.arestas.items())
    
    if grafo.ehCompleto() == False:
        print("Este grafo não é completo, então não é possível encontrar um caminho mínimo")
    else:
        print("Ótimo! Este grafo é completo. Vamos encontrar um caminho mínimo")  