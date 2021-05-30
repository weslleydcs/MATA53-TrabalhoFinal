import math
import sys
from dijkstar import Graph, find_path
import networkx as nx
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import *

window = tk.Tk()
frame_1 = tk.Frame()
frame_2 = tk.Frame()
frame_3 = tk.Frame()
frame_4 = tk.Frame()
menor = math.inf
tsp = []
caminhos_finais = []
lista_Visitados = [[]]
lista_arestas = []
lista_caminho_1_2 = []
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

def escolherFormato():

    frame_1.pack_forget()
    frame_2.pack_forget()
    frame_3.pack()
    if e1.get() == '1': #Se optar por char, transforma o tipo dele em str
        EntradaChar = True
        #print(EntradaChar)
    if e1.get() == '2':
        EntradaInt = True
        #print(EntradaInt)

def add_Aresta():

    if e1.get() == '1':
        graph.add_edge(e2.get(), e3.get(), e4.get())
        G.add_edge(e2.get(), e3.get(), weight = int(e4.get()))
        lista_arestas.append((e2.get(), e3.get(), int(e4.get())))
        #print(G.nodes())
    if e1.get() == '2':
        graph.add_edge(int(e2.get()), int(e3.get()), int(e4.get()))
        G.add_edge(int(e2.get()), int(e3.get()), weight = int(e4.get()))
        lista_arestas.append((int(e2.get()), int(e3.get()), int(e4.get())))
        #print(G.nodes())

    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    e4.delete(0, tk.END)

def VerificaCompletude():

    frame_3.pack_forget()

    if (ehCompleto() == False or len(graph) == 0):
        #print("Este grafo não é completo, então não é possível encontrar um caminho mínimo")
        sys.exit()
    #else:
        #print("Ótimo! Este grafo é completo. Vamos encontrar um caminho hamiltoniano!!")

    frame_4.pack()

def encontraCicloHam():

    global menor
    caminhos = []
    caminho_1 = []
    caminho_2 = []

    if e1.get() == '1':
        vertice_escolhido = e5.get()

    if e1.get() == '2':
        vertice_escolhido = int(e5.get())

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

        lista_caminho_1_2.append(lista_key) #Lista auxiliar apenas para printar os caminhos depois

    #print(tsps.items())

    caminho_1 = lista_caminho_1_2[0]
    caminho_2 = lista_caminho_1_2[1]

    fig = plt.figure(num='Modelo TSP: Custo Mínimo = {0}, Caminho 1 = {1}, Caminho 2 = {2}'.format(menor, caminho_1, caminho_2))

    G.add_weighted_edges_from(lista_arestas)

    pos = nx.spring_layout(G)
    peso_arestas = nx.get_edge_attributes(G, 'weight')

    nx.draw(G, pos, with_labels = True, font_weight = 'bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels = peso_arestas)

    fig.show()
########################################################################Programa do Usuário########################################################################

tk.Label(master=frame_1, text="Digite 1 para formato (CHAR, CHAR). Digite 2 para formato (INT, INT)").grid(row=0)
e1 = tk.Entry(master=frame_1)
e1.grid(row=3, column=0)

tk.Button(master=frame_2, text='Escolher Formato', command=escolherFormato).grid(row=4, column=0, sticky=tk.W, pady=0)

tk.Label(master=frame_3, text="Insira as arestas e seu peso(inteiro) no formato Origem-Destino-Peso").grid(row=0)

tk.Label(master=frame_3, text="Digite um vértice no formato de entrada escolhido").grid(row=1)
e2 = tk.Entry(master=frame_3)
e2.grid(row=1, column=1)

tk.Label(master=frame_3, text="Digite outro vértice no formato de entrada escolhido").grid(row=2)
e3 = tk.Entry(master=frame_3)
e3.grid(row=2, column=1)

tk.Label(master=frame_3, text="Digite o Peso desta aresta").grid(row=3)
e4 = tk.Entry(master=frame_3)
e4.grid(row=3, column=1)

tk.Button(master=frame_3, text='Adicionar Aresta', command=add_Aresta).grid(row=4, column=1, sticky=tk.W, pady=0)
tk.Button(master=frame_3, text='Gerar TSP', command=VerificaCompletude).grid(row=4, column=2, sticky=tk.W, pady=0)

tk.Label(master=frame_4, text="Escolha um vértice para encontrar um caminho hamiltoniano a partir dele: ").grid(row=0) #sorted(graph.get_data().keys())
e5 = tk.Entry(master=frame_4)
e5.grid(row=0, column=1)

tk.Button(master=frame_4, text='Encontrar Ciclo', command=encontraCicloHam).grid(row=1, column=1, sticky=tk.W, pady=0)

window.title("TSP")

frame_1.pack()
frame_2.pack()

window.geometry('600x600')
window.mainloop()
####################################Programa do Usuário####################################
