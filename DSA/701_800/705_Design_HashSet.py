class MyHashSet:
    # array + linked list
    def __init__(self):
       self.buckets = 1003
       self.table = [[] for _ in range(self.buckets)]
    
    def hash(self, key:int) -> int:
        return key % self.buckets

    def add(self, key: int) -> None:
        hashed_key = self.hash(key)
        if key in self.table[hashed_key]:
            return 
        else:
            self.table[hashed_key].append(key)

    def remove(self, key: int) -> None:
        hashed_key = self.hash(key)
        if key not in self.table[hashed_key]:
            return 
        else:
            self.table[hashed_key].remove(key)
        

    def contains(self, key: int) -> bool:
        hashed_key = self.hash(key)
        return key in self.table[hashed_key]