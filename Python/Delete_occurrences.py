'''
24/02/2021

6 kyu
Delete occurrences of an element if it occurs more than n times

Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering. 
For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 
1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].

Example

  delete_nth ([1,1,1,1],2) # return [1,1]

  delete_nth ([20,37,20,21],1) # return [20,37,21]

'''

def delete_nth(order,max_e):
    # code here
    
    from collections import defaultdict
    # dict and list
    count = defaultdict(int)
    delete = []
    for i, v in enumerate(order):
        # Populate the dict with count of each element in list.
        count[v] += 1
        # Element having more then max_e count, append to delete list. 
        if count[v] > max_e:
            print(i)
            delete.append(i)
    
    for i in reversed(delete):
        # pop the coressponding index values.
        order.pop(i)
    
    return order
