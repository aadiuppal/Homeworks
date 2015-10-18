from Node import Node
from heap import Heap
class Astar:
    def a_star(self,start,goal,mode):
        isvisited = {}
        iter_count = 0
        max_front_len = 1
        prev_iter_count = 0
        heap = Heap()
        #front = {start : start.heurstic(goal,mode)}#+start.depth}
        heap.push_value(start,start.heurstic(goal,mode))
        while len(heap.array) > 0:
            temp,temp_heur = heap.pop_min()
            if temp.game == goal.game:
                return temp.traceback(),iter_count,max_front_len,len(isvisited.keys())
            for i in temp.successor():
                if str(i) in isvisited:
                    continue
                isvisited[str(i)] = True
                state = Node(i, temp)
                heap.push_value(state,state.heurstic(goal,mode))
                #front[state] = state.heurstic(goal,mode) #+ float(state.depth)
            max_front_len = max(max_front_len, len(heap.array))
            iter_count += 1
            print "iter=",iter_count,"queue=",len(heap.array),"f=g+h=",temp_heur,"depth=",temp.depth
            if iter_count > 10000000:
                print "Exiting A-star search :::iteration count excceded 10000000"
                return [[None]],iter_count,max_front_len,len(isvisited.keys())
        return [[None]],iter_count,max_front_len,len(isvisited.keys())
