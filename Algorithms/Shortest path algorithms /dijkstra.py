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

	distanceQueue =distance.copy()
	#Edge relaxations
	while queue:
		u = min(distanceQueue) 
		print "Vertex with minimum distance is : ", u
		queue.remove(u)
		for adjVertex in graph[u]:
			temp = distance[u] + graph[u][adjVertex]
			if temp < distance[adjVertex]:
				"Found better distance for %c as %d rather than %d" %(adjVertex, temp, distance[adjVertex] )
				distance[adjVertex] = temp
				parent[adjVertex] = u

		del distanceQueue[u]

	return (distance, parent)


(distance, parent) = dijkstra(graph, 'a')

print distance

print parent


