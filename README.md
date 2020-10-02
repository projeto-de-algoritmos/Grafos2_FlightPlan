# Flight Plan

**Número da Lista**: 2 <br>
**Conteúdo da Disciplina**: Grafos 2<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 16/0133394  |  Lucas Fellipe Carvalho Moreira |
| 15/0009917  |  Gabriel Alves S. de Souza |

## Sobre 
Projeto que consiste em determinar o menor caminho entre dois aeroportos. Foi utilizado um *dataset* encontrado no Kaggle sobre voos de várias companhias aéreas. Apesar de ter várias companhias aéreas, escolhemos a GOL. O projeto utiliza os algoritmos de *Dijkstra*, *Floyd Warshall* e *Prim* para determinar o menor caminho entre dois aeroportos e para gerar a MST (*Minimum Spanning Tree*). 

## Screenshots
### Lista de todos os aeroportos <br>
![Airports](/assets/images/airports.png) <br>
### Aplicação do Algoritmo de Prim (MST)
![MST](/assets/images/mst.png) <br>
### Aplicação do Algoritmo de Floyd Warshall
![Floyd Warshall](/assets/images/floyd-warshall.png) <br>
### Tempo de execução do Algoritmo de Floyd Warshall
![Execution Time](/assets/images/execution-time-floyd-warshall.png) <br>
### Visualização do Grafo gerado pelo algoritmo de Djikstra
![Djikstra Algorithm](/assets/images/graph-visualization-using-djikstra.png)


## Instalação 
**Linguagem**: Python 3<br>
Antes qualquer coisa, clone o repositório ```git clone https://github.com/projeto-de-algoritmos/Grafos2_FlightPlan```, abra o terminal e digite ```cd Grafos2_FlightPlan``` e instale as dependências do Python:
```
# Instale no virtualenv caso queira
pip3 install -r requirements.txt
```

E para rodar o projeto, acesse a pasta src digitando ```cd src``` e, em seguida, digite:
```
python3 graph.py
```

## Uso 
Para usar, basta digitar as opções do menu:

![Menu](/assets/images/menu.png) <br>

* 1 - Lista todos os aeroportos disponíveis;
* 2 - Usa o Algoritmo de *Djikstra* para encontrar o menor caminho entre dois aeroportos;
* 3 - Usa o Algoritmo de *Prim* para encontrar a MST (*Minimum Spanning Tree*);
* 4 - Usa o Algoritmo de *Floyd Warshall* para encontrar o menor caminho entre dois aeroportos;
* 5 - Mostra o tempo de execução do Algoritmo de *Floyd Warshall* para todo o grafo;
* 0 - Sair.




