import math
import sys
from dijkstar import Graph, find_path
import networkx as nx
from matplotlib import pyplot as plt

menor = math.inf
tsp = []
caminhos_finais = []
lista_Visitados = [[]]
lista_arestas = []
graph = Graph(undirected=True)
G = nx.Graph()
caminhos_ham = {}
custos_totais = {} #lista de custos totais
tsps = {}

InsereAresta = True
EntradaChar = False
EntradaInt = False

#Função para verificar se o grafo é completo
def ehCompleto():
    for key in graph.get_data().keys():
        for yek in graph.get_data().keys():
            if key != yek:
                if key not in graph.get_data()[yek].keys():
                    return False
    return True

#Função para encontrar todos os caminhos possíveis a partir de um vértice, mas sem voltar pra ele
def find_all_paths_from(vertice, visitados):
    visitados.append(vertice)
    for vertex in graph.get_data().keys(): #todos os vértices
        if vertex not in visitados:
            find_all_paths_from(vertex, visitados.copy())
    lista_Visitados.append(visitados)

####################################Programa do Usuário####################################
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

print("--- Insira as arestas e seu peso(inteiro) no formato Origem-Destino-Peso. Digite / para não inserir mais arestas---")

#Origem-Destino-Peso
#0       2       4

while InsereAresta == True:

    entrada_split = []
    entrada_tratada = []

    aresta = input()

    entrada_split = aresta.split('-')

    for e in entrada_split:
	    entrada_tratada.append(e)

    if entrada_tratada == ['/']: #Tratamento para parar de inserir arestas
        InsereAresta = False

    elif EntradaInt == True and entrada_tratada[0].isalpha() or EntradaInt == True and entrada_tratada[1].isalpha(): #Se optar por int e digitar char
        print("O formato de aresta escolhido foi (INT, INT)")

    elif EntradaChar == True and entrada_tratada[0].isdigit() or EntradaChar == True and entrada_tratada[1].isdigit(): #Se optar por char e digitar int
        print("O formato de aresta escolhido foi (CHAR, CHAR)")

    else:
        if EntradaChar == True:
            graph.add_edge(entrada_tratada[0], entrada_tratada[1], int(entrada_tratada[2]))
            G.add_edge(entrada_tratada[0], entrada_tratada[1], weight = int(entrada_tratada[2]))
            lista_arestas.append((entrada_tratada[0], entrada_tratada[1], int(entrada_tratada[2])))
        if EntradaInt == True:
            graph.add_edge(int(entrada_tratada[0]), int(entrada_tratada[1]), int(entrada_tratada[2]))
            G.add_edge(entrada_tratada[0], entrada_tratada[1], weight = int(entrada_tratada[2]))
            lista_arestas.append((entrada_tratada[0], entrada_tratada[1], int(entrada_tratada[2])))

if (ehCompleto() == False or len(graph) == 0):
    print("Este grafo não é completo, então não é possível encontrar um caminho mínimo")
    sys.exit()
else:
    print("Ótimo! Este grafo é completo. Vamos encontrar um caminho hamiltoniano!!")

print("----Escolha um vértice para encontrar um caminho hamiltoniano a partir dele----")
print("Vertices disponíveis: ", sorted(graph.get_data().keys())) #ordenar isso aqui para exibir e colocar numa lista

if EntradaInt == True:
    vertice_escolhido = int(input())

if EntradaChar == True:
    vertice_escolhido = str(input())
####################################Programa do Usuário####################################

find_all_paths_from(vertice_escolhido, []) #o usuário escolhe o vértice

for L in lista_Visitados: #para cada caminho presente no grafo
    H = L.copy() #copio este caminho para uma lista auxiliar
    if len(H) == len(graph): #se esste caminho percorre todos os vértices do grafo
        caminhos_finais.append(H) #a lista de caminhos finais recebe este caminho

#print(lista_Visitados, caminhos_finais)
#print(caminhos_finais)

for Lista in caminhos_finais: #para cada caminho que percorre todos os vértices, salvo em um dicionário este caminho e seu peso
    custo_total = 0
    proximo_vertice = 0
    for e in Lista:
        proximo_vertice += 1
        if proximo_vertice < len(Lista):
            no, aresta, custos, custo = find_path(graph, e, Lista[proximo_vertice])
            custo_total += custo
        else: #quando e for o último elemento da lista
            no, aresta, custos, custo = find_path(graph, e, Lista[0])
            custo_total += custo
            custos_totais[tuple(Lista)] = custo_total

for key in custos_totais.keys(): #para cada caminho em caminhos completos sem o vértice inicial:
    custo_caminho = custos_totais[key] #pego o custo desse caminho
    if custo_caminho <= menor: #se esse custo for menor ou igual a um já encontrado:
        menor = custo_caminho #o menor é atualizado
        caminhos_ham[key] = menor #salvo este menor caminho em um dicionário de caminhos hamiltonianos

#print(caminhos_ham.keys())
#print(caminhos_ham.values())

for key in caminhos_ham.keys(): #para cada caminho hamiltoniano encontrado
    lista_key = list(key) #pego este caminho e transformo em uma lista
    lista_key.append(vertice_escolhido) #adiciono nesta lista o vertice_escolhido pelo usuário
    tupla_key = tuple(lista_key) #pego esta lista, que é um caminho e transformo de volta para uma tupla
    tsps[tupla_key] = caminhos_ham[key] #salvo este caminho nos tsps encontrados, com o custo dele

print(tsps.items())

G.add_weighted_edges_from(lista_arestas)

pos = nx.spring_layout(G)
peso_arestas = nx.get_edge_attributes(G, 'weight')

nx.draw(G, pos, with_labels = True, font_weight = 'bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels = peso_arestas)
plt.show()