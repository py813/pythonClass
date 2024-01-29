class HashTable:

    def __init__(self, size):
    #initialize table
       self.hash_table = size
       self.table = [None] * size
       
    def hashFunction(self, key):
        #basic hash function
        return len(key) % 10

    def check_collision(self, index, key, value):
        # make sure entry is empty
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
        #if not empty add to the entry
            self.table[index].append((key, value))

    def add_to_linked_list(self):
       pass

    def insert(self, key, value):
        #Create entry based on hash function then check for collision
        index = self.hashFunction(key)
        self.check_collision(index, key, value)

    def delete(self, key):
        #assign index to be able to use key
        index = self.hashFunction(key)
        #remove appropriate entry based on key
        self.table[index] = None

    def get(self, key):
        hashValue = self.hashFunction(key)
        #see if there is a entry with that hash value
        if self.table[hashValue] is not None:
            for stored_key, value in self.table[hashValue]:
                if stored_key == key:
                    return value
        return None 

#Initialize
hash_table = HashTable(size=20)
#insert values
hash_table.insert("name", "John")
hash_table.insert("age", 25)
hash_table.insert("city", "New York")
#test Output
print(hash_table.get("name"))  # Output: John
print(hash_table.get("age"))   # Output: 25
print(hash_table.get("city"))  # Output: New York
hash_table.delete("age")
print(hash_table.get("age"))   # Output: None (age is deleted)