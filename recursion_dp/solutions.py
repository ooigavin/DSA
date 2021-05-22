def longest_common_subsequence(s1, s2):
  """
  problem can be broken down into 2 cases
  1. the compared chars match: both char can be removed & the remaining string is compared
  eg: lcs('hello', 'hallo') = 1 + lcs('ello', 'allo')

  2. the compared chars dont match: remove either of the chars and take the largest result
  eg: lcs('hello', 'goodbye') = max(lcs('hello', 'oodbye'), lcs('ello', 'goodbye'))

  if done recursively
  time complexity: O(2^n) exponential worst case whr the strings dont match at all -> 'AAA' VS 'BBB'

  if done using dp saving the results in a grid
  time complexity: O(mn) as
  space complexity: O(mn) is the size of the grid
  """
  grid = [
    [0 for _ in range(len(s1)+1)]
    for _ in range(len(s2)+1)
  ]
  # fill up the grid
  for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
      if s1[i-1] == s2[j-1]:
        grid[j][i] = 1 + grid[j-1][i-1]
      else:
        grid[j][i] = max(grid[j-1][i], grid[j][i-1])
  # grid[j][i] gives the len of the longest sub sequence

  # visualise grid
  # print(f'_ [_, {", ".join(ch for ch in s1)}]')
  # for idx, row in enumerate(grid):
  #   ch = s2[idx-1] if idx > 0 else '_'
  #   print(f'{ch} {row}')

  # follow the path to find the longest subsequence
  ans = ''
  i, j = len(s1), len(s2)
  while i > 0 and j > 0:
    # if they match, the path goes diagonally upwards
    if s1[i-1] == s2[j-1]:
      ans = s1[i-1] + ans
      i -= 1
      j -= 1
    # else move to the highest value in the grid, either up or to the left
    elif grid[j-1][i] > grid[j][i-1]:
       j -= 1
    else:
      i -= 1
  return ans
