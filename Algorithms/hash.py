class hashValue:
  """A single node in a hash table"""
  def __init__(self, value):
    self.value = value
    self.next = None

class hashMap:
  """Implementation of hashing"""
  def __init__(self):
    self.list = [None]
    self.hashMapLen = len(self.list)
    self.count = 0

  def hash(self, value):
    # Using division hash method
    return value % self.hashMapLen

  def toList(self, log):
    retval = []
    for entry in self.list:
      if log:
        print "----------------------------" 
      node = entry
      while node is not None:
        retval.append(node.value)
        if log:
          print node.value 
        node = node.next
    return retval

  def tableDouble(self):
    tmp = self.toList(False)
    self.list = [None] * self.hashMapLen * 2
    self.hashMapLen = len(self.list)
    # print "Table doubled to ", self.hashMapLen
    self.insertListIntoHash(tmp)

  def insertElement(self, value):
    # print "Insert",value
    if self.count + 1 >= 0.75 * self.hashMapLen:
      # print "Table size is less, need to double"
      self.tableDouble()

    # print "Trying to insert", value
    key = self.hash(value)
    # print "Now inserting at:", key
    self.insertAt(key, value)
    self.count = self.count + 1

  def insertListIntoHash(self, valueList):
    for value in valueList:
      self.insertElement(value)

  def shrinkTable(self):
    tmp = self.toList(False)
    self.list = [None] * self.hashMapLen / 2
    self.hashMapLen = len(self.list)
    self.insertListIntoHash(tmp)

  def insertAt(self, key, value):
    value = hashValue(value)
    if self.list[key] is None:
      self.list[key] = value
    else:
      curr = self.list[key]
      nextValue = self.list[key].next
      while nextValue is not None:
        curr = curr.next
        nextValue = nextValue.next
      curr.next = value

  def deleteAt(self, key, value):
    if self.list[key].value is value:
      self.list[key] = self.list[key].next
    else:
      curr = self.list[key]
      nextValue = self.list[key].next
      while curr.value is not value:
        curr = curr.next
        nextValue = nextValue.next

      curr.value = nextValue.value
      curr.next = nextValue.next
      self.count = self.count -1

      if self.count <= 0.25 * self.hashMapLen:
        self.shrinkTable()

  def check(self, value):
    key = self.hash(value)
    node = self.list[key]
    while node is not None:
      if node.value is value:
        print "Found"
        return 
      node = node.next
    print "Not found"


myHash = hashMap()
myHash.insertElement(5)
myHash.insertElement(4)
myHash.insertElement(12)
myHash.insertElement(22)
myHash.insertElement(35)
myHash.insertElement(42)
myHash.insertElement(123)
myHash.insertElement(1231)
myHash.insertElement(2)
myHash.insertElement(31)
myHash.insertElement(2312)
myHash.insertElement(213)
myHash.insertElement(545)
myHash.insertElement(1245)
myHash.insertElement(1)
myHash.insertElement(56)
myHash.insertElement(69)
myHash.insertElement(81)

myHash.toList(True)

myHash.check(2312)

myHash.check(0)


