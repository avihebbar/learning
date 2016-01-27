N = 5
K = 3
 
arr = [1,2,3,1,1]

count = {
	'+' : 0,
	'-' : 0
}

window = arr[0:K]

arr = arr[K:N]

diffArray = []
subSequenceRangeLengths = []

for i in range(0, K-1):
	if window[i] == window[i+1]:
		diffArray.append('=')
	elif window[i] > window[i+1]:
		diffArray.append('-')
	else:
		diffArray.append('+')

def subRanges(i):
	retVal = 0
	for j in range(i, 0 ,-1):
		retVal = retVal + j
	return retVal

subSequenceRange = 1
equalSequenceLength = 0

for i in range( 1, len(diffArray) ):
	if diffArray[i] == '=':
		equalSequenceLength = equalSequenceLength + 1
	elif diffArray[i] != diffArray[ i-1 ]:
		subSequenceRangeLengths.append( subSequenceRange )
		count[ diffArray[ i - 1 ] ] = subRanges(subSequenceRange)
		subSequenceRange = 1
	subSequenceRange = subSequenceRange + 1

while 1:
	print count['+'] - count['-']
	if arr:
		#Ananlyze the effect of removal of first item
		opType = diffArray[0]
		count[opType] = count[opType] - subSequenceRangeLengths[0]
		subSequenceRangeLengths[0] = subSequenceRangeLengths[0] - 1
		if subSequenceRangeLengths[0] == 0:
			subSequenceRangeLengths.remove( subSequenceRangeLengths[0] )

		window.remove(window[0])
		window.append(arr[0])
		arr.remove(arr[0])
		
		#For equal ranges it screws :(
		#Analyze the effect of removal of last item
		if window[K-2] == window[K-1]:
			subSequenceRangeLengths[-1] = subSequenceRangeLengths[-1] + 1
		elif window[K-2] < window[K-1]:
			subSequenceRangeLengths[-1] = subSequenceRangeLengths[-1] + 1
		else:
	else:
		break
