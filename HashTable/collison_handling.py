class Hashtable:
    def __init__(self):
        self.MAX = 10
        self.arr =[[] for i in range(self.MAX)]  # [[This will create a list of empty lists to handle collisions.]]  as we are storing key value pair in those cases so we need to create a list of empty lists to store the key value pairs in case of collisions.
        
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)  # ord finds ascii value of the character
        return h % self.MAX
    
    def __setitem__(self,key,val):
        h= self.get_hash(key)
        found = False
         # self.arr[h] = val  # before handling collisions we use to overwrite the value at the respective hash index but now we need to handle collisions so we need to store the key value pair in the list at the respective hash index.
        for idx, element in enumerate(self.arr[h]):  # in enumerate is  used to  iterate the list # [[This will iterate through the list at the respective hash index and check if the key already exists in the list. If it does then it will update the value of that key. If it does not then it will append the key value pair to the list.]]
            if len(element)==2 and element[0]==key:  # [[This will check if the key already exists in the list at the respective hash index. If it does then it will update the value of that key.]]
                self.arr[h][idx] = (key, val)
                found = True
                break
                
        if not found:
            self.arr[h].append((key, val))

    def __getitem__(self,key):
        h = self.get_hash(key)
        self.arr[h]  # [[This will return the list at the respective hash index.]]
        for element in self.arr[h]:  # [[This will iterate through the list at the respective hash index and check if the key exists in the list. If it does then it will return the value of that key. If it does not then it will return None.]]
            if element[0] == key:
                return element[1]
        return None

    def __delitem__(self,key):
        h = self.get_hash(key)
        for i, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][i]
                break
            
            
t = Hashtable()
t["march 6"] = 100
t["dec 270"] = 200
t["dec 270"] = 300
t["june 26"] = 400
t["march 17"] = 500
print(t["march 6"])
print(t["june 26"])
print(t["dec 270"])
print(t["march 17"])


t["march 6"] = 700
del t["march 17"]
print(t.arr)