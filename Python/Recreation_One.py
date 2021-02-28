
'''
28/02/2021

5 kyu
Integers: Recreation One

Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764. The sum of the squared divisors is 2500 which is 50 * 50, a square!

Given two integers m, n (1 <= m <= n) we want to find all integers between m and n whose sum of squared divisors is itself a square. 42 is such a number.

The result will be an array of arrays or of tuples (in C an array of Pair) or a string, each subarray having two elements, first the number whose squared divisors is a square and then the sum of the squared divisors.

Examples:
list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42, 2500], [246, 84100]]

'''

def list_squared(m, n):
    # your code
    import math
    
    list_numb = []
    for num in range(m, n+1):  
        sq_list = []
        list_div = []
        
        
        # Each number iteration
        for i in range(1, num+1):
            if num % i == 0:
                list_div.append(i)
                    
        sq_sum = sum([numb*numb for numb in list_div])
        
        # To check for perfect square
        if math.sqrt(sq_sum) % 1 == 0: # No decimal part for perfect square
            list_numb.append([num, sq_sum])
    
    return list_numb


