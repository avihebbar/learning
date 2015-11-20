vertices = [
  {
    exploered : false,
    edges : [0, 1] 
  },
  {
    exploered : false,
    edges:[1, 3, 7]
  },
  {
    exploered : false,
    edges:[0, 2, 7]
  },
  {
    exploered : false,
    edges:[2, 4, 6]
  },
  {
    exploered : false,
    edges:[3, 4, 5]
  },
  {
    exploered : false,
    edges:[6, 5]
  }
]

edgesList = [
  {
    vertices:[0,2]
  },
  {
    vertices:[0,1]
  },
  {
    vertices:[2,3]
  },
  {
    vertices:[1,4]
  },
  {
    vertices:[3,4]
  },
  {
    vertices:[4,5]
  }
  {
    vertices:[3,5]  
  },
  {
    vertices:[2,1]
  }
]

starting_vertex = 0

queue = []
queue.push(starting_vertex)

vertices[starting_vertex].exploered = true

while queue.length isnt 0
  curr_vertex = ( queue.shift() )
  console.log "Current Vertex:"+ curr_vertex
  edges = vertices[ curr_vertex ].edges
  # console.log "Edges to that: "+edges
  for edge in edges
    for vertex in edgesList[edge].vertices
      # console.log "Edge: #{edge} : #{vertex}"
      if not vertices[vertex].exploered and vertex isnt curr_vertex
        queue.push(vertex)
        vertices[vertex].exploered = true
  # console.log "queue :#{queue}"