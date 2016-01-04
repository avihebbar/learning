class node(object):
  """docstring for node"""
  def __init__(self, value):
    super(node, self).__init__()
    self.value = value
    self.next = None

t = node(3)
s = node(4)
t.next = s

r = node(5)

curr = t
nextNode = t.next
while nextNode is not None:
  print "Node value",curr.value
  curr = curr.next
  nextNode = nextNode.next

curr.next = r

curr = t
while curr is not None:
  print curr.value
  curr = curr.next


# # Prints 5
# nextNode = r
# print nextNode.value

# # Prints 4
# nextNode = r
# print t.next.value
  