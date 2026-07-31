class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.tail=None
        self.head=None        
    def get(self, key: int) -> int:
        if key in self.cache.keys():
            self.movetoTail(self.cache[key])
            return self.cache[key].value
        else:
            return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            self.cache[key].value = value
            self.movetoTail(self.cache[key])
            return
        else:
            if self.capacity==0:
                return
            if len(self.cache)<self.capacity:
                if self.tail==None:
                    self.tail=Doublelist(key,value,None,None)
                    self.head=self.tail
                else:
                    self.tail.next=Doublelist(key,value,self.tail,None)
                    self.tail=self.tail.next
                self.cache[key]=self.tail
                return
            else:
                if self.head.next==None:
                    self.cache.pop(self.head.key,None)
                    self.head=None
                    self.tail=None
                    self.tail=Doublelist(key,value,None,None)
                    self.head=self.tail
                else:
                    key_remove=self.head.key
                    self.head=self.head.next
                    self.head.prev=None
                    self.cache.pop(key_remove,None)

                    self.tail.next=Doublelist(key,value,self.tail,None)
                    self.tail=self.tail.next
                self.cache[key]=self.tail
        return
    def movetoTail(self, node: Doublelist) -> None:
        if self.tail==self.head:
            return
        if node==self.head:
            self.head=self.head.next
            self.head.prev=None
            self.tail.next=node
            node.prev=self.tail
            node.next=None
            self.tail=node
            return
        if node==self.tail:
            return
        node.prev.next=node.next
        node.next.prev=node.prev
        self.tail.next=node
        node.prev=self.tail
        node.next=None
        self.tail=node
        return

        

class Doublelist:
    def __init__(self,key,value,prev,next):
        self.key=key
        self.value=value
        self.prev=prev
        self.next=next
