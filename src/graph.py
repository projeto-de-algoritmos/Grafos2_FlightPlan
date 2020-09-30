import json, math
import gol_flights, graph_algorithms
import networkx as nx
import matplotlib.pyplot as plt
import pprint
import os

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
    font_color = 'r'
  )
  plt.show();  

def plot_graph_shortest_path(path, cost):
  G = nx.DiGraph()
  G.add_nodes_from(path.keys())
  for s in path.keys():
      G.add_edge(s, path[s])
  pos = nx.spring_layout(G)
  plt.figure(4,figsize=(20,7))
  nx.draw_networkx(
    G,
    pos = nx.spring_layout(G, k = 0.5, iterations = 25),
    font_color = 'r'
    
  )
  plt.text(0, 0.5, 'Minimum distance = %f' % cost + ' km')
  plt.show();  

def main():
  graph = create_graph()

  loop_condition = True
  os.system('cls' if os.name == 'nt' else 'clear')
  while loop_condition:
    print('1 - List all airports')
    print('2 - Use djikstra\'s algorithm to find the shortest path between two airports')
    print('3 - Generate the minimum spanning tree using prim\'s algorithm')
    print('4 - Use floyd warshall\'s algorithm to find the minimum distance between two airports')
    print('5 - Execution time floyd warshall\'s algorithm for all airports')
    option = input('Enter the option: ')
    if option == '1':
      airports = list_airports(graph)
      pp = pprint.PrettyPrinter(indent=8)
      pp.pprint(airports)
    elif option == '2':
      try:
        input1 = input('Enter the first airport: ')
        input2 = input('Enter the second airport: ')
        graph_algorithms.djikstra(graph, input1)
        djikstra_path = graph_algorithms.shortest_path_using_djikstra(graph, input1, input2)
        print('The shortest path and the minimum distance is:')
        print(djikstra_path[0], djikstra_path[1])
        plot_graph_shortest_path(djikstra_path[0], djikstra_path[1])
      except KeyError:
        print('This place does not exist, enter a valid place, please')
    elif option == '3':
      input1 = input('Enter the airport to generate the MST (Minimum Spanning Tree) from this airport: ')
      mst = graph_algorithms.mst(graph, input1)
      print('This is a mst from airport %s' % input1)
      print(dict(mst))
    elif option == '4':
      dist, pred = graph_algorithms.floyd_warshall(graph)
      input1 = input('Enter the first airport: ')
      input2 = input('Enter the second airport: ')
      try:
        print('The minimum distance between ' + input1 + ' and ' + input2 + ' is: %f' % dist[input1][input2] + ' km')
      except KeyError:
        print('This place does not exist, enter a valid place, please')
    elif option == '5':
      print('The execution time of floyd warshall\'s algorithm for all graph is: ' + str(graph_algorithms.get_execution_time_floyd_warshall(graph)) + ' seconds')
    elif option == '0':
      loop_condition = False


if __name__ == '__main__':
  main()


