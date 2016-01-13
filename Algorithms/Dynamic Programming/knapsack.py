knapsackSize = 10#165
weights = [0,2,3,5,7]#[0, 23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
benefits = [5,3,7,9]#[92, 57, 49, 68, 60, 43, 67, 84, 87, 72]

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

memo = [ [0 for i in range(knapsackSize+1) ] for j in range(len(weights))]
used = 0*[len(weights)]
for i in range(1, len(weights) ):
	for j in range(1, knapsackSize+1):
		if weights[i] > j:
			memo[i][j] = memo[i-1][j]
		else:
			memo[i][j] = max( memo[i-1][j], memo[i-1][j - weights[i] ] + benefits[i - 1] )

j = knapsackSize
i = len(weights) - 1

while i >= 1 and j >=	1:
	if memo[i-1][j] == memo[i][j]:
		print "0"
	else:
		print "1"
	i = i - 1
	j = j - 1

print memo
print memo[len(weights) - 1 ][knapsackSize]

