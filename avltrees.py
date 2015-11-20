import commands

class Tree(object):
  """docstring for Tree"""
  def __init__(self):
    self.left = None
    self.right = None
    self.data = None
    self.height = 0
    self.parent = None

f = open("output.dot", "w")
f.write("digraph g {\n")

def writeEntry(node):
  if node.left != None:
    text = '{} -> {};\n'.format(node.data, node.left.data)
    f.write(text)
    writeEntry(node.left)
  if node.right != None:
    text = '{} -> {};\n'.format(node.data, node.right.data)
    f.write(text) 
    writeEntry(node.right)

def showTree(root):
  writeEntry(root)
  f.write("}")
  f.close()
  commands.getoutput('dot -Tps output.dot -o out.ps')
  commands.getoutput('evince out.ps')

def insert(data, node):
  global parent 
  # print("Coming for something", data)
  if node is None:
    node = Tree()
    node.parent = parent
    # print("Creating a node")
  if node.data is None:
    # print ("inserting here", data)
    node.height = node.height + 1
    node.data = data
  elif node.data > data:
    parent = node
    # print ("going for left")
    node.left = insert(data, node.left)
  elif node.data <= data:
    parent = node
    # print ("going for right")
    node.right = insert(data, node.right)
  return node

root = Tree()
parent = None
# root.data = 6
# root.left = Tree()
# root.left.data = 2


insert(3, root)
insert(5, root)
insert(2, root)
insert(7, root)
insert(4, root)
insert(12, root)
# insert(11, root)
# insert(13, root)
# insert(6, root)
# insert(15, root)
# insert(22, root)
# insert(0, root)
# insert(3, root)
# insert(8, root)

showTree(root)


