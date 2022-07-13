class MyHashSet:

    def __init__(self):
        
        self.buckets = [[] for _ in range(200)]

    def add(self, key: int) -> None:
                        
                        
                        
                        
                        
                        if not self.contains(key):
                            bucket = key%200
                            self.buckets[bucket].append(key)
                
                        
                        
                    
            # self.array[key] = True
        

    def remove(self, key: int) -> None:
                        bucket = key%200 
                        if key in self.buckets[bucket]:
                            self.buckets[bucket].remove(key)
                        
        

    def contains(self, key: int) -> bool:
                        bucket = key%200
                        return key in self.buckets[bucket]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)