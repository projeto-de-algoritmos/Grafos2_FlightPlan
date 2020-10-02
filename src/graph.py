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

def main():
  graph = create_graph()

  loop_condition = True
  os.system('cls' if os.name == 'nt' else 'clear')
  while loop_condition:
    print('1 - List all airports')
    print('2 - Use dijkstra\'s algorithm to find the shortest path between two airports')
    print('3 - Generate the minimum spanning tree using prim\'s algorithm')
    print('4 - Use floyd warshall\'s algorithm to find the minimum distance between two airports')
    print('5 - Execution time floyd warshall\'s algorithm for all airports')
    print('0 - Exit')
    option = input('Enter the option: ')
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
        input1 = input('Enter the first airport: ')
        input2 = input('Enter the second airport: ')
        graph_algorithms.dijkstra(graph, input1)
        dijkstra_path = graph_algorithms.shortest_path_using_dijkstra(graph, input1, input2)
        print('\nThe shortest path is: \n')
        print(dijkstra_path[0])
        print('\nand the minimum distance is: ')
        print(str(dijkstra_path[1]) + ' km')
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
        input1 = input('Enter the airport to generate the MST (Minimum Spanning Tree) from this airport: ')
        mst = graph_algorithms.mst(graph, input1)
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
        print('The weight of the mst from airport %s' % input1 + ' is: ' + str(graph_algorithms.get_cost_of_mst(graph, input1)) + ' km')
        print('\n')
      except KeyError:
        print('This airport does not exist, enter a valid airport, please')
    elif option == '4':
      os.system('cls' if os.name == 'nt' else 'clear')
      dist, pred = graph_algorithms.floyd_warshall(graph)
      airports = list_airports(graph)
      pp = pprint.PrettyPrinter(indent=8)
      pp.pprint(airports)
      input1 = input('Enter the first airport: ')
      input2 = input('Enter the second airport: ')
      try:
        print('\nThe minimum distance between ' + input1 + ' and ' + input2 + ' is: %f' % dist[input1][input2] + ' km')
        print('\n')
      except KeyError:
        print('This airport does not exist, enter a valid airport, please')
    elif option == '5':
      os.system('cls' if os.name == 'nt' else 'clear')
      print('The execution time of floyd warshall\'s algorithm for all graph is: ' + str(graph_algorithms.get_execution_time_floyd_warshall(graph)) + ' seconds\n')
    elif option == '0':
      print('Thank you!')
      loop_condition = False
    else:
      print('Enter valid option [1, 2, 3, 4, 5, 0], please')


if __name__ == '__main__':
  main()
