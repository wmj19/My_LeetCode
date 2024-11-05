class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = [[] for _ in range(self.size)]

    def hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self.hash(key)
        for item in self.table[idx]:
            if item[0] == key:
                item[1] = value
                return
        self.table[idx].append([key, value])

    def get(self, key: int) -> int:
        idx = self.hash(key)
        for item in self.table[idx]:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        idx = self.hash(key)
        for i, item in enumerate(self.table[idx]):
            if item[0] == key:
                self.table[idx].pop(i)



