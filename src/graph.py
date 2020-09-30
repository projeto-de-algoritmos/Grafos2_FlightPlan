import json, math
import gol_flights, graph_algorithms
import networkx as nx
import matplotlib.pyplot as plt

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
  path = graph_algorithms.bfs(graph, 'Santos Dumont', 'Leite Lopes')
  path = graph_algorithms.sp(path, 'Santos Dumont', 'Leite Lopes')
# minimum spanning tree  
  mst = graph_algorithms.mst(graph, 'Santos Dumont')
  print(mst)
# djikstra
  graph_algorithms.djikstra(graph, 'Santos Dumont')
  djikstra_path = graph_algorithms.shortest_path_using_djikstra(graph, 'Santos Dumont', 'Leite Lopes')
  plot_graph_shortest_path(djikstra_path[0], djikstra_path[1])

if __name__ == '__main__':
  main()


