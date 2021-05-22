## 1. Construct Target Array With Multiple Sums
Given an array of integers target. From a starting array, A consisting of all 1's, you may perform the following procedure :
- let x be the sum of all elements currently in your array.
- choose index i, such that 0 <= i < target.size and set the value of A at index i to x.
- You may repeat this procedure as many times as needed.
```
Input: target = [9,3,5]
Output: true
Explanation: [1, 1, 1] -> [1, 3, 1] -> [1, 3, 5] -> [9, 3, 5]

Input: target = [1,1,1,2]
Output: false
Explanation: Impossible to create target array from [1,1,1,1].

Input: target = [8,5]
Output: true
Explanation:
[1,1] -> [1,2] -> [3,2] -> [3,5] -> [8,5]

Input: target = [1,1,10]
Output: false
```

## 2. Count Primes
Count the no of primes less than a non-negative integer n
```
Input: n = 10
Output: 4

Input: n = 10000
Output: 1229

Input: n = 1234567
Output: 95360
```