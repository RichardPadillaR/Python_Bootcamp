class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:
    def front(self):
        if self.head == None:
            return False
        else:
            head = self.head
            print(head)


    def removefront(self):
        if self.head == None:
            return False
        else:
            new_head = self.next
            self.head = new_head
            print(new_head)

    def addfront(self,data):
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head


