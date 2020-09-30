from collections import defaultdict
import heapq, queue

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

def djikstra(graph, _from, to=None):
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
    print('This place does not exist')

def shortest_path_using_djikstra(graph, _from, to):
  try:
    d, p = djikstra(graph, _from, to)
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
    print('This place does not exist')

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