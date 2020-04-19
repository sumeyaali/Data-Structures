# How do you find and return the middle node of a singly linked in one pass?
# Dont have to the length
# if length is even, return the first of the middle node
# Cant store nodes in another data structure


# Singly linked list goes in one direction
# Loop through array starting at the head, using a while loop as we dont know the length of the list
# Keep going through the list until you reach head.next is None

# After head.next is None, We've reached the tail
#We would be incrementing the size
# Size = length of the list

# 1 -> 2 -> 3 -> None
# size = 1
# size = 2
# size = 2
# middle = size // 2

#if size is even(that means there is an odd number of values):
 # return list (middle)
 # Otherwise: return list(middle -1 ) to get the first of the middle indices


# size = 0 # this is to keep track of length of array
# i = 0 # this is the starting index, head
# current_node = i # to keep track of the next node

# while current_node is not None:
#     current_node + 1
#     size += 1
# middle = size // 2
# return middle

_________________________________________________________________


# How do you reverse a singly linked list without recursion?
# You many not store the values in other data structures
# Dont make a new list 


# How to make the tail the head and the head the tail



# remove from tail and add to head
# 5 -> 1 -> 2 -> 3 -> 4 -> None 

# remove from tail
# set the tail to self.head.next
# 5 -> 4 -> 1 -> 2 -> 3 -> None


# set the tail to self.head.next
# 1 -> 2 -> 3 -> 4 -> 5 -> None 
# 5 -> 4 -> 3 -> 2 -> 1 -> None
