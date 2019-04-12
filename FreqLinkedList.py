class Node:
    def __init__(self,data):
        self.data = data
        self.frequency =0
        self.next = None
        

class FreqLinkedList:
    
    def __init__(self):
        self.head = None
             	
# Function to remove node
    def RemoveNode(self, Removekey):

        HeadVal = self.head

        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                

        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        prev.next = HeadVal.next

        HeadVal = None
# Function to filterwords
    def filterWords(self,N):
       curr = self.head
       while (curr):
           if curr.frequency < N:
               Removekey = curr.data
               self.RemoveNode(Removekey)
           curr = curr.next
       self.printList()

# Function to print the linked list
    def printList(self):
        printval = self.head
        while (printval):
            print(printval.data,printval.frequency),
            printval = printval.next

            
# Function to add a node in alphabetical order
    def addNode(self,word):
        temp = self.head
        while temp is not None:
            if temp.data == word:
                temp.frequency = temp.frequency +1
                return
            temp=temp.next
        curr = self.head
        if curr is None:
            n = Node(word)
            n.data = word
            n.frequency =1
            self.head = n
            return
        if curr.data > word:
            n = Node(word)
            n.data = word
            n.next = curr
            n.frequency =1
            self.head = n
            return
        while curr.next is not None:
            if curr.next.data > word:
                break
            curr = curr.next
        n = Node(word)
        n.data = word
        n.next = curr.next
        n.frequency =1
        curr.next = n
        return
   
    
