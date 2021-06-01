# MATA53-TrabalhoFinal

* [Apresentação](#apresentacao)
* [TSP](#tsp)
* [Complexidade](#complexidade)
* [Bibliotecas](#bibliotecas)
* [Video](#video)
* [Exemplo](#exemplo)


## [<svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg>](#apresentacao)Apresentacao

* Trabalho Final: Algoritmo do TSP(Travelling Salesman Problem)
* UFBA: Dsiciplina MATA53 - Teoria dos Grafos
* Professor: Tiago de Oliveira Januário
* Aluno: Weslley Daltro de Castro Silva


## [<svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg>](#tsp)TSP

O TSP(Travelling Salesman Problem) ou Problema do caixeiro viajante em português é um algoritmo clássico de otimização combinatória. Ele surgiu, baseado na necessidade de vendedores em realizar entregas em diversos locais (cidades) percorrendo o menor caminho possível, reduzindo o tempo necessário para a viagem e os possíveis custos com transporte e combustível.

Dado um conjunto de cidades e a distância entre cada par de cidades, o problema é encontrar a rota mais curta possível que visite todas as cidades exatamente uma vez e retorne ao ponto de partida.

O TSP se parece muito com outro problema de grafos, o problema do ciclo hamiltoniano. Seu algoritmo é descobrir se existe um passeio que visite todas as cidades exatamente uma vez. Quando trabalhamos com Grafos completos, sabemos que estes passeios existem, o problema é econtrar um ciclo hamiltoniano, de peso mínimo, este seria o TSP.

Solução:
* Considere a cidade 1 como ponto inicial e final.
* Gere todas as (n-1)! Permutações de cidades.
* Calcule o custo de cada permutação e acompanhe a permutação de custo mínimo.
* Retorne a permutação com custo mínimo.


## [<svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg>](#complexidade)Complexidade

* Tempo de Complexidade: Θ(n!)
* Programação Dinâmica:

Seja o conjunto de vértices dado {1, 2, 3, 4,… .n}. Consideramos 1 como vértice inicial e final do grafo. Para cada outro vértice i (diferente de 1), encontramos o caminho de custo mínimo com 1 como ponto inicial, i como ponto final e todos os vértices aparecendo exatamente uma vez. 

Seja o custo deste caminho o custo (i), o custo do Ciclo correspondente seria custo (i) + distância (i, 1) onde distância (i, 1) é a distância de i a 1. 

Finalmente, retornamos o mínimo de todos os valores [custo (i) + distância (i, 1)]. A questão é como obter o custo (i)? Para calcular o custo (i) usando a Programação Dinâmica, precisamos ter alguma relação recursiva em termos de subproblemas. 

Definimos um termo: C (S, i) o custo do caminho de custo mínimo visitando cada vértice no conjunto S exatamente uma vez, começando em 1 e terminando em i.

Começamos com todos os subconjuntos de tamanho 2 e calculamos C (S, i) para todos os subconjuntos onde S é o subconjunto, então calculamos C (S, i) para todos os subconjuntos S de tamanho 3 e assim por diante, lembrando que 1 deve estar presente em cada subconjunto.

Para um conjunto de tamanho n, consideramos n-2 subconjuntos, cada um com tamanho n-1, de forma que todos os subconjuntos não tenham n-ésimo elemento.
Usando a relação de recorrência acima, podemos escrever uma solução baseada em programação dinâmica. Existem no máximo O (n * 2^n ) subproblemas, e cada um leva um tempo linear para ser resolvido. O tempo total de execução é, portanto, O (n² * 2^n). A complexidade do tempo é muito menor do que O (n!), Mas ainda exponencial. O espaço necessário também é exponencial. Portanto, essa abordagem também é inviável mesmo para um número ligeiramente maior de vértices.

## [<svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg>](#bibliotecas)Bibliotecas

Para que o algoritmo funcione, é necessário instalar/configurar algumas bibliotecas. Os comandos estão melhor separados no arquivo pips.txt. No Terminal de comando ou no cmd do windows digite:

* pip install dijkstar
* pip install networkx
* pip install tk
* python -m pip install -U matplotlib

## [<svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg>](#video)Video

O vídeo contendo a explicação do algoritmo, implementação, execução e exibição está melhor explicado no link do vídeo abaixo: https://youtu.be/W54NOjvx3Ek

## [<svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg>](#exemplo)Exemplo

Exemplo ilustrativo de um grafo para realização do TSP

![Formula de pi](https://github.com/weslleydcs/MATA53-TrabalhoFinal/blob/main/TSP.PNG)
