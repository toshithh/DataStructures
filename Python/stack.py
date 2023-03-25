from LinkedLists import SinglyLinkedList as SLL, DoublyLinkedList as DLL

class SinglyLinkedList(SLL):
    def __init__(self, *args) -> None:
        super().__init__(*args)
    
    def push(self, data):
        return super().append(data)
    
    def pushBottom(self, data):
        return super().appendRight(data)
    
    def pop(self):
        return super().pop(0)
    
    def __str__(self):
        temp = self.head
        while temp!=None:
            print(temp.data)
            temp = temp.next


class DoublyLinkedList(DLL):
    def __init__(self, *args) -> None:
        super().__init__(*args)

    def push(self, data):
        super().appendLeft(data)

    def pop(self):
        super().pop(0)
    
    def pushBottom(self, data):
        super().append(data)

    def __str__(self):
        temp = self.head
        while temp!=None:
            print(temp.data)
            temp = temp.next


class PythonList:
    def __init__(self, *data):
        self.stack = []
        for x in data:
            self.push(data)

    def push(self, data):
        self.stack.insert(0, data)

    def pushBottom(self, data):
        self.stack.append(data)

    def pop(self):
        self.stack.pop(0)

    def __str__(self):
        for x in self.stack:
            print(x)