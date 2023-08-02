class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, key, value):
        new_node = Node(key, value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


class Hashtable:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [LinkedList() for temp in range(self.size)]

    def hash(self, key):
        key = str(key)
        return sum(ord(char) for char in key) % self.size

    def set(self, key, value):
        index = self.hash(key)
        bucket = self.buckets[index]
        current = bucket.head
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next
        bucket.append(key, value)

    def get(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        current = bucket.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def has(self, key):
        if self.get(key):
            return True
        return False

    def keys(self):
        keys = set()
        for bucket in self.buckets:
            current = bucket.head
            while current:
                keys.add(current.key)
                current = current.next
        return list(keys)