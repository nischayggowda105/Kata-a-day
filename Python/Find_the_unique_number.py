'''
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

'''

def find_uniq(arr):
    # your code here
    
    # Simple way to get count of each number in list.
    from collections import Counter
    
    # Counter dict
    num_count = Counter(arr)
    
    # Check for key having Value as 1.
    for key,value in num_count.items():
        if value == 1:
            return key
        else:
            continue
