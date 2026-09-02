class Node:
    def __init__(self,data):
        self.data=data          #stores data
        self.next=None          #points to next node

class LL:
    def __init__(self):
        self.head=None          #initially LL is empty

    def isEmpty(self):
        return self.head is None

    def create(self):
        n=int(input("Enter no. of nodes:"))
        if n<=0:                                   
            print("Enter valid no. of nodes.")       # checks if the number of nodes is valid
            return
        for i in range(1,n+1):
            value=input(f"Enter value for node {i}:")       # takes the value of each node from the user
            self.insert(value)

    def insert(self,val):
        new_node=Node(val)
        if self.isEmpty():
            self.head=new_node          # if linked list is empty, new node becomes the head
        else:
            temp=self.head                          # starts from the first node
            while temp.next is not None:            # moves temp until it reaches the last node
                temp=temp.next
            temp.next=new_node                      # last node points to the new node

    def display(self):
        if self.isEmpty():
            print("Linked List is empty...")
            return
        temp=self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next
        print("None")                       # marks the end of the linked list

    def delete(self,val):
        if self.isEmpty():
            print("Nothing to delete...")
            return
        if self.head.data==val:                     # if the first node contains the given value
            self.head=self.head.next                # move head to the next node
            print(f"Node {val} is deleted...")
            return

        prev=self.head                              # prev stores the previous node
        temp=self.head.next                         # temp starts from the second node
        while temp is not None:                     # searches for the node containing the given value
            if temp.data==val:
                prev.next=temp.next                 # removes the node from the list
                print(f'Node {val} is deleted...')
                return                              # stop after deleting
            prev=temp                               
            temp=temp.next                          # move both pointers to the next nodes
        print(f"Node {val} not found...")           #if value not found

n=LL()
while True:
    ch=int(input("1 for create\n2 for insert\n3 for display\n4 for delete\nenter choice: "))
    if ch==1:
        n.create()
    elif ch==2:
        val=input("Enter value to insert:")
        n.insert(val)
    elif ch==3:
        n.display()
    elif ch==4:
        val=input("Enter value to delete:")
        n.delete(val)
    else:
        print("Invalid choice, try again.")