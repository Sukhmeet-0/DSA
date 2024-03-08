class Node:
    def __init__(self,val=None,next=None):
        self.val = val 
        self.next = next
class SLL:
    def __init__(self,start=None):
        self.start=start
    def isEmpty(self):
        return self.start==None
    def insert_at_start(self,data):
        n = Node(data,self.start)
        self.start = n 
    def insert_at_last(self,data):
        n = Node(data)
        if self.isEmpty():
            self.start = n 
        else:
            temp = self.start 
            while temp.next is not None:
                temp = temp.next
            temp.next = n   
    def search(self,data):
        temp = self.start 
        while temp is not None:
            if temp.val == data:
                return temp
            temp = temp.next
        return None
    def traverse(self):
        temp = self.start 
        while temp:
            print(temp.val,end='->')
            temp=temp.next
    def insert_after(self,data,temp):
        if data is not None:
            n = Node(temp,data.next)
            data.next = n 
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
    def delete_item(self,item):
        if self.start is None:
            pass
        elif (self.start.val == item) and (self.start.next is None):
            self.start = None
        else:
            temp = self.start 
            if temp.val == item:
                self.start = temp.next
            else:
                while temp is not None:
                    if temp.next.val == item:
                        temp.next= temp.next.next
                        break 
                    temp = temp.next
    def __iter__(self):
        return SLLIterable(self.start)
class SLLIterable:
    def __init__(self,start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.val
        self.current = self.current.next
        return data
            
mylist = SLL()
mylist.insert_at_start(10)
# mylist.traverse()
mylist.insert_at_start(20)
# mylist.traverse()
mylist.insert_at_last(30)
# mylist.traverse()
mylist.insert_after(mylist.search(10),25)
# mylist.traverse()
mylist.delete_last()
# mylist.traverse()
mylist.delete_item(10)
# mylist.traverse()

for x in mylist:
    print(x,end=' ')
print()