"""
2Sum problem
find the total no of unique pairs of values from an array of integers whose sum equals a target value
>>> two_sum([1,1,2,3,3,4,5], 6)
>>> [[3, 3], [2, 4], [1, 5]]

Solution:
- create dict of visited values and their counts (to handle the case whr n+n=target)
- iterate thru the arr, and check if the required value exists in the visited dict
- only add the curr val & req val to the ans if the curr val has not been visited before to prevent duplicates
- in the case whr n+n=target, a duplicate should be allowed, ONLY if the seen count == 1
- note that this check should be done at the start of the loop before the seen count is incremented

time:  O(N) --> only one pass of the array is required
space: O(N) --> max size of visited dict == N, max no of unique pairs == N/2
"""
def two_sum(arr, target):
  visited = {}
  ans = []
  for n in arr:
    r = target - n
    if r == n and visited.get(n, 0) == 1:
      ans.append([r, n])

    if n in visited:
      visited[n] += 1
    else:
      if r in visited:
        ans.append([r, n])
      visited[n] = 1

  return ans


"""
3Sum problem
find total no of unique 3-no values from an array of integers whose sum equals a target value
>>> [-1,2,2,2,-1,-4]
>>> [[-4,2,2],[-1,-1,2]]

Solution:
- sort arr
- iterate thru the arr of integers
- if curr val >= target, the loop can be broken as all subsequent values will be greater and can never sum to the target
- for each pass, create a left & right pointer at the ends of the remaining slice
- while the 2 pointers do not cross each other
  - if lp + rp > req_val (target-curr_val), move rp left as this will make the sum smaller
  - elif lp + rp < req_val, move lp right
  - else, the sum == req_val, add (curr_val,lp,rp) to ans, shift both lp & rp as there could be more solutions
  
time: O(N^2) --> 2 nested passes per element in arr (worst case)
space: O(N) --> all elements used to form unique triples
"""
def three_sum(arr, target):
  arr.sorted()
  size = len(arr)
  ans = []
  for i in range(size):
    if arr[i] > target:
      break
    # remove duplicate from 3 sum
    if i > 0 and arr[i] == arr[i-1]:
      continue

    lp = i+1
    rp = size-1
    # if size < 3 we will not enter the while loop and simply return an empty list
    while lp < rp:
      total = arr[lp] + arr[rp] + arr[i]
      if total > target:
        rp -= 1
      elif total < target:
        lp += 1
      else:
        ans.append([arr[i], arr[lp], arr[rp]])
        # remove duplicates in 2 sum problem
        while lp < rp and arr[lp] == arr[lp+1]:
          lp += 1
        while lp < rp and arr[rp] == arr[rp-1]:
          rp -= 1
        rp -= 1
        lp += 1

  return ans
