import json, math
import gol_flights
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

def dfs(graph, visited, node):
  visited[node] = True
  for u in graph[node]:
    if u not in visited.keys():
      dfs(graph, visited, u)

def bfs(graph, _from, to):
  visited = {}
  queue = []
  parent = {}
  queue.append(_from)
  visited[_from] = True

  while queue:
    node = queue.pop(0)
    sp = []

    for u in graph[node]:
      if u not in visited.keys():
        if node not in queue:
          visited[u] = True
          queue.append(u)
          parent[u] = node
          if (u == to):
            return parent

def sp(parent, _from, to):
  sp = [to]
  while sp[-1] != _from:
    sp.append(parent[sp[-1]])
  sp.reverse()
  sp_map = {}
  for i, node in enumerate(sp[:-1]):
    sp_map[node] = sp[i + 1]
  return sp_map

def djikstra(graph, _from, to):
  

def plot_graph(path):
  G = nx.DiGraph()
  G.add_nodes_from(path.keys())
  for s in path.keys():
      G.add_edge(s, path[s])
  pos = nx.spring_layout(G)
  plt.figure(4,figsize=(20,10))

  nx.draw_networkx(
    G,
    pos = nx.spring_layout(G, k = 0.5, iterations = 25),
    font_color = 'r'
  )
  plt.show();

def main():
  graph = create_graph()
  path = bfs(graph, 'Santos Dumont', 'Leite Lopes')
  path = sp(path, 'Santos Dumont', 'Leite Lopes')
if __name__ == '__main__':
  main()


