"""
previous num can be found from subtracting the remaining numbers from the current largest num
process repeats and if at the end the result is an array containing only "1"s then the array is valid
% modulo operator is used to reduce the no of subtraction operations
use a heap to keep track of the largest value in the array

time complexity: O(nlg(n)) the loop will run at most n times, heap insertion/removal is lg(n)
space complecity: O(n) extra space needed for the heap
"""
def target_array(target_arr):
  from heapq import heappushpop, heapify

  heap = []
  total = 0
  for n in target_arr:
    total += n
    heap.append(-n)
  heapify(heap)

  # if largest value in the heap is 1, then the arr is valid
  while heap[0] < -1:
    largest = -heap[0]
    remainder = total - largest
    # remainder can be >= the largest value
    # smallest value of the remainder should be 1 which is the smallest possible value
    if remainder >= largest or remainder < 1:
      return False

    # use mod to find the value after subtracting remainder from largest the most times
    new_val = largest % remainder
    # smallest possible value should be 1
    # if new_val is 0 AND remainder is not 1 this operation is invalid
    if new_val == 0 and remainder != 1:
      return False
    heappushpop(heap, -new_val)
    total += new_val - largest
  return True


"""
when testing if nos are a multiple of another number there will be repeats, e,g
num = 100, factors = 2, 4, 5, 10, 20, 25, 50 --> 10x10, 5x20, 20x5
there is only a need to test up until sqrt(n)

any multiples of prime nos will not be considered prime
so the logic will be to create an array initializing all values to 1 (represents a prime no)
up till the sqrt of the num mark all multiples of prime nos as non prime
sum the array

time complexity: O(sqrt(n)*lg(lg(n)) outer loop runs sqrt(n) times each loop does n/i work to cross out non primes
dont really understand this one but you can google "sum of the reciprocals of prime numbers"
space complexity: O(n) to store the array of primes
"""
def no_primes(num):
  if num <= 2:
    return 0

  primes = [1]*num
  # 0 & 1 are non prime nos
  primes[0], primes[1] = 0, 0
  # only need to count multiples up to the sqrt of n
  for i in range(2, int(num**0.5)+1):
    if primes[i]:
      # mark non prime nos as 0
      for j in range(i*i, num, i):
        primes[j] = 0
  return sum(primes)
