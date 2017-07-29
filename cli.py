import os
import sys
import time
import json
import copy
from game import pickup_game, PickupState
from agents import BasicPlayer, StudentPlayer

def pretty_print_grid(grid):
    print
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print grid[i][j],
        print ""


def main(agent0, agent1):
	grid = [['','',''],['','',''],['','','']]

	state = PickupState(grid)

	while(True):
		update = state.is_won()
		if update[0] or state.is_full():
			break
		state = agent0.alpha_beta_move(state)
		update = state.is_won()
		if update[0] or state.is_full():
			break
		state = agent1.alpha_beta_move(state)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("agent0", type=str, choices=['basic', 'student'])
    parser.add_argument("agent1", type=str, choices=['basic', 'student'])
    parser.add_argument("agent0alg", type=str, choices=['minimax', 'alphabeta'])
    parser.add_argument("agent1alg", type=str, choices=['minimax', 'alphabeta'])
    args = parser.parse_args()

    if args.agent0 == 'basic':
        agent0 = BasicPlayer(0, pickup_game)
    else:
        agent0 = StudentPlayer(0, pickup_game)

    if args.agent1 == 'basic':
        agent1 = BasicPlayer(1, pickup_game)
    else:
        agent1 = StudentPlayer(1, pickup_game)

    main(agent0, agent1)