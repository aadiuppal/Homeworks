from state import State
from house import House
from person import Person
class Puzzle:
    def __init__(self,domain,states,typ,mrv = False):
        self.domain = domain
        self.typ = typ
        self.count = 0
        self.mrv = mrv
        self.states = states
        pass
    def solver(self,state,current,result):
        ###update_states on curr
        for d in self.domain:
            if self.consistency_check(state,d,current):
                current.append([state,d])
                if self.isComplete(current):
                    result += [tuple(current)]
                    print
                    print "Result found at iteration ",self.count,"for puzzle ",self.typ,"with mrv ",self.mrv
                    stop = raw_input("\nDo you want to search for more results ?   \n('y' to continue searching , anything else to exit)")
                    if stop != 'y':
                        return
                else:
                    next_s = self.next_state(state,current)
                    #self.solver(state.next(),current,result)
                    self.solver(next_s,current,result)
                current.pop()
    def consistency_check(self,state,d,current):
        self.count += 1
        if self.typ == "jobs":
            return self.consistency_jobs(state.Node,d,current)
        else:
            return self.consistency_houses(state.Node,d,current)

    def consistency_jobs(self,person,jobs,current):
        if person.name not in ['roberta','thelma','steve','pete']:
            return False
        if len(jobs) != 2:
            return False
        for i in jobs:
            if i not in ['chef','guard','nurse','clerk','police','teacher','actor','boxer']:
                return False
        job1, job2 = jobs
        for i in current:
            if i[0].Node.name == person.name:
                return False
            if i[1][0] == job1 or i[1][1] == job1:
                return False
            if i[1][0] == job2 or i[1][1] == job2:
                return False
        if person.gender == "female":
            if job1 == "actor" or job2 =="actor":
                return False
            if job1 == "clerk" or job2 =="clerk":
                return False
            if job1 == "nurse" or job2 == "nurse":
                return False
        if person.education != None and person.education <= 9:
            if job1 == "nurse" or job1 == "police" or job1 == "teacher":
                return False
            if job2 == "nurse" or job2 == "police" or job2 == "teacher":
                return False
        if person.gender == "male":
            if job1 == "chef" or job2 == "chef":
                return False
        if person.name == "roberta":
            if job1 == "chef" or job1 == "police" or job1 == "boxer":
                return False
            if job2 == "chef" or job2 == "police" or job2 == "boxer":
                return False
        if job1 == "chef" and job2 == "police":
            return False
        if job1 == "police" and job2 == "chef":
            return False
        if job1 == "clerk" and job2 == "chef":
            return False
        if job1 == "chef" and job2 == "clerk":
            return False
        return True
    def consistency_houses(self,house,attr,current):
        h_colr = house.color
        citizen,food,drink,pet,h_num = attr

        if citizen == "english" and h_colr != "red":
            return False
        if citizen == "spaniard" and pet != "dog":
            return False
        if citizen == "norwegian" and h_num != 1:
            return False
        curr_houses = {}
        for i in current:
            if i[0].Node.color not in curr_houses:
                curr_houses[i[0].Node.color] = i[1]
            else:
                return False
        for k in curr_houses:
            if k == h_colr :
                return False
            if curr_houses[k][0] == citizen:
                return False
            if curr_houses[k][1] == food:
                return False
            if curr_houses[k][2] == drink:
                return False
            if curr_houses[k][3] == pet:
                return False
            if curr_houses[k][4] == h_num:
                return False
        if "ivory" in curr_houses and h_colr == "green":
            if curr_houses["ivory"][4] != h_num - 1:
                return False
        if "green" in curr_houses and h_colr == "ivory":
            if curr_houses["green"][4] != h_num + 1:
                return False
        if food == "kitkat" and h_colr != "yellow":
            return False
        if food == "smarties" and pet != "snails":
            return False
        if food == "snickers" and drink != "orange juice":
            return False
        if citizen == "ukranian" and drink != "tea":
            return False
        if citizen == "japanese" and food != "milky ways":
            return False
        if h_colr == "green" and drink != "coffee":
            return False
        if h_num == 3 and drink != "milk":
            return False
        if citizen == "norwegian" and h_colr == "blue":
            return False
        if food == "hersheys" and pet == "fox":
            return False
        if food == "kitkat" and pet == "horse":
            return False

        if pet == "fox":
            for h in curr_houses:
                if curr_houses[h][1] == "hersheys":
                    if curr_houses[h][4] != h_num + 1 and curr_houses[h][4] != h_num - 1:
                        return False
        if food == "hersheys":
            for h in curr_houses:
                if curr_houses[h][3] == "fox":
                    if curr_houses[h][4] != h_num + 1 and curr_houses[h][4] != h_num - 1:
                        return False
        if "blue" in curr_houses and citizen == "norwegian":
            if curr_houses["blue"][4] != h_num + 1 and curr_houses["blue"][4] != h_num - 1:
                return False
        if h_colr == "blue":
            for h in curr_houses:
                if curr_houses[h][0] == "norwegian":
                    #print attr,h_colr
                    if curr_houses[h][4] != h_num +1 and curr_houses[h][4] != h_num -1:
                        return False
        if food == "kitkat":
            for h in curr_houses:
                if curr_houses[h][3] == "horse":
                    if curr_houses[h][4] != h_num + 1 and curr_houses[h][4] != h_num - 1:
                        return False
        if pet == "horse":
            for h in curr_houses:
                if curr_houses[h][1] == "kitkat":
                    if curr_houses[h][4] != h_num + 1 and curr_houses[h][4] != h_num - 1:
                        return False

        return True
    def isComplete(self,current):
        if self.typ == "jobs":
            if len(current) == 4:
                return True
        else:
            if len(current) == 5:
                return True
        return False
    def next_state(self,my_state,current):
        #print current
        #print N_visited
        if not self.mrv:
            return my_state.next_node
        nodes = self.states
        N_visited = {}
        visited = []
        if self.typ == "houses":
            for i in current:
                visited.append(i[0].Node.color)
            for i in nodes:
                if i not in visited:
                    N_visited[i] = 0
            for n in N_visited:
                for d in self.domain:
                    if self.consistency_houses(House(n),d,current):
                        N_visited[n] += 1

            return State(House(sorted(N_visited,key= N_visited.get)[0]),self.typ)
        else:
            for i in current:
                visited.append(i[0].Node.name)
            for i in nodes:
                if i[0] not in visited:
                    N_visited[i[0]] = [i[1],0]
            for n in N_visited:
                for d in self.domain:
                    if self.consistency_jobs(Person(n,N_visited[n][0]),d,current):
                        N_visited[n][1] += 1
            p_name = sorted(N_visited,key= N_visited.get)[0]
            return State(Person(p_name,N_visited[p_name][0]),self.typ)
