# Alex Miller

class Node(object):

    value = ""
    def __init__(self,v):
        self.value = v
        self.next = None
    
    def addafterhead(self,v):
        newNode = Node(v)
        newNode.value = v
        newNode.next = None
        if v > str(self.value):
            self.next.addafterhead(v)
        else:
            if self.next != None:
                node = self.next
                self.next = newNode
                newNode.next = node
            else:
                self.next = newNode
class LL:

    def __init__(self):
        self.head = Node(None)
        self.next = Node(None)

    def PrintList(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next

    def add(self,v):
        newNode = Node(v) # create a new node
        newNode.next = None
        if self.head.value == None:
            self.head = newNode
        else:
            if v > self.head.value:
                self.next.addafterhead(v)

def main():
    L = LL()
    value = ""
    while value != "exit":
        print("Enter a value: ",end="")
        value = input()
        if value == "exit":
            break
        L.add(value)

    print()
    LL.PrintList(L)

if __name__ == '__main__':
    main()