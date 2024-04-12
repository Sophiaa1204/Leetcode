class MyHashMap:

    def __init__(self):
        self.buckets = 1003
        self.table = [[] for _ in range(self.buckets)]
       

    def hash(self, key:int) -> int:
        return key % self.buckets

    def put(self, key: int, value: int) -> None:
        hash_key = self.hash(key)
        for item in self.table[hash_key]:
            if key == item[0]:
                item[1] = value
                return
        self.table[hash_key].append([key,value])

    def get(self, key: int) -> int:
        hash_key = self.hash(key)
        for item in self.table[hash_key]:
            if key == item[0]:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        hash_key = self.hash(key)
        for i,item in enumerate(self.table[hash_key]):
            if key == item[0]:
                self.table[hash_key].pop(i)
                return
   
