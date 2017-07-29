import random
from copy import deepcopy


class GamePlayer(object):
    '''Represents the logic for an individual player in the game'''

    def __init__(self, player_id, game):
        '''"player_id" indicates which player is represented (int)
        "game" is a game object with a get_successors function'''
        self.player_id = player_id
        self.game = game
        return

    def evaluate(self, state):
        '''Evaluates a given state for the specified agent
        "state" is a game state object'''
        pass

    def minimax_move(self, state):
        '''Returns a string action representing a move for the agent to make'''
        pass

    def alpha_beta_move(self, state):
        '''Same as minimax_move with alpha-beta pruning'''
        pass


class BasicPlayer(GamePlayer):
    '''A basic agent which takes random (valid) actions'''

    def evaluate(self, state):
        '''This agent doesn't evaluate states, so just return 0'''
        return 0

    def minimax_move(self, state):
        '''Don't perform any game-tree expansions, just pick a random move
            that's available in the list of successors'''
        assert state.player == self.player_id
        successors, actions = self.game.get_successors(state)
        print "here is the current board: "
        values = num_print_grid(state.grid)
        person = 0
        while(True):
        	person = input('Enter a valid number where you would like to move: ')
        	if person in values:
        		break
        for suc in successors:
        	if suc.grid[values[person][0]][values[person][1]] == state.map[state.player]:
        		if(suc.is_won()[0]):
        			print "You Won!\n"
        		if(suc.is_full()):
        			print "Game Ends in a Draw\n"
        		return suc
        raise NotImplementedError()
        # Take a random successor's action
        

    def alpha_beta_move(self, state):
        '''Just calls minimax_move'''
        return self.minimax_move(state)


def minimax_dfs(game, state, depth, eval_fn):
    """Return (value, action) tuple for minimax search up to the given depth"""
    # *** YOUR CODE HERE ***
    sucs, act = game.get_successors(state)
    assert sucs is not None
    evals = []
    for suc in sucs:
        evals.append(minimax_min(game, suc, depth + 1, eval_fn))
    index = evals.index(max(evals))
    return sucs[index], act[index]

def minimax_min(game, state, depth, eval_fn):
    sucs, act = game.get_successors(state)
    if sucs is None or state.is_won()[0] or state.is_full():
        return eval_fn(state)
    evals = []
    for suc in sucs:
        evals.append(minimax_max(game, suc, depth + 1, eval_fn))
    index = evals.index(min(evals))
    return evals[index]


def minimax_max(game, state, depth, eval_fn):
    sucs, act = game.get_successors(state)
    if sucs is None or state.is_won()[0] or state.is_full():
        return eval_fn(state)
    evals = []
    for suc in sucs:
        evals.append(minimax_min(game, suc, depth + 1, eval_fn))
    index = evals.index(max(evals))
    return evals[index]

def alphabeta(game, state, depth, eval_fn, alpha, beta):
    sucs, act = game.get_successors(state)
    assert sucs is not None
    evals = []
    for suc in sucs:
        evals.append(alphabeta_min(game, suc, depth + 1, eval_fn, alpha, beta))
    index = evals.index(max(evals))
    return sucs[index], act[index]


def alphabeta_max(game, state, depth, eval_fn, alpha, beta):
    sucs, act = game.get_successors(state)
    if sucs is None or state.is_won()[0] or state.is_full():
        return eval_fn(state)
    evals = []
    for suc in sucs:
        alpha = alphabeta_min(game, suc, depth + 1, eval_fn, alpha, beta)
        if alpha >= beta:
            return alpha
        evals.append(alpha)
    index = evals.index(max(evals))
    return evals[index]


def alphabeta_min(game, state, depth, eval_fn, alpha, beta):
    sucs, act = game.get_successors(state)
    if sucs is None or state.is_won()[0] or state.is_full():
        return eval_fn(state)
    evals = []
    for suc in sucs:
        beta = alphabeta_max(game, suc, depth + 1, eval_fn, alpha, beta)
        if alpha >= beta:
            return beta
        evals.append(beta)
    index = evals.index(min(evals))
    return evals[index]


class StudentPlayer(GamePlayer):
    def __init__(self, player_id, game):
        GamePlayer.__init__(self, player_id, game)
        self.searched = 0
        return

    def evaluate(self, state):
        # *** YOUR CODE HERE ***
        win = state.is_won()

        if win[0]:
        	if self.player_id == state.player:
        		return -1
        	return 1

        return 0
        raise NotImplementedError()

    def minimax_move(self, state):
        assert state.player == self.player_id
        # Experiment with the value of horizon
        suc, action = minimax_dfs(self.game, state, 0, self.evaluate)
        print "Gideon Bot is Thinking....."
        pretty_print_grid(suc.grid)
        if(suc.is_won()[0]):
        	print "Gideon Bot Won!\n"
        if(suc.is_full()):
        	print "Game Ends in a Draw\n"
        return suc

    def alpha_beta_move(self, state):
    	assert state.player == self.player_id
        # *** YOUR CODE HERE ***
        alpha = -2000
        beta = 2000
        suc, action = alphabeta(self.game, state, 0, self.evaluate, alpha, beta)
        print "Gideon Bot is Thinking....."
        pretty_print_grid(suc.grid)
        if(suc.is_won()[0]):
        	print "Gideon Bot Won!\n"
        if(suc.is_full()):
        	print "Game Ends in a Draw\n"
        return suc
        raise NotImplementedError()

def pretty_print_grid(grid):
    print "\n++++++\n",
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "":
                print " ",
            else: print grid[i][j],
        print ""
    print "++++++\n\n",

def num_print_grid(grid):
	values = {}
	num = 0
	print "\n++++++\n",
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j] == "":
				print str(num),
				values[num] = (i, j)
				num = num + 1
			else: print grid[i][j],
		print ""
	print "++++++\n\n",
	return values
