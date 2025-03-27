class HashTable:
    def __init__(self):
        self.table = []

    def update(self, key):
        if not self.contain(key):
            self.table.append(key)

    def contain(self, key):
        for val in self.table:
            if val == key:
                return True
        return False

    def remove(self,key):
        for i,val in enumerate(self.table):
            if val == key:
                del self.table[i]
                return



class HashSet:
    def __init__(self):
        self.initial_capacity = 2096
        self.hash_table = [HashTable() for i in range(self.initial_capacity)]

    def add(self, key):
        hash_key = key%self.initial_capacity
        self.hash_table[hash_key].update(key)

    def remove(self,key):
        hash_key = key%self.initial_capacity
        self.hash_table[hash_key].remove(key)

    def contains(self,key):
        hash_key = key%self.initial_capacity
        return self.hash_table[hash_key].contain(key)