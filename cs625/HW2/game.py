import random
class CreateGame:
    def create_game(self, stacks,letters):
        game=[]
        for i in range(stacks):
            game.append([])
        generated={}
        for i in range(letters):
            var=random.randint(1,letters)
            while var in generated:
                var=random.randint(1,letters)
            generated[var]=True
            pos=random.randint(0,stacks-1)
            game[pos]+=[str(unichr(var+64))]
        for i in range(len(game)):
            print i+1,game[i]
        return game

    def create_target(self, stacks, letters):
        game = []
        for i in range(stacks):
            game.append([])
        for i in range(letters):
            game[0].append(str(unichr(i+65)))
        self.print_moves([game])
        return game
    def print_moves(self, moves):
        for move in moves:
            print "--------------"
            for i in range(len(move)):
                print i+1,move[i]

