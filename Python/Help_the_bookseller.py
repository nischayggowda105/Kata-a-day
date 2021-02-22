'''
A bookseller has lots of books classified in 26 categories labeled A, B, ... Z. Each book has a code c of 3, 4, 5 or more characters. The 1st character of a code is a capital letter which defines the book category.

For example an extract of a stocklist could be:

L = {"ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"}
M = {"A", "B", "C", "W"} 

result - 
(A : 20) - (B : 114) - (C : 50) - (W : 0)
'''





def stock_list(listOfArt, listOfCat):
    ....
        if len(listOfArt) == 0 or len(listOfCat) == 0:
        return ''

    # declare dict - books
    books = {}
    
    result = []
    
    title = []
    num = []
    
    # Get Book title and count.
    for Art in listOfArt:
        title = Art.split()[0]     
        num = Art.split()[1]
        
        # category wise count of books
        if title[0] in books:
            books[title[0]] += int(num)
        else:
            books[title[0]] = int(num)
    
    for Cat in listOfCat:
        if Cat in books:
            number = books[Cat]
        else:
            number = 0
        result.append(f'({Cat} : {number})')
    
    return ' - '.join(result)
