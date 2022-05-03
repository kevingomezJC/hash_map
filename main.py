# A hashmap implementation in python


class HashMap:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size

    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return None
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
            return None


    def delete(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return False
        else:
            for i in range(0, len(self.map[key_hash])):
                if self.map[key_hash][i][0] == key:
                    self.map[key_hash].pop(i)
                    return True
        return False


hashmap = HashMap()
hashmap.add('one', 1)
hashmap.add('two', 2)


print(hashmap.get('one'))
print(hashmap.get('two'))
print(hashmap.delete('one'))
print(hashmap.delete('two'))
print(hashmap.get('one'))
print(hashmap.get('two'))