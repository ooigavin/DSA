"""
3 ways to solve this problem

1. sort the entire array and get element at len(arr)-k
time complexity: O(nlgn)

2. use a min heap & restrict heap size to k
removal & insertion of item to heap is lg(size of heap)
iterate thru each item n times
time complexity: O(nlgk) whr k shld be less than n

3. use a partitioning logic to sort individual elements into correct position
stop when partition value == len(arr)-k
avg time complexity: O(n)
worst case is when arr is sorted & k = len(arr) OR arr is reverse sorted & k = 1 --> O(n^2)
for full explanation watch, its alotta math -> https://www.youtube.com/watch?v=hGK_5n81drs
"""
def find_k_largest(nums, k):
  def _partition(arr, l, h):
    val = arr[h]
    i = l - 1
    while l < h:
      if arr[l] < val:
        i += 1
        arr[i], arr[l] = arr[l], arr[i]
      l += 1
    arr[h], arr[i+1] = arr[i+1], arr[h]
    return i+1

  p = _partition(nums, 0, len(nums)-1)
  k = len(nums) - k
  while p != k:
    if p > k:
      p = _partition(nums, 0, p-1)
    else:
      p = _partition(nums, p+1, len(nums)-1)
  return nums[p]
