class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class List:
    ###here tail_prev keeps record of the immediate
    ###second last element  
    def __init__(self):
        self.head = None
        self.tail = None
        self.tail_prev = None
        self.size = 0

    ###function for adding an element at last
    ###if head is null then head is the last element
    ###else add one after the tail O(1)  
    def add_last(self,node_value):
        node = Node(node_value)
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail_prev = self.tail
        self.tail = node 
        self.size += 1

    ###function for adding an element at first
    ###if head is null then head is the first element
    ###else add one before the head O(1)
    def add_first(self,node_value):
        node = Node(node_value)
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            node.next = self.head 
        self.head = node
        self.size += 1

    ###function for printing the list element O(n)
    def print(self):
        temp = self.head
        if not temp:
            print('list is empty')
            return
        while temp:
            print(temp.data,end = ' ')
            temp = temp.next
        print()

    ###function that return the given positioned value O(n)
    def at(self,i):
        if i < 0 or i >= self.size:
            return -10**6
        f=0
        res = self.head
        while f<i:
            f += 1
            res = res.next
        return res.data

    ###function insert at given position O(n)
    def insert_at(self,i,data):
        ###if invalid position, return
        if i < 0 or i >= self.size:
            return
        ###if insertion being at 1st position,
        ###calling the built function add_first
        if i == 0:
            self.add_first(data)
        ###if insertion being at last position,
        ###calling the built function add_last
        elif i == self.size - 1:
            self.add_last(data)
        ###else finding the given positoned node and
        ###the node before that.Then add the given node
        ###between them 
        else:
            flag = 0
            temp = self.head
            node = Node(data)
            pre = None
            while flag < i-1:
                if flag < i:
                    pre = temp
                temp = temp.next
                flag += 1 
            node.next = temp
            pre.next = node

    ###function delete at given position O(n)
    def remove(self,i):
        ###check for invalid position
        if not self.head:
            return
        ###if first position to be deleted then,
        ###make the head as the current heads next
        if i == 0:
            self.head = self.head.next
        ###if last position to be deleted then,
        ###make the previous node pointer of tial as null
        elif i == self.size - 1:
            self.tail_prev.next = None
        ###else find the node before and after the given
        ###positioned node and connect them
        else:
            flag = 0
            temp = self.head
            pre = None
            while flag <= i:
                if flag < i:
                    pre = temp
                temp = temp.next
                flag += 1
            pre.next = temp
        self.size -= 1

    ###funtion for deleting all the element from the list O(n)
    def remove_all(self):
        while self.head:
            self.remove(self.size)
        self.size = 0 

    ###function for reverse the whole list O(n)
    def reverse(self):
        if not self.head:
            return
        prev = None
        cur = self.head 
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

             
            
if __name__ == '__main__':
    ls = List()
    ls.print()
    ls.add_last(1)
    ls.add_last(12)
    ls.print()
    ls.add_last(-4)
    ls.add_last(8)
    ls.print()
    ls.add_first(56)
    ls.add_first(102)
    ls.print()
    print(ls.size)
    print(ls.at(4))
    print(ls.at(0))
    ls.insert_at(0,102)
    ls.insert_at(6,-1025)
    ls.insert_at(4,-25)
    ls.print()
    ls.remove(0)
    ls.print()
    ls.remove(7)
    ls.print()
    ls.remove(3)
    ls.print()
    #ls.remove_all()
    ls.print()
    print(ls.size)
    ls.add_last(669)
    ls.print()
    print(ls.size)
    ls.reverse()
    ls.print()

