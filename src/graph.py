import json, math
import gol_flights, graph_algorithms
import networkx as nx
import matplotlib.pyplot as plt
import pprint
import os, json

def create_graph():
  with open('../gol_flights_json') as json_file:
    dt = json.load(json_file)
  graph = {}
  for (key, value) in dt['Aeroporto.Origem'].items():
    if not graph.get(value):
      graph[value] = {}

    _from = {'latitude': dt['LatOrig'][key], 'longitude': dt['LongOrig'][key]}
    to = {'latitude': dt['LatDest'][key], 'longitude': dt['LongDest'][key]}
    graph[value][dt['Aeroporto.Destino'][key]] = gol_flights.distance(_from, to)
  return graph

def list_airports(graph):
  airports = set()
  for _from in graph:
    airports.add(_from)
    for to in graph[_from]:
      airports.add(to)
  return airports

def plot_graph(path):
  G = nx.DiGraph()
  G.add_nodes_from(path.keys())
  for s in path.keys():
    for u in path[s]:
      G.add_edge(s, u)
  pos = nx.spring_layout(G)
  plt.figure(4,figsize=(10,7))

  nx.draw_networkx(
    G,
    pos = nx.spring_layout(G, k = 0.5, iterations = 25),
    font_color = 'r'
  )
  plt.show();

def plot_graph_shortest_path(path):
  G = nx.DiGraph()
  G.add_nodes_from(path.keys())
  for s in path.keys():
    G.add_edge(s, path[s])
  pos = nx.spring_layout(G)
  plt.figure(4,figsize=(10,7))

  nx.draw_networkx(
    G,
    pos = nx.spring_layout(G, k = 0.5, iterations = 25),
    font_color = 'black'
  )
  plt.show();

def plot_graph_shortest_path(path, cost):
  G = nx.DiGraph()
  G.add_nodes_from(path.keys())
  for s in path.keys():
      G.add_edge(s, path[s])
  pos = nx.spring_layout(G)
  plt.figure(4,figsize=(20,10))
  nx.draw_networkx(
    G,
    pos = nx.spring_layout(G, k = 0.5, iterations = 25),
    font_color = 'black'

  )
  plt.text(0, 0.5, 'Minimum distance = %f' % cost + ' km')
  plt.show();

def menuPortuguese():
  print('1 - Lista de todos aeroportos')
  print('2 - Algoritmo de Dijkstra para encontrar o menor caminho entre dois aeroportos')
  print('3 - Gerar a árvore geradora mínima usando o algoritmo de prim')
  print('4 - Algoritmo de Floyd Warshall para encontrar a distância mínima entre dois aeroportos')
  print('5 - Tempo de execução do algoritmo de Floyd Warshall para todos aeroportos')
  print('0 - Exit')
  option = input('Digite a opção: ')
  return option

def menuEnglish():
  print('1 - List all airports')
  print('2 - Use dijkstra\'s algorithm to find the shortest path between two airports')
  print('3 - Generate the minimum spanning tree using prim\'s algorithm')
  print('4 - Use floyd warshall\'s algorithm to find the minimum distance between two airports')
  print('5 - Execution time floyd warshall\'s algorithm for all airports')
  print('0 - Exit')
  option = input('Enter the option: ')
  return option

