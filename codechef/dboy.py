noTestCases = int(raw_input())

while noTestCases:
	N = int(raw_input())
	dist = [ int(x) for x in raw_input().split()  ]
	weights = [int(x) for x in raw_input().split() ]
	weights = [0] + weights
	 # [1, 4, 5, 3]dboy
# weights = [0, 1, 4, 5, 3]
# N = 10

	arr = [[9999999999 for i in range(len(weights))] for i in range(501)]

	arr[0][0] = 0

	for i in range(501):
		for j in range(1, len(weights)):
			if i >= weights[j]:
				arr[i][j] = min( arr[i][j-1], 1 + arr[i - weights[j] ][j]  )
			else:
				arr[i][j] = arr[i][j-1]

	sum = 0
	for d in dist:
		sum = sum + arr[2 * d][len(weights) - 1]

	print sum
	noTestCases = noTestCases - 1
# for i in range(N+1):
# 	for weight in weights:
# 		print weight, arr[i]
# 		if i % weight is 0:
# 			arr[i] = min( i / weight, arr[i] )

# for i in range(1, N+1):
# 	for j in range (i - 1, -1, -1):
# 		print arr[i], arr[j], arr[i-j]
# 		arr[i] = min(arr[i], arr[j] + arr[i - j] )

