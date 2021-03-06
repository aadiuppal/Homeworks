import sys
from Node import Node
from game import CreateGame
from astar import Astar

if __name__ == "__main__":
    Game = CreateGame()
    game = Game.create_game(int(sys.argv[1]),int(sys.argv[2]))
    #game = [['D'],['E','F','I','J'],['B','G'],['C','H'],['A']]
    #game = [['F', 'C', 'B', 'G', 'I', 'J','K', 'L','M', 'N', 'O','P', 'Q', 'A'], ['D', 'H'], ['E']]
    target_game = Game.create_target(int(sys.argv[1]),int(sys.argv[2]))
    #target_game = Game.create_target(3,10)
    start = Node(game)
    target = Node(target_game)
    #heurstics = {"default":"Default (blocks out of place)","M":"Matching Rows","De":"Euclidean Distance","Dm":"Manhattan Distance"}
    #heurstics = {"M":"matching rows"}
    #heurstics = {"default":"default heur"}
    heurstics = {"default":"default heur(out of place blocks)","M":"Matching rows"}
    for h in heurstics.keys():
        mode = h
        A = Astar()
        ans,iter_count,front_len,visited = A.a_star(start,target,mode)
        print "____Some Statistics____"
        print "Heuristic :",heurstics[h]
        print "Max frontier length",front_len
        print "Length of path",len(ans)
        print "Number of iterations",iter_count
        print "Visited States",visited
	print "Solutio path:"
        Game.print_moves(ans[::-1])
    #if ans:
    #    print_moves(ans[::-1])
    #else:
    #    print "No Solution exists"
    #print_moves(start.successor())
    #print_moves(successor(game))

