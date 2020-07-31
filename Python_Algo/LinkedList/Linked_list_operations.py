class Node:
    def __init__(self,item):
        self.item = item
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        
        def insertAtBegining(self,data):
            new_node = Node(data)
            
            new_node.next = self.head
            self.head = new_node
        
        def insertAfter(self,node,data):
            
            if node is None:
                print("The given node is not in list")
                return
            
            new_node = Node(data)
            new_node.next = node.next
            node.next = new_node
            
        def insertAtEnd(self,data):
            new_node = Node(data)
            
            if self.head is None:
                self.head = new_node
                return
            
            last = self.head
            while(last.next):
                last = last.next
                
            last.next = new_node
        
        def deleteNode(self,position):
            
            if self.head == None:
                return
            
            temp_node = self.head
            
            if position == 0:
                self.head = temp_node.next
                temp_node = None
                return

            for i in range(position -1):
                temp_node = temp_node.next
                if temp_node is None:
                    break
            
            if temp_node is None:
                return
            
            if temp_node.next is None:
                return
            
            next = temp_node.next.next
            temp_node.next = None
            temp_node.next = next
            
            def printList(self):
                temp_node = self.head
                while (temp_node):
                    print(str(temp_node.item) + " ", end="")
                    temp_node = temp_node.next

            
        
                