knapsackSize = 165
weights = [0, 23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
benefits = [0, 92, 57, 49, 68, 60, 43, 67, 84, 87, 72]

# solution = 1
# 1
# 1
# 1
# 0
# 1
# 0
# 0
# 0
# 0

memo = [ [0 for i in range(len(weights)) ] for j in range(knapsackSize+1)]

for i in range(1, len(weights) ):
	for j in range(1, knapsackSize+1):
		if weights[i] > j:
			memo[i][j] = 0
		else:
			memo[i][j] = min( memo[i-1][j], memo[i][j - weights[i] ] + benefits[i] )

print memo[len(weights)][knapsackSize]