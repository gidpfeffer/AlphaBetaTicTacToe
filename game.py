from copy import deepcopy

class PickupState:
    def __init__(self, grid, player=0):
        self.grid = grid
        self.player = player
        self.map = {0:'X', 1:'O'}

    def is_won(self):
        tries = []

        tries.append(self.horizontal_win())
        tries.append(self.vertical_win())
        tries.append(self.down_diagonal_win())
        tries.append(self.up_diagonal_win())

        for trie in tries:
            if trie[0]:
                return trie

        return (False, "")

    def horizontal_win(self):
        tries = {}
        grid = self.grid
        for i in range(len(grid)):
            win = True
            pos = grid[i][0]
            for j in range(len(grid[0])):
                if grid[i][j] != pos:
                    win = False
            tries[win] = pos
        for key in tries:
            if key and tries[key] != '':
                return (True, tries[key])

        return (False, "")

    def vertical_win(self):
        tries = {}
        grid = self.grid
        for i in range(len(grid[0])):
            pos = grid[0][i]
            win = True
            for j in range(len(grid)):
                if grid[j][i] != pos:
                    win = False
            tries[win] = pos
        for key in tries:
            if key and tries[key] != '':
                return (True, tries[key])

        return (False, "")

    def down_diagonal_win(self):
        win = True
        grid = self.grid
        pos = grid[0][0]
        for i in range(len(grid)):
            if grid[i][i] != pos:
                win = False
        if win and pos != '':
            return (win, pos)

        return (False, "")

    def up_diagonal_win(self):
        win = True
        grid = self.grid
        depth = len(grid[0])
        pos = grid[depth - 1][0]
        for i in range(len(grid)):
            if grid[depth - 1 - i][i] != pos:
                win = False
        if win and pos != '':
            return (win, pos)

        return (False, "")

    def is_full(self):
        isFull = True
        grid = self.grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '':
                    isFull = False

        return isFull

class PickupGame:
    def __init__(self):
        pass
    
    def get_successors(self, state):
        grid = state.grid
        
        successors = []
        actions = []

        places = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '':
                    places.append((i, j))
            
        for place in places:
            new_state = deepcopy(state)
            new_state.player = 1 - state.player
            new_state.grid[place[0]][place[1]] = new_state.map[state.player]
            
            successors.append(new_state)
            actions.append(place)
            
        return successors, actions

pickup_game = PickupGame()