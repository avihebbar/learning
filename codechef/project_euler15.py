gridsize = 21

ways = [ [0 for i in range(gridsize)] for j in range(gridsize) ]

for i in range(gridsize):
	ways[gridsize-1][i] = ways[i][gridsize-1] = 1

for i in range(gridsize-2, -1, -1):
	for j in range(gridsize-2, -1, -1):
		ways[i][j] = ways[i+1][j] + ways[i][j+1]

print ways[0][0]

