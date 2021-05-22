"""
Binary heaps are used a special kind of binary trees
they need to fulfill 2 properties
- complete tree --> all lvls except the last lvl need to be filled
- all vals of child node need to be smaller than parent node val for max heap, & larger for min heap

heaps can perform insertion & removal in worst case lg(n) time which is the height of the tree

can be implemented with a list due to the property of a complete tree
for a 1-indexed array, node at index P has left child at 2P and right child at 2P+1
appending new node at the end of list
replacing elements with last element of the list, both operations maintain the complete tree structure
up-heapify/down-heapify operations need to be done to satisfy the heap property
"""
class MinHeap:

  def __init__(self):
    # start with an empty root node so that indexing can be performed easier
    self.heap = [0]
    self.size = 0

  def insert(self, item):
    # insert using append preserves the complete tree property
    # but may not respect the ordered heap property
    # need to swap nodes till the heap is ordered
    self.heap.append(item)
    self.size += 1
    self.heapify_up(self.size)

  def heapify_up(self, i):
    while i // 2 > 0:
      if self.heap[i] < self.heap[i//2]:
        temp = self.heap[i//2]
        self.heap[i//2] = self.heap[i]
        self.heap[i] = temp
      i = i//2

  def remove(self):
    # remove the root node
    retval = self.heap[1]
    # replace with the smallest node
    self.heap[1] = self.heap.pop()
    self.size -= 1
    # swap nodes till ordering is preserved
    self.heapify_down(1)

    return retval

  def heapify_down(self, i):
    # check if we can still go down one lvl
    left = i * 2
    right = left + 1
    smallest = i

    if left <= self.size and self.heap[left] < self.heap[i]:
      smallest = left
    if right <= self.size and self.heap[right] < self.heap[i]:
      smallest = right

    if smallest != i:
      self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
      self.heapify_down(smallest)

