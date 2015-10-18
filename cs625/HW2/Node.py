class Node:
    def __init__(self,game,parent=None):
        self.parent = parent
        self.game = game
        if parent:
            self.depth = parent.depth + 1
        else:
            self.depth = 0

    def traceback(self):
        if not self.parent:
            return [self.game]
        return [self.game]+self.parent.traceback()

    def successor(self):
        moves = []
        my_game = []
        temp_game = []
        move_count = 0
        for i in range(len(self.game)):
            my_game.append(0)
            temp_game.append(0)
        for i in range(len(self.game) * len(self.game)):
            moves.append(0)
        my_game[:] = [stack for stack in self.game]
        total_rows = len(my_game)
        for row in range(total_rows):
            if my_game[row] == []:
                continue
            top = my_game[row][-1]
            my_game[row] = my_game[row][:-1]
            temp_game[:] = [stack for stack in my_game]
            for i in range(total_rows):
                if i == row:
                    continue
                temp_game[i] = temp_game[i] + [top]
                moves[move_count] = [p for p in temp_game]
                move_count += 1
                temp_game[i] = temp_game[i][:-1]
            my_game[row] = my_game[row] + [top]
        moves=moves[:move_count]
        return moves

    def heurstic(self,target,mode):
        #if mode == "De" or mode == "Dm":
        #    h_dist = self.difference(self.game,target.game)
        if mode == "M":
            h_dist = self.matching_rows(self.game,target.game)
        if mode == "default":
            h_dist = self.blocksOutofPlace(self.game,target.game)
        return h_dist + self.depth

    def difference(self, game1, game2,typ):
        diff = 0
        for row in range(len(game1)):
            if game1[row] == []:
                continue
            for i in range(len(game1[row])):
                g2_row, g2_col = self.searchfor(game2, game1[row][i])
                if typ == "Dm":
                    diff += self.manhattan_dist(row, i, g2_row, g2_col)
                if typ == "De":
                    diff += self.euclidean_dist(row, i, g2_row, g2_col)
        return diff

    def searchfor(self, game, letter):
        for row in range(len(game)):
            if game[row] == []:
                continue
            for i in range(len(game[row])):
                if game[row][i] == letter:
                    return row,i
        return None

    def manhattan_dist(self,x1,y1,x2,y2):
        return abs(x2 - x1) + abs(y2 - y1)

    def euclidean_dist(self,x1,y1,x2,y2):
        return (((x2-x1)**2 + (y2-y1)**2)**0.5)

    def matching_rows(self,game1,game2):
        state_dist = 0
        for row in range(len(game1)):
            state_dist += self.compare_rows(game1[row],game2[row],row) * 0.7
            state_dist += self.difference(game1,game2,"De") *0.2
            state_dist += self.blocksOutofPlace(game1,game2) *0.4
        return state_dist

    def compare_rows(self,row1,row2,row_wt):
        dist = 0
        dist += self.compare_lengths(row1,row2,row_wt)
        dist += self.compare_elements(row1,row2)
        return dist

    def compare_lengths(self,row1,row2,row_wt):
        if len(row1) == len(row2):
            return 0
        if len(row1) < len(row2):
            return float(abs(len(row1)-len(row2))) *0.1
        if len(row1) > len(row2):
            return float(abs(len(row1) - len(row2))) *(1/(row_wt+1))

    def compare_elements(self,row1,row2):
        dist = 0
        for i in range(len(row1)):
            if i<len(row2) and row1[i] != row2[i]:
                if row1[i] not in row2:
                    dist +=1
                else:
                    dist +=2
            #elif i>len(row2):
            #    dist += 1
        return dist

    def blocksOutofPlace(self,game1,game2):
        block = 0
        for row in range(len(game1)):
            if game1[row] == []:
                continue
            for col in range(len(game1[row])):
                row_g2,col_g2 = self.searchfor(game2,game1[row][col])
                if row_g2 != row or col_g2 != col:
                    block += 1
        return block
"""
##matching columns
##parameters:
    ##length:
        if l_state > l_goal:
            increased dist
        else:
            dcereased dist
    ##if element in same column:
        yes:
            at same place:
                decreased dist
            not at same place:
                increased dist(greater than no case)
        no:
            increased dist

"""




