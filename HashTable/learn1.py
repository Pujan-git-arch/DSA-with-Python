
class Hashtable:
    def __init__(self):
        self.MAX = 100
        self.arr =[None for i in range(self.MAX)]
        
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)  #ord finds ascii value of the character
        return h % self.MAX
    
    def __setitem__(self,key,val):
        h= self.get_hash(key)
        self.arr[h] = val
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]   
    
t = Hashtable()
print(t.get_hash("march 6")) 
print(t.get_hash("dec 270")) 
t["march 6"] = 100         # this is same as t.__setitem__("march 6", 100) and t["march 6"] is same as t.__getitem__("march 6")
t["dec 270"] = 200
print(t["march 6"])
print(t["dec 270"])  # [[With this we need to give t["march 6"] = 100 before t["march 6"] otherwise it will return None because we are not storing the value in the array.]]
print(t.arr) # [[This will show the array with the values stored at the respective hash index.]]

    
#     def add(self,key,val):
#         h= self.get_hash(key)
#         self.arr[h] = val
    
#     def get(self,key):        
#         h = self.get_hash(key)
#         return self.arr[h]   
    
    
# t = Hashtable()
# print(t.get_hash("march 6"))
# t.add("march 6", 100)
# print(t.get("march 6"))      [[With this we need to give t.add("march 6", 100) before t.get("march 6") otherwise it will return None because we are not storing the value in the array.]]
    