'''
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
'''


def high(x):
    # Code here
    
    import string
    
    # dict for alphabet with score.
    alpha_dict = dict(zip(string.ascii_lowercase, range(1,27)))    
    
    # list of words.
    word_list = x.split()
    
    # To score each word in word_list
    score_word = []
    for word in word_list:
        temp = 0
        
        # To get score for each letter in a word.
        for letter in word:
            temp += int(alpha_dict[letter])
            
        score_word.append(temp)
        
        # To get index of Highest Score word in wordlist
    return word_list[score_word.index(max(score_word))]
