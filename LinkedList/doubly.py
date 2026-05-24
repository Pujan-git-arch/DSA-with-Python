class Node:
    def __init__(self,data=None,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    
    def insert_at_beginning(self,data):
         node = Node(data,None,self.head)
         
         if self.head is not None:
             self.head.prev = node
             
         self.head = node
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None,None)
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data,itr,None)
            
    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def get_length(self):
        count =0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    
    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Choice")
        if index==0:
            self.head=self.head.next
            if self.head:
                self.head.prev=None
            return
        count=0
        itr=self.head
        while itr:
            if count==index:
                itr.prev.next=itr.next
                if itr.next:
                    itr.next.prev=itr.prev
                break
            count+=1
            itr=itr.next
            
    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Choice")
        if index==0:
            self.insert_at_beginning(data)
            return
        
        count=0
        itr=self.head
        while itr:
            if count == index-1:
                node = Node(data,itr,itr.next)
                if itr.next:
                    itr.next.prev=node
                itr.next=node
                break
            count+=1
            itr=itr.next
            
    def print_forward(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        llstr=""
        itr=self.head
        while itr:
            llstr+=str(itr.data)+"-->"
            itr=itr.next
        print(llstr)
        
    def print_backward(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        llstr=""
        itr=self.head
        while itr.next:
            itr=itr.next
        while itr:
            llstr+=str(itr.data)+"-->"
            itr=itr.prev
        print(llstr)
        
if __name__ == '__main__':
    ll=LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    