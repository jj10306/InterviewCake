# I have two registers: one for take-out orders, and the other for the other folks eating inside the cafe. 
#All the customer orders get combined into one list for the kitchen, where they should be handled first-come, first-served.

# Recently, some customers have been complaining that people who placed orders after them are getting their food first. Yikes—that's not good for business!

# To investigate their claims, one afternoon I sat behind the registers with my laptop and recorded:

# The take-out orders as they were entered into the system and given to the kitchen. (take_out)
# The dine-in orders as they were entered into the system and given to the kitchen. (dine_in)
# Each customer order as it was finished by the kitchen. (served_orders)
# Given all three lists, write a function to check that my service is first-come, first-served. All food should come out in the same order customers requested it.

# We'll represent each customer order as a unique integer.

# Check if we're serving orders first-come, first-served
def is_first_come_first_served(take_out, dine_in, served_orders):
    
    i, j = 0, 0
    
    while i + j < len(served_orders):
        if i < len(take_out) and take_out[i] == served_orders[i + j]:
            i += 1
        elif j < len(dine_in) and dine_in[j] == served_orders[i + j]:
            j += 1
        #if i and j are out of bounds OR if current element matches served_orders current element
        else:
            return False
    return True