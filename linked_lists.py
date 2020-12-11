class Node:

  def __init__(self, val, next=None, prev=None):
    self.next = next
    self.val = val
    self.prev = prev

  def display(self):
    res = [str(self.val)]
    node = self
    while node.next is not None:
      res.append(str(node.next.val))
      node = node.next
    print(' '.join(res))

def setup():
  e = Node(5)
  d = Node(4, e)
  c = Node(3, d)
  b = Node(2, c)
  return Node(1, b)


"""
remove the nth node from the tail of a singly linked list & return the head

Solution:
- use 2 pointers to save a sliding window of n-nodes
- move window until right most pointer has no next node

time: O(N)
space: n, only need to store n-nodes in the window
"""
def remove_n(head, n):
  # assuming that the n will always lie within the list
  # add a dummy node to account for single and double length lists
  # need to return dummy.next instead of head, in the case whr head is the node that is removed
  dummy = Node(0)
  rp = lp = dummy
  for _ in range(n):
    rp = rp.next

  while rp.next is not None:
    rp = rp.next
    lp = lp.next
  lp.next = lp.next.next
  return dummy.next



"""
find out if the list is a circularly linked list
given the first node of the list
"""
def check_circular_list(node):
  next_node = node.next
  # while next_node.next:
  for i in range(10):
    print(f'\ncurrent: {node.val}\nnext: {next_node.val}')
    # check if vals same
    if next_node.val == node.val:
      return True
    # increment both nodes
    # print(f'initial next: {node.next.val}')
    node = node.next
    # print(f'new next: {node.next.val}')
    next_node = next_node.next.next

  return False


"""
reverse the order of a linked list
"""
def rev_list(node):
  curr_node = node
  prev_node = None
  next_node = None

  # terminate when the next node is None (tail)
  while curr_node:
    # set next_node to curr_node.next
    next_node = curr_node.next
    # set curr_node.next = prev_node
    curr_node.next = prev_node
    # set prev_node to curr_node
    prev_node = curr_node
    # set curr_node to next_node
    curr_node = next_node

  return prev_node.val
