from api import server
from flask import render_template, jsonify
from api.controller import *
from api.astar import *
import numpy as np

@server.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@server.route('/solve/<string:lists>', methods=['GET', 'POST'])
def solve(lists):
	# Final Running of the Code
	lists = lists.split(",")
	print(lists)
	initial_state = np.zeros(9)
	for i, x in enumerate(lists):
		initial_state[i] = np.array(x)
	k = np.reshape(initial_state, (3, 3))



	check_correct_input(k)
	check_solvable(k)

	root = Node(0, k, None, None, 0)

	# BFS implementation call
	goal, s, v = exploring_nodes(root)

	if goal is None and s is None and v is None:
	    print("Goal State could not be reached, Sorry")
	else:
	    # Print and write the final output
	    # print_states(path(goal))
	    z = print_states(path(goal))
	    print(z)
	return jsonify({'message':z})

@server.route('/solve/astar/<string:lists>', methods=['GET', 'POST'])
def solve_astar(lists):
	lists = lists.split(",")
	lists = [ int(x) for x in lists ]
	print(lists)
	z = str(astar_solver(lists))
	return jsonify({'message':z})