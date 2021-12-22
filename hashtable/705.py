
class MyHashSet:

    def __init__(self):
        self.my_set = [False]*int(1e6+1)


    def add(self, key: int) -> None:
        self.my_set[key] = True


    def remove(self, key: int) -> None:
        self.my_set[key] = False


    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.my_set[key]

obj = MyHashSet()
obj.add(1)
obj.remove(1)
param_3 = obj.contains(1)