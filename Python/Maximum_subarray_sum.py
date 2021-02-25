'''
25/02/2021
5 kyu
Maximum subarray sum

The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]

Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. 
If the list is made up of only negative numbers, return 0 instead.

'''
def max_sequence(arr):
	
    # If len is 0, return 0.
    if len(arr) == 0:
        return 0
    
    else:
        # form a list of 0 for len of arr. 
        dp = [0 for i in range(len(arr))]
        
        dp[0] = arr [0]
        
        # Check if value increases for every sum.
        for i in range(1, len(arr)):
            dp[i] = max(dp[i-1] + arr[i], arr[i])
        
        # if max is negative, return 0.
        if max(dp) < 0:
            return 0
        
        return max(dp)

