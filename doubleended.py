class Deque:
      def_init_(self):
           self.items=[]
      def isEmpty(self):
            return self.items==[]
      def addFront(self,item):
            self.items.append(item)
      def addRear(self,item):
            self.items.insert(0,item)
      def removeFront(self):
            return self.items.pop()
      def removeRear(self):
            return self.items.pop(0)
      def size(self):
            return len(self.items)

d=Deque()
print(d.isEmpty())
d.addRear(7)
d.addRear(5)
d.addFront(9)
d.addFront(6)
print(d.size())
print(d.isEmpty())
d.addRear(4)
print(d.removeRear())
print(d.removeFront())
d.addFront(55)
d.addRear(45)
print(d.items)
