from collections import defaultdict
import heapq, time

def dijkstra(graph, _from, to=None):
  try:
    distances = {v: float('inf') for v in graph}
    distances[_from] = 0
    pq = [(0, _from)]
    pred = {}
    while len(pq) > 0:
      cd, cv = heapq.heappop(pq)
      if cd > distances[cv]:
        continue
      for u, w in graph[cv].items():
        distance = cd + w
        if distance < distances[u]:
          distances[u] = distance
          pred[u] = cv
          heapq.heappush(pq, (distance, u))
    return distances, pred
  except KeyError:
    print('This airport does not exist')

def shortest_path_using_dijkstra(graph, _from, to):
  try:
    d, p = dijkstra(graph, _from, to)
    pred = to
    path = []
    while pred != None:
      path.append(pred)
      pred = p.get(pred, None)
    path.reverse()
    path_map = {}
    for i, node in enumerate(path[:-1]):
      path_map[node] = path[i + 1]
    return path_map, d[to]
  except KeyError:
    print('This airport does not exist')

def floyd_warshall(graph):
  try:
    dist = {}
    pred = {}
    for u in graph:
      dist[u] = {}
      pred[u] = {}
      for v in graph:
        dist[u][v] = float('inf')
        pred[u][v] = -1
        dist[u][u] = 0
        for z in graph[u]:
          dist[u][z] = graph[u][z]
          pred[u][z] = u
    for k in graph:
      for i in graph:
        for j in graph:
          if dist[i][k] + dist[k][j] < dist[i][j]:
            dist[i][j] = dist[i][k] + dist[k][j]
    return dist, pred
  except KeyError:
    print('This airport does not exist')

def get_execution_time_floyd_warshall(graph):
  start = time.time()
  dist, pred = floyd_warshall(graph)
  end = time.time()
  return end - start

def mst(graph, start):
  mst = defaultdict(set)
  visited = set([start])
  edges = [
    (cost, start, to)
    for to, cost in graph[start].items()
  ]
  heapq.heapify(edges)
  while edges:
    cost, _from, to = heapq.heappop(edges)
    if to not in visited:
      visited.add(to)
      mst[_from].add(to)
      for to_next, cost in graph[to].items():
        if to_next not in visited:
          heapq.heappush(edges, (cost, to, to_next))
  return mst