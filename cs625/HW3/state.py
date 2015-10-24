class State:
    def __init__(self,Node,typ,heur = None):
        self.heuristic = heur
        self.typ = typ
        self.Node = Node
        self.next_node = None

    def next(self):
        return self.next_node
    def setHeur(self,heur):
        self.heuristic = heur
