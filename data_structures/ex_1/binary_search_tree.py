class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    cb(self.value) # invoke cb with self

    if self.left: # left
      self.left.depth_first_for_each(cb)

    if self.right: # right
      self.right.depth_first_for_each(cb)


  def breadth_first_for_each(self, cb):
    queue = [] # setup a que to check nodes
    queue.append(self) # first/root node

    while len(queue):
      current = queue.pop(0) # first in que pulled out
      if current.left is not None: # if left, put in tree
        queue.append(current.left)
      if current.right is not None: # elif, put in right branch
        queue.append(current.right)
      cb(current.value) # call's current node and repeats while loop

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
