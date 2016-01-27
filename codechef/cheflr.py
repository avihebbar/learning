noTestCases = int(raw_input())

while noTestCases:
	pattern = raw_input()

	N = len(pattern)
	flag = 0
	result = 1
	for char in pattern:
		if not flag:
			if char is "l":
				result = result * 2
			else:
				result = result * 2 + 2
			flag = 1
		else:
			if char is "l":
				result = result * 2 - 1
			else:
				result = result * 2 + 1
			flag = 0

	print result % 1000000007
	noTestCases = noTestCases -1

	# alreadyOverNumbers = 0
	# for i in range(N-2, -2 , -2):
	# 	alreadyOverNumbers = alreadyOverNumbers + pow(2, i)

	# numPos = 1
	# for char in pattern:
	# 	numPos = numPos * 2
	# 	if char is "r":
	# 		numPos = numPos + 1

	# prevTreeSize = pow(2, N) - 1

	# posInLevel = numPos - prevTreeSize

	# alreadyOverNumbers = alreadyOverNumbers + posInLevel 

	# if N+1 % 2 == 0:
	# 	print int(2 * alreadyOverNumbers) % 1000000007
	# else:
	# 	print int(2 * alreadyOverNumbers - 1) % 1000000007