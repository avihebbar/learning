#Compute the shortest path from a single source to all other vertices
#Takes as input, a weighted graph. Outputs 
# - Dictionary D : Shortest path to each vertex
# - Partent P : Parent of each vertex in a shortest path

graph = {
	'a' : {'b' : 7, 'd' : 14, 'c' : 9 },
	'b' : {'a' : 7, }
}


def dijkstra(graph, source):
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
	while queue:
		u = min(distance)
		print "Vertex with minimum distance is : ," u
		queue.remove(u)

		for adjVertex in graph[u]:
			temp = distance[u] + graph[u][adjVertex]
			if temp < distance[adjVertex]:
				"Found better distance for %c as %d rather than %d" %(adjVertex, temp, distance[adjVertex] )
				distance[adjVertex] = temp
				parent[adjVertex] = u
  
  return distance, parent




