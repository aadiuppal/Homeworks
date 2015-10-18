class Heap:
    def __init__(self):
        self.array = []
    def push_value(self,node,value):
        self.array.append([node,value])
        self.swim_heap(0,len(self.array)-1)
    def swim_heap(self,start,end):
        if start >= end:
            return
        child = end
        if end%2 == 0:
            parent = (end/2)-1
        else:
            parent = end/2
        if self.array[parent][1] < self.array[child][1]:
            return
        self.array[parent],self.array[child] = self.array[child],self.array[parent]
        self.swim_heap(start,parent)
    def pop_min(self):
        temp = self.array[0]
        if len(self.array) == 1:
            self.array = []
            return temp
        self.array[0] = self.array[-1]
        self.array = self.array[:-1]
        self.sink_heap(0,len(self.array)-1)
        return temp
    def sink_heap(self,start,end):
        if start >= end:
            return
        parent = start
        child1 = parent *2 + 1
        child2 = parent *2 + 2
        if child1 >= len(self.array):
            return
        if self.array[parent][1] <= self.array[child1][1]:
            if child2 >= len(self.array):
                return
            if self.array[parent][1] <= self.array[child2][1]:
               return
        if self.array[parent][1] > self.array[child1][1]:
            self.array[parent],self.array[child1] = self.array[child1], self.array[parent]
            self.sink_heap(child1,end)
        else:
            self.array[parent],self.array[child2] = self.array[child2], self.array[parent]
            self.sink_heap(child2,end)
