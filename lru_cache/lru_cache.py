from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.amount_of_nodes = 0
        self.list = DoublyLinkedList
        self.storage = dict()



    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # Check does key exist in list
        # If key does exist, check if key is head, return self.head
        # if key is not self.head, iterate through list and return key:value pair that matches the current node
        if key not in self.storage:
            return None
        else:
            #Key is in cache
            node = self.storage[key] 
            self.list.move_to_end(node)
            return node.value[1]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # Check to see if key already exists
        if key in self.storage:
            # Override the key and add the value, value is inside of node
            node = self.storage[key]
            node.value =(key,value)
            #move to tail, most recent
            self.list.move_to_end(node)
            return
        # We need ot check to see if the capacity has been reached
        if len(self.list) == self.limit:
        # If we reached capacity, we need to delete head
            current_head = self.list.head.value[0] 
            del self.storage[current_head]
            self.list.remove_from_head()
        # If capacity hasnt been reached, add to tail
        self.list.add_to_tail((key,value))
        # Add to storage
        self.storage[key] = self.list.tail
