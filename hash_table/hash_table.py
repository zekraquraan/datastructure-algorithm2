
from linked_list.linked_list import Node, LinkedList

class Hashtable:
    def __init__(self, size=1024):
        self._size = size
        self._buckets = [None] * size
        self._keys = []

    def _hash(self, key):
        '''
           method to return the hash code for a given key

           argument : key

           return : hash code for the key "Index"
        '''
        hash_total = sum([ord(i) for i in key])
        return (hash_total * 211) % self._size

    def set(self, key, value):
        '''
          set a key-value pair in the bucket, handling a collasions
          as needed

          arg : key to be hashed and used as an identifier
              for the value
                value that associated with the key
        '''
        hashed_key = self._hash(key)

        if not self._buckets[hashed_key]:
            self._buckets[hashed_key] = LinkedList()
        self._keys.append(key)
        self._buckets[hashed_key].insert((key, value))

    def get(self, key):
        hashed_key = self._hash(key)

        bucket = self._buckets[hashed_key]

        current = bucket.head
        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current.next

    def has(self, key):
        """
           method to check if the given key exist in the hash table
           arg : key
           returns "boolean --> true Or false"
        """
        hashed_key = self._hash(key)

        bucket = self._buckets[hashed_key]

        if not bucket == None:
            current = bucket.head
            while current:
                if current.value[0] == key:
                    return True
                current = current.next
        return False

    def keys(self):
        '''
        return a list of all keys presents in the hash_table
        '''
        return self._keys
    
   
    
=======
from functools import reduce
from operator import add

class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

class HashTable:
    def __init__(self, size=1024):
        self.__size = size
        self.__buckets = [None] * size
        self.__keys_set = set()

    def __hash(self, key):
        return reduce(add, [ord(str(char)) for char in key]) * 283 % self.__size

    def set(self, key, value):
        index = self.__hash(key)
        if self.__buckets[index] is None:
            ll = LinkedList()
            self.__buckets[index] = ll

        self.__buckets[index].insert([key, value])
        self.__keys_set.add(key)

    def get(self, key):
        index = self.__hash(key)
        bucket = self.__buckets[index]
        if bucket is not None:
            curr = bucket.head
            while curr:
                if curr.value[0] == key:
                    return curr.value[1]
                curr = curr.next
        return None

    def has(self, key):
        return key in self.__keys_set

    def keys(self):
        return list(self.__keys_set)

