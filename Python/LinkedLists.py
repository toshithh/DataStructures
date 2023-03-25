class SinglyLinkedList:
    class Node:
        def __init__(self, data) -> None:
            self.next = None
            self.data = data

    def __init__(self, *args) -> None:
        self.head = None
        self.length = 0
        for x in args:
            self.append(x)

    def checkIndex(self, index):
        if index>=self.length:
            raise(IndexError("Index out of range"))

    def append(self, data):
        node = self.Node(data)
        node.next = self.head
        self.head = node
        self.length +=1

    def appendRight(self, data):
        node = self.Node(data)
        temp = self.head
        if temp==None:
            self.head = node
        else:
            while temp.next!=None:
                temp = temp.next
            temp.next = node

    def pop(self, index=0):
        temp = self.head
        self.checkIndex(index)
        temp = self.head
        self.length-=1
        if index==0:
            self.head = self.head.next
        else:
            i = 1
            while i<index:
                temp = temp.next
                i+=1
            temp.next = temp.next.next
    
    def data(self, index):
        self.checkIndex(index)
        temp = self.node(index)
        return temp.data
    
    def node(self, index):
        self.checkIndex(index)
        temp = self.head
        i = 0
        while i<index:
            temp = temp.next
            i+=1
        return temp
    
    def insert(self, index, data):
        self.checkIndex(index)
        if index==0:
            return self.append(data)
        temp = self.head
        for i in range(index-1):
            temp = temp.next
        temp.next = temp.next.next

    def __str__(self):
        temp = self.head
        print("{", end=" ")
        while temp!=None:
            print(temp.data, end=" ")
            temp = temp.next
        return "}"






class DoublyLinkedList:
    class Node:
        def __init__(self, data):
            self.next = None
            self.prev = None
            self.data = data
        
    def __init__(self, *args) -> None:
        self.head = None
        self.tail = None
        self.length = 0
        for x in args:
            self.append(x)

    def checkIndex(self, index):
        if index>=self.length:
            raise(IndexError("Index out of range"))

    def appendLeft(self, data):
        node = self.Node(data)
        node.next = self.head
        if self.head == None:
            self.head = node
            self.tail = self.head
        else:
            self.head.prev = node
            self.head = node
        self.length+=1

    def append(self, data):
        node = self.Node(data)
        node.prev = self.tail
        if self.tail == None:
            self.tail = node
            self.head = self.tail
        else:
            self.tail.next = node
            self.tail = node
        self.length+=1

    def insert(self, index, data):
        if(index==0):
            return self.appendLeft(data)
        if(index==self.length):
            return self.append(data)
        self.checkIndex(index)
        temp = self.head
        for i in range(index-1):
            temp = temp.next
        node = self.Node(data)
        node.prev = temp
        node.next = temp.next
        node.next.prev = node
        node.prev.next = node
        self.length+=1

    def data(self, index):
        self.checkIndex(index)
        temp = self.node(index)
        return temp.data
    
    def node(self, index):
        self.checkIndex(index)
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp
    
    def pop(self, index=0):
        self.checkIndex(index)
        temp = self.head
        if index==0:
            self.head = self.head.next
            self.head.prev = None
        elif index==self.length-1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            for i in range(index-1):
                temp = temp.next
            temp.next = temp.next.next
            temp.next.prev = temp

    def __str__(self):
        temp = self.head
        print("{", end=" ")
        while temp!=None:
            print(temp.data, end=" ")
            temp = temp.next
        return ("}")
