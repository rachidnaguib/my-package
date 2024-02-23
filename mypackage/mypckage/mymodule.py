def top_n(items, n):
    '''Return the top n items in an array, in desc order.
    
    Args:
        items (array): list or array-like object
        n (int): num of items to return
        
    Return:
        array: top n items, in desc order
        
    Egs:
    >>> top_n([8, 3, 2, 7, 4], 3)
    [8, 7, 3]
    '''
    for i in range(n):  # Keep sorting until we have the top n items
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:  # If this item is bigger than the next item
                items[j], items[j + 1] = items[j + 1], items[j]  # Swap the two
                
    # Get the last n items
    top_n = items[-n:]
    
    # Return in descending order
    return top_n[::-1]

# Test the function
print(top_n([8, 3, 2, 7, 4], 3))  # Output: [8, 7, 3]