def main():
  graph = create_graph()

  os.system('cls' if os.name == 'nt' else 'clear')
  print('1 - Menu em português')
  print('2 - Menu in english')
  language = input('1 ou 2: ')

  loop_condition = True
  os.system('cls' if os.name == 'nt' else 'clear')
  while loop_condition:
    if language == '1':
      option = menuPortuguese()
    else:
      option = menuEnglish()
    if option == '1':
      os.system('cls' if os.name == 'nt' else 'clear')
      airports = list_airports(graph)
      pp = pprint.PrettyPrinter(indent=8)
      pp.pprint(airports)
    elif option == '2':
      os.system('cls' if os.name == 'nt' else 'clear')
      try:
        airports = list_airports(graph)
        pp = pprint.PrettyPrinter(indent=8)
        pp.pprint(airports)
        if language == '1':
          input1 = input('Digite o primeiro aeroporto: ')
          input2 = input('Digite o segundo aeroporto: ')
        else:
          input1 = input('Enter the first airport: ')
          input2 = input('Enter the second airport: ')
        graph_algorithms.dijkstra(graph, input1)
        dijkstra_path = graph_algorithms.shortest_path_using_dijkstra(graph, input1, input2)
        if language == '1':
          print('\nO caminho mais curto é: \n')
          print(dijkstra_path[0])
          print('\ne a distância mínima é: ')
          print(dijkstra_path[1])
          print('')
          plot_graph_shortest_path(dijkstra_path[0], dijkstra_path[1])
          print('\n')
        else:
          print('\nThe shortest path is: \n')
          print(dijkstra_path[0])
          print('\nand the minimum distance is: ')
          print(dijkstra_path[1])
          print('')
          plot_graph_shortest_path(dijkstra_path[0], dijkstra_path[1])
          print('\n')
      except KeyError:
          print('This airport does not exist, enter a valid airport, please')
    elif option == '3':
      os.system('cls' if os.name == 'nt' else 'clear')
      try:
        airports = list_airports(graph)
        pp = pprint.PrettyPrinter(indent=8)
        pp.pprint(airports)
        if language == '1':
          input1 = input('Digite o aeroporto para gerar o MST (Minimum Spanning Tree) deste aeroporto: ')
        else:
          input1 = input('Enter the airport to generate the MST (Minimum Spanning Tree) from this airport: ')
        mst = graph_algorithms.mst(graph, input1)
        if language == '1':
          print('Este é um mst do aeroporto %s' % input1)
        else:
          print('This is a mst from airport %s' % input1)
        print(dict(mst))
        print('')
        print('-----------------------------------------------------------------------------------\n')
        for key in mst:
            cnt = 0
            print(key, end=': ')
            for value in mst[key]:
                cnt += 1
                if (cnt == len(mst[key])):
                    print(value)
                else:
                    print(value, end=' -> ')
            print('')
        if language == '1':
          print('O peso do MST do aeroporto %s' % input1 + ' é: ' + str(graph_algorithms.get_cost_of_mst(graph, input1)))
        else:
          print('The weight of the mst from airport %s' % input1 + ' is: ' + str(graph_algorithms.get_cost_of_mst(graph, input1)))
        print('\n')
      except KeyError:
        print('This airport does not exist, enter a valid airport, please')
    elif option == '4':
      os.system('cls' if os.name == 'nt' else 'clear')
      dist, pred = graph_algorithms.floyd_warshall(graph)
      airports = list_airports(graph)
      pp = pprint.PrettyPrinter(indent=8)
      pp.pprint(airports)
      if language == '1':
        input1 = input('Digite o primeiro aeroporto: ')
        input2 = input('Digite o segundo aeroporto: ')
      else:
        input1 = input('Enter the first airport: ')
        input2 = input('Enter the second airport: ')
      try:
        if language == '1':
          print('\nA minima distância entre ' + input1 + ' e ' + input2 + ' é: %f' % dist[input1][input2] + ' km')
        else:
          print('\nThe minimum distance between ' + input1 + ' and ' + input2 + ' is: %f' % dist[input1][input2] + ' km')
        print('\n')
      except KeyError:
        print('This airport does not exist, enter a valid airport, please')
    elif option == '5':
      os.system('cls' if os.name == 'nt' else 'clear')
      if language == '1':
        print('O tempo de execução do algoritmo de floyd warshall para todos o grafo é: ' + str(graph_algorithms.get_execution_time_floyd_warshall(graph)) + ' segundos\n')
      else:
        print('The execution time of floyd warshall\'s algorithm for all graph is: ' + str(graph_algorithms.get_execution_time_floyd_warshall(graph)) + ' seconds\n')
    elif option == '0':
      if language == '1':
        print('Obrigado!')
      else:
        print('Thank you!')
      loop_condition = False
    else:
      if language == '1':
        print('Digite um valor válido, por favor')
      else:
        print('Enter valid option [1, 2, 3, 4, 5, 0], please')


if __name__ == '__main__':
  main()
