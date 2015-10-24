from person import Person
from state import State
from house import House
class Loader:
    def __init__(self,state,domain,typ):
        self.state = state
        self.domain = domain
        self.typ = typ
    def generate_domain(self):
        dom = []
        if self.typ == "jobs":
            for i in range(len(self.domain)-1):
                temp = []
                temp.append(self.domain[i])
                for j in range(i+1,len(self.domain)):
                    temp.append(self.domain[j])
                    dom += [tuple(temp)]
                    temp.pop()
        else:
            citizen,food,drink,pets = self.domain
            for c in citizen:
                temp = []
                temp.append(c)
                for f in food:
                    temp.append(f)
                    for d in drink:
                        temp.append(d)
                        for p in pets:
                            temp.append(p)
                            for h in range(1,6):
                                temp.append(h)
                                dom += [tuple(temp)]
                                temp.pop()
                            temp.pop()
                        temp.pop()
                    temp.pop()
                temp.pop()
        return dom


    def load_state(self):
        states = []
        if self.typ == "jobs":
            prev = None
            for s in self.state:
                temp = Person(s[0],s[1])
                if s[0] == "pete":
                    temp.education = 9
                temp_state = State(temp,self.typ)
                temp_state.next_node = prev
                prev = temp_state
        else:
            prev = None
            for s in self.state:
                temp = House(s)
                temp_state = State(temp,self.typ)
                temp_state.next_node = prev
                prev = temp_state
        return prev
