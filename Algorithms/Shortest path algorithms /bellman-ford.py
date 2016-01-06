#Compute the shortest path from a single source to all other vertices
#Takes as input, a weighted graph. Outputs 
# - Dictionary D : Shortest path to each vertex
# - Partent P : Parent of each vertex in a shortest path

graph = {
  'a' : {'b' : 7, 'd' : 14, 'c' : 9 },
  'b' : {'a' : 7, 'c' : 10, 'f' : 15},
  'c' : {'a' : 9, 'b' : 10, 'd' : 2, 'f': 11},
  'd' : {'a' : 14, 'c' : 2, 'e' : 9},
  'e' : {'d' : 9, 'f' : 6},
  'f' : {'b' : 15, 'c': 11, 'e' : 6}
}


def bellman_ford(graph, source):
  if source not in graph:
    print "Source not present in the graph"
    return 

  distance = {
    source : 0
  }
  parent = {
    source : None
  }
  queue = []
  for vertex in graph:
    distance[vertex] = 9999999
    parent[vertex] = None
    queue.append(vertex)

  distance[source] = 0

  #Edge relaxations
  #Relax repeatedly as many vertices in the graph
  for vertex in graph:
    for vertex in graph:
      for adjVertex in graph[vertex]:
        temp = distance[vertex] + graph[vertex][adjVertex]
        if temp < distance[adjVertex]:
          distance[adjVertex] = temp


  #Negative weight cycle detection
  for vertex in graph:
    for adjVertex in graph[vertex]:
      temp = distance[vertex] + graph[vertex][adjVertex]
      if temp < distance[adjVertex]:
        print "negative weight edge detected"
        return 

  return (distance, parent)


(distance, parent) = dijkstra(graph, 'a')

print distance

print parent


