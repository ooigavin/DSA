class BinaryTree:

  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def set_left(self, val):
    if self.left:
      self.left = BinaryTree(val, left=self.left)
    else:
      self.left = BinaryTree(val)

  def set_right(self, val):
    if self.right:
      self.right = BinaryTree(val, right=self.right)
    else:
      self.right = BinaryTree(val)

def setup():
  a = BinaryTree('a')
  c = BinaryTree('c')
  e = BinaryTree('e')
  h = BinaryTree('h')
  d = BinaryTree('d', left=c, right=e)
  b = BinaryTree('b', left=a, right=d)
  i = BinaryTree('i', left=h)
  g = BinaryTree('g', right=i)
  f = BinaryTree('f', left=b, right=g)
  return f


"""
Pre-order traversal
- visits the root node first
- performs pre-order traversal on the left subtree followed by the right subtree 
"""

"""
if the curr node is valid, visit it first
else pop the next node off the stack to be visited
if the right child exists push it onto the stack to for later traversal
move to left child
"""
def preorder_iter(root):
  s = []
  curr = root
  while s or curr:
    if curr is None:
      curr = s.pop()
    print(curr.val)

    if curr.right:
      s.append(curr.right)

    curr = curr.left


# recursive
def preorder_rec(root):
  if root:
    print(root.val)
    preorder_rec(root.left)
    preorder_rec(root.right)


"""
In-order traversal
- visit the left subtree in order
- visit the root node
- visit the right subtree in order
"""

# recursive
def inorder_rec(root):
  if root:
    inorder_rec(root.left)
    print(root.val)
    inorder_rec(root.right)

"""
keep traversing the left side of the tree
if no child remains, pop the first node off the stack and visit it (left most leaf node)
move pointer to right child of that node
"""
def inorder_iter(root):
  s = []
  curr = root
  while len(s) > 0 or curr:
    if curr:
      s.append(curr)
      curr = curr.left
    else:
      curr = s.pop()
      print(curr.val)
      curr = curr.right


"""
Post-order traversal
- visit the left subtree in post order
- visit the right subtree in post order
- visit the root node

post-order traversal is used in deleting the nodes from a tree or in stack operations (AST)
"""
def postorder_rec(root):
  if root:
    postorder_rec(root.left)
    postorder_rec(root.right)
    print(root.val)


"""
node can only be popped off the stack after BOTH left & right child nodes hv been visited
the parent node will always be visited immediately after its right node
this property can be used to check if the right child node of  a particular node has been visited yet
"""
def postorder_iter(root):
  curr = root
  s = []
  last_visited = None
  while s or curr:
    if curr:
      s.append(curr)
      curr = curr.left
    else:
      # note that the node is not popped off the stack here
      # if the node has a right child, right node still needs to be visited first
      peeked = s[-1]
      if peeked.right and peeked.right != last_visited:
        curr = peeked.right
      else:
        print(peeked.val)
        last_visited = s.pop()


"""
Level-order traversal (BFS)
nodes in a tree are visited level by level

keep a 2 counts
curr_lvl: no of nodes to visit in the curr lvl
next_lvl: no of nodes to visit in the next lvl
dec and inc the counts accordingly
when the curr count reaches zero, lvl has been traversed
swap the curr and next counts
"""
def level_order(root):
  q = []
  if root:
    q.append(root)

  curr_lvl = 1
  next_lvl = 0
  ans = []
  lvl = []
  while q:
    node = q.pop(0)
    curr_lvl -= 1
    lvl.append(node.val)
    if node.left:
      next_lvl += 1
      q.append(node.left)
    if node.right:
      next_lvl += 1
      q.append(node.right)

    if curr_lvl == 0:
      ans.append(lvl)
      lvl = []
      curr_lvl, next_lvl = next_lvl, curr_lvl
  return ans
