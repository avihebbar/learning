N = 5
K = 3
 
arr = [1,2,3,1,1]

nonDecreasingCount = 0
decreasingCount = 0

# -Get first K onto the list
# - Compute the counts
# - pop the first one out
# - append the popped one from the parent list
# - Compute again
# - Repeat

window = arr[0:K]

arr = arr[K:N]

for i in range(0, K-1):
	if window[i] == window[i+1]:
		nonDecreasingCount = nonDecreasingCount + 1
		decreasingCount = decreasingCount + 1
	elif window[i] > window[i+1]:
		decreasingCount = decreasingCount + 1
	else:
		nonDecreasingCount = nonDecreasingCount + 1


while 1:
	print nonDecreasingCount -decreasingCount
	if arr:
		#Ananlyze the effect of removal of first item
		if window[0] == window[1]:
			nonDecreasingCount = nonDecreasingCount - 1
			decreasingCount = decreasingCount - 1
		elif window[0] < window[1]:
			nonDecreasingCount = nonDecreasingCount - 1
		else:
			decreasingCount = decreasingCount - 1
		
		window.remove(window[0])
		window.append(arr[0])
		arr.remove(arr[0])
		
		#Analyze the effect of removal of last item
		if window[K-2] == window[K-1]:
			nonDecreasingCount = nonDecreasingCount + 1
			decreasingCount = decreasingCount + 1
		elif window[K-2] < window[K-1]:
			nonDecreasingCount = nonDecreasingCount + 1
		else:
			decreasingCount = decreasingCount + 1
	else:
		break
