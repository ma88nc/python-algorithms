# Linked list
# Ported from this link in c#:
# https://stackoverflow.com/questions/3823848/creating-a-very-simple-linked-list/13742139

import sys

class Node:
    
    def __init__(self):
        self.next = None
        self.data = ''


class LinkedList:

    def __init__(self):
        self.head = None

    def printAllNodes(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

    def addFirst(self, data):
        toAdd = Node()

        toAdd.data = data
        toAdd.next = self.head

        self.head = toAdd

    def addLast(self, data):
        if self.head == None:
            self.head = Node()
            self.head.data = data
            self.head.next = None 
        else:
            toAdd = Node()
            toAdd.data = data    

            current = self.head
            while current.next != None:
                current = current.next    
            current.next = toAdd                           


def main():
    myList1 = LinkedList()
    print("Linkus listus addus firstus")

    myList1.addFirst("Harry")
    myList1.addFirst("Ron")
    myList1.addFirst("Hermione")
    myList1.addFirst("Ginny")
    myList1.printAllNodes()

    myList2 = LinkedList()
    print("\nLinkus listus addus lastus")

    myList2.addLast("Dumbledore")
    myList2.addLast("Snape")
    myList2.addLast("Hagrid")
    myList2.addLast("McGonagall")
    myList2.printAllNodes()

if __name__ == '__main__':
    main()        
