
# this is linklist with head reference prepending node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linklist:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, val):
        new_node = Node(val)
        # self.head = new_node
        new_node.next = self.head
        self.head = new_node

    def travel(self):
        print("\n traveling..🚉")
        if self.head is None:
            print("linklist is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end="-")
                temp = temp.next

    def search(self, data):
        print("\n seraching..🔍")
        if self.head is None:
            print(f"linklist is empty {data} is not available.")
        else:
            temp = self.head
            while temp is not None:
                if temp.data == data:
                    print(f"found {data}")
                    break
                temp = temp.next
            else:
                print("not found")

    def remove(self, data):
        print("\n removing..🚮")
        if self.head is None:
            print(f"linklist is empty {data} is not available.")
        else:
            prev_node = None
            current_node = self.head
            while current_node is not None and current_node.data != data:
                prev_node = current_node
                current_node = current_node.next

            if current_node is not None:
                if current_node == self.head:
                    self.head = current_node.next
                else:
                    prev_node.next = current_node.next


l = linklist()
l.add(10)
l.add(20)
l.add(30)
l.travel()
l.remove(30)
l.travel()
