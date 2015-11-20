# array = [10, 13, 2, 8, 9, 7, 1]
array = []
def min_heapify(array, i):
  left = 2*i - 1
  right = 2*i  
  largest = i-1
  # print array[largest], array[left], array[right]
  if (left < len(array) and array[left] < array[largest]):
    largest = left
  if (right < len(array) and array[right] < array[largest]):
    largest = right
  if (largest != i-1):
    (array[i-1], array[largest]) = (array[largest], array[i-1])
    min_heapify(array, largest+1)

  return


def remove_min(array):
  n = len(array)
  (array[0], array[n - 1]) = (array[n - 1], array[0]) 
  ret = array.pop()
  min_heapify(array, 1)
  return ret

def insert(array, item):
  array.append(item)
  print array
  index = len(array)/2
  while (index != 0):
    # print("calling again for", array[index])
    # print array
    min_heapify(array, index)
    index = index /2
  return

# middle = len(array) / 2 

# for i in range(middle, 0, -1):
#   min_heapify(array, i)

insert(array, 11)
insert(array, 12)# #insert
insert(array, 2)

# # #sort
n = len(array)
for i in range(0, n):
  print( remove_min(array) )




