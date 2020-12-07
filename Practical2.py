#343 #Taksh
class Node:
    def __init__(self, element, next=None, prev=None):
        self.element = element
        self.next = next
        self.prev = prev

    def display(self):
        print(self.element)

class LinkedList:
    def __init__(self):
        self.start = None
        self.end = None
        self.length = 0

    def is_empty(self) -> bool:
        return self.length == 0

    def get_size(self) -> int:
        return self.length

    def display(self):
        if self.is_empty():
            print("Doubly Linked List is empty")
            return
        first = self.start
        print("The List: ", end='')
        print("[" + first.element, end='')
        first = first.next
        while first:
            print(", " + first.element, end='')
            first = first.next
        print("]")

    def add_head(self, e):
        old_head = self.start
        self.start = Node(e)
        self.start.next = old_head
        if old_head is not None:
            old_head.prev = self.start
        if self.end is None:
            self.end = self.start
        self.length += 1

    def get_head(self) -> Node:
        return self.start

    def remove_head(self):
        if self.is_empty():
            print("Doubly Linked List is empty")
            return
        elif self.length == 1:
            self.start = None
            self.end = None
        else:
            self.start = self.start.next
        self.length -= 1

    def add_tail(self, e):
        new_value = Node(e)
        if self.get_tail() is not None:
            old_tail = self.end
            self.end = new_value
            self.end.prev = old_tail
            old_tail.next = self.end
            self.length += 1
        else:
            self.add_head(e)

    def get_tail(self) -> Node:
        return self.end

    def remove_tail(self):
        if self.is_empty():
            print("Doubly Linked List is empty")
            return
        elif self.length == 1:
            self.start = None
            self.end = None
        else:
            self.end = self.end.prev
        self.length -= 1

    def add_between_list(self, index, element):
        if index > self.length or index < 0:
            print("Index out of bounds")
        elif index == self.length:
            self.add_tail(element)
        elif index == 0:
            self.add_head(element)
        else:
            prev_node = self.get_node_at(index - 1)
            current_node = self.get_node_at(index)
            new_value = Node(element)
            prev_node.next = new_value
            new_value.next = current_node
            new_value.prev = prev_node
            current_node.prev = new_value
            self.length += 1

    def get_node_at(self, index, direction="auto") -> Node:
        if index < 0 or index >= self.length:
            print("Index out of bounds")
        else:
            element_node = self.start
            counter = 0
            while counter < index:
                element_node = element_node.next
                counter += 1
            return element_node

    def remove_between_list(self, index):
        if index < 0 or index >= self.length:
            print("Index out of bounds")
        elif index == self.length - 1:
            self.remove_tail()
        elif index == 0:
            self.remove_head()
        else:
            prev_node = self.get_node_at(index - 1)
            next_node = self.get_node_at(index + 1)
            prev_node.next = next_node
            next_node.prev = prev_node
            self.length -= 1

    def merge(self, linked_list_value):
        if not self.is_empty():
            last_node = self.get_tail()
            last_node.next = linked_list_value.start
            if not linked_list_value.is_empty():
                linked_list_value.start.prev = last_node
                self.end = linked_list_value.end
            self.length = self.length + linked_list_value.length
        else:
            self.start = linked_list_value.start
            self.end = linked_list_value.end
            self.length = linked_list_value.length

    def reverse(self):
        if self.is_empty():
            print("Doubly Linked List is empty")
            return
        elif self.length == 1:
            return
        elif self.length == 2:
            temp = self.start
            self.start = self.end
            self.end = temp
            self.start.prev = None
            self.start.next = self.end
            self.end.prev = self.start
            self.end.next = None
        elif self.length == 3:
            mid = self.__get_node_from_start(1)
            temp = self.start
            self.start = self.end
            self.end = temp
            self.start.prev = None
            self.start.next = mid
            mid.prev = self.start
            mid.next = self.end
            self.end.prev = mid
            self.end.next = None
        elif self.length > 3:
            temp_lst = []
            first = self.start
            temp_lst.append(first)
            first = first.next
            while first:
                temp_lst.append(first)
                first = first.next
            temp_lst.reverse()
            for i in range(0, len(temp_lst)):
                if i == 0:
                    self.start = temp_lst[i]
                    self.start.prev = None
                    self.start.next = temp_lst[i + 1]
                elif i == 1:
                    temp_lst[i].prev = self.start
                    temp_lst[i].next = temp_lst[i + 1]
                elif i == len(temp_lst) - 1:
                    self.end = temp_lst[i]
                    self.end.prev = temp_lst[i - 1]
                    self.end.next = None
                else:
                    temp_lst[i].prev = temp_lst[i - 1]
                    temp_lst[i].next = temp_lst[i + 1]
            temp_lst[len(temp_lst) - 2].prev = temp_lst[len(temp_lst) - 2 - 1]
            temp_lst[len(temp_lst) - 2].next = self.end


one = LinkedList()
print(one.is_empty())
one.add_between_list(0, "zero")
one.add_between_list(1, "one")
one.add_between_list(2, "two")
one.display()
print(one.is_empty())
one.remove_between_list(1)
one.display()
one.add_between_list(1, "one")
one.display()

two = LinkedList()
two.add_head("first_name")
two.add_tail("last_name")
print("Head: ", end='')
two.get_head().display()
print("Tail: ", end='')
two.get_tail().display()
two.remove_tail()
two.get_tail().display()
two.remove_head()
try:
    two.get_head().display()
except AttributeError as e:
    print(e, "\nNo head found")
two.display()

two = LinkedList()
two.add_between_list(0, "zero")
two.add_between_list(1, "one")
two.add_between_list(2, "two")
two.add_between_list(3, "three")
two.display()
two.get_node_at(3).display()
two.get_node_at(3, "start").display()
two.get_node_at(3, "end").display()

three = LinkedList()
three.add_between_list(0, "0")
three.add_between_list(1, "1")
three.add_between_list(2, "2")
three.add_between_list(3, "4")
two.display()
print("Head: ", end='')
two.get_head().display()
print("Tail: ", end='')
two.get_tail().display()
three.display()
print("Head: ", end='')
three.get_head().display()
print("Tail: ", end='')
three.get_tail().display()
two.merge(three)
two.display()
print("Head: ", end='')
two.get_head().display()
print("Tail: ", end='')
two.get_tail().display()
print(f"Size: {two.get_size()}")
two.display()
two.reverse()
two.display()
