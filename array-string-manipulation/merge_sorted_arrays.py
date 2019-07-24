# We have our lists of orders sorted numerically already, in lists. 
# Write a function to merge our lists of orders into one sorted list.

# Combine the sorted lists into one large sorted list
def merge_lists(my_list, alices_list):

    res = []
    i = 0
    j = 0
    
    while i < len(my_list) and j < len(alices_list):
        if my_list[i] < alices_list[j]:
            res.append(my_list[i])
            i += 1
        else:
            res.append(alices_list[j])
            j+= 1
            
    while i < len(my_list):
        res.append(my_list[i])
        i += 1
    while j < len(alices_list):
        res.append(alices_list[j])
        j+= 1
        
        
    return res

# TODO: write solution to handle sorting n sorted arrays