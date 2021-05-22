import random

def rand_arr(size):
  return [random.randint(0,99) for i in range(size)]

"""
Quick sort
finds a pivot value in the array
sorts the pivot value into its final position
recursively sorts the left & right portions of the array
sorts the array in place

worst case: O(n^2) reverse sorted array
average/best case: O(nlogn)
average space complexity: O(logn)
worst case space: O(n) n recursive calls for the worst case scenario
"""
def partition(arr, l, h):
  p = arr[h]
  i = l - 1
  while l < h:
    if arr[l] < p:
      i += 1
      arr[i], arr[l] = arr[l], arr[i]
    l += 1
  arr[i+1], arr[h] = arr[h], arr[i+1]
  return i + 1

def quick(arr):
  def _quick(arr, l, h):
    if l > h:
      return arr
    p = partition(arr, l, h)
    _quick(arr, l, p-1)
    _quick(arr, p+1, h)
    
  _quick(arr, 0, len(arr)-1)


"""
Merge Sort
recursively splits the array into smaller sub arrays
base case is when sub array is holding less than 2 elements & is sorted by definition
sub arrays are then merged in sorted order from the bottom up

average/best case: O(nlogn)
space complexity: O(n)
space used in each lvl is S(n), S(n/2), S(n/4) for logn lvls, max space used at bottom of call stack is 2n --> S(n) 
"""
def merge(arr):
  if len(arr) < 2:
    return arr
  # split & sort the sub array
  split = len(arr)//2
  l = merge(arr[:split])
  r = merge(arr[split:])

  # merge the sorted sub arrays
  new_arr = []
  i = j = 0
  while i < len(l) and j < len(r):
    if l[i] < r[j]:
      new_arr.append(l[i])
      i += 1
    else:
      new_arr.append(r[j])
      j += 1

  # add the remainder of the left over sub array
  if i < len(l):
    new_arr.extend(l[i:])
  else:
    new_arr.extend(r[j:])
  return new_arr


"""
Bubble sort
making passes along the list, bubbling items that are greater up the list
each pass will bubble the largest val to the top of the list
worst case complexity of n^2 as n operations for n passes are required
"""
def bubble(arr):
  # iterate  from the start to a decreasing end index
  # bubble the largest value per pass to the end of the list
  for i in range(len(arr)-1, 0, -1):
    for j in range(i):
      # for every pass compare adjacent elements and swap them
      if arr[j] > arr[j+1]:
        arr[j], arr[j + 1] = arr[j+1], arr[j]


"""
Selection sort
does one exchange per pass
iterates thru the array 
per pass, finds the smallest element with respect to the current element and swaps them

average/best/worst time complexity: O(n^2)
space complexity: O(1)
"""
def selection(arr):
  size = len(arr)
  for curr_index in range(size):
    # set the smallest element as the current index (no swap)
    smallest_index = curr_index
    # iterate thru the remainder of the array and find the smallest element
    for i in range(curr_index, size):
      if arr[i] < arr[smallest_index]:
        smallest_index = i
    # swap the elements
    arr[curr_index], arr[smallest_index] = arr[smallest_index], arr[curr_index]


"""
insertion sort
maintains a sorted sublist, shifts the next element down the sorted list until it finds its slot

average/worst time complexity: O(n^2)
space complexity: O(1)
"""
def insertion(arr):
  for i in range(1, len(arr)):
    p1 = i
    while p1 > 0:
      if arr[p1-1] > arr[p1]:
        arr[p1], arr[p1-1] = arr[p1-1], arr[p1]
        p1 -= 1
      else:
        break
  return arr
