from person import Person
from game_new import Puzzle
from state import State
from loader import Loader
#######Game 1 inputs
persons = [["roberta","female"],["thelma","female"],["steve","male"],["pete","male"]]
jobs = ["chef","guard","nurse","clerk","police","teacher","actor","boxer"]
game1_state = persons
game1_domain = jobs
game1_type = "jobs"

#########Game 2 inputs

"""
house_colr = ["blue","ivory","green","yellow","red"]
citizen = ["english","spaniard","ukranian","norwegian","japanese"]
food = ["kitkat","smarties","snickers","milky ways","hersheys"]
drink = ["tea","water","coffee","orange juice","milk"]
pets = ["dog","snails","horse","fox","zebra"]
"""
#"""
house_colr = ["green","ivory","red","blue","yellow"]
citizen = ["norwegian","japanese","english","spaniard","ukranian"]
food = ["kitkat","milky ways","snickers","hersheys","smarties"]
drink = ["water","milk","orange juice","coffee","tea"]
pets = ["zebra","horse","fox","dog","snails"]
#"""

game2_state = house_colr
game2_domain = [citizen,food,drink,pets]
game2_type = "houses"

#####init loading run & print 
load = Loader(game1_state,game1_domain,game1_type)
domain = load.generate_domain()
start_state = load.load_state()
puz = Puzzle(domain,game1_state,game1_type,True)
result = []
puz.solver(start_state,[],result)

print "\n_____Result(s) for \"jobs\" puzzle using MRV______"
for i in result:
    for j in i:
        print j[0].Node.name,
        print j[1:]

puz = Puzzle(domain,game1_state,game1_type,False)
result = []
puz.solver(start_state,[],result)

print "\n_____Result(s) for \"jobs\" puzzle using backtracking______"
for i in result:
    for j in i:
        print j[0].Node.name,
        print j[1:]

load = Loader(game2_state,game2_domain,game2_type)
domain = load.generate_domain()
start_state = load.load_state()

puz = Puzzle(domain,game2_state,game2_type,True)
result = []
puz.solver(start_state,[],result)

print "\n_____Result(s) for \"houses\" puzzle using MRV______"
for i in result:
    for j in i:
        print j[0].Node.color,
        print j[1:]

puz = Puzzle(domain,game2_state,game2_type,False)
result = []
puz.solver(start_state,[],result)

print "\n_____Result(s) for \"houses\" puzzle using backtracking______"
for i in result:
    for j in i:
        print j[0].Node.color,
        print j[1:]


print "___________"

#for i in result:
#    for j in i:
        #print j[0].Node.name,
        #print j[1:]
    #print "___________"
