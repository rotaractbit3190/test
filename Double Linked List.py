

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createDLL(self, value):
        newnode = Node(value)

        newnode.next = None
        newnode.prev = None
        self.head = newnode
        self.tail = newnode
        return "created"

    def insert(self, value, location):

        if self.head == None:
            print("node does not exist")

        else:
            newnode = Node(value)
            if location == 0:

                newnode.prev = None
                newnode.next = self.head
                self.head.prev = newnode
                self.head = newnode

            elif location == -1:

                newnode.next = None
                newnode.prev = self.tail
                self.tail.next = newnode
                self.tail = newnode

            else:
                tempnode = self.head
                index = 0
                while index < location-1:
                    tempnode = tempnode.next
                    index += 1

                # newnode.next = tempnode.next
                # newnode.prev=tempnode
                # # this line gets the prev of the next node
                # newnode.prev.next = newnode
                # tempnode.next=newnode

                # my logic

                nextnode = tempnode.next
                newnode.prev = tempnode
                newnode.next = nextnode
                tempnode.next = newnode
                nextnode.prev = newnode

    def transversal(self):
        if self.head == None:
            print("head does not exist")
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def reverse_transversal(self):
        if self.head == None:
            print("head does not exist")
        node = self.tail
        while node is not None:
            print(node.value)
            node = node.prev

    def search(self, value):
        if self.head == None:
            print("head does not exist")
        node = self.head
        while node:
            if node.value == value:
                print(f"{node.value} found")

            node = node.next

    def delete(self, location):
        if self.head == None:
            print("node does not exist")

        else:
            if location == 0:
                if self.tail == self.head:
                    self.head = None
                    self.tail = None

                else:
                    self.head = self.head.next
                    self.head.prev = None

            elif location == -1:
                if self.tail == self.head:
                    self.head = None
                    self.tail = None

                else:
                    self.tail = self.tail.prev
                    self.tail.next = None

            else:
                tempnode = self.head
                index = 0
                while index < location-1:
                    tempnode = tempnode.next
                    index += 1

                nextnode = tempnode.next
                tempnode.next = nextnode.next
                nextnode.next.prev = tempnode

    def deleteall(self):

        tempnode = self.head
        while tempnode:
            tempnode.prev=None
            tempnode=tempnode.next
        
        self.head=None
        self.tail=None
        
        print("done")




createdDDL = DLL()
createdDDL.createDLL(3)

# added a comment
print([i.value for i in createdDDL])
createdDDL.insert(1, 0)
createdDDL.insert(2, -1)
createdDDL.insert(3, -1)
createdDDL.insert(2, 1)

print([i.value for i in createdDDL])

createdDDL.transversal()
createdDDL.reverse_transversal()
createdDDL.search(2)

createdDDL.delete(2)
print([i.value for i in createdDDL])

createdDDL.deleteall()
print([i.value for i in createdDDL])
