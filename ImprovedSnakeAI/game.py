import random
import curses
import copy
from sys import argv
import numpy as np
import math


sc = curses.initscr()
h, w = sc.getmaxyx()

def fitness_func(steps, apples):
	# return (steps + ((2 ** apples) + ((apples ** 2.1) * 500)) - ((apples ** 1.2) * ((steps * 0.25) ** 1.3))) / 1000000
	# return apples
	if apples == 0:
		return -(steps*10)
	else:
		return (steps*10) + (apples*200)
	# return (steps*10) + (apples*200)

def angle_with_apple(snake_position, apple_position):
	snake_direction = np.array(snake_position[0]) - np.array(snake_position[1])
	apple_direction = np.array(apple_position) - np.array(snake_position[0])
	snake_direction = snake_direction / np.linalg.norm(snake_direction)
	apple_direction = apple_direction / np.linalg.norm(apple_direction)
	return math.atan2(snake_direction[0] * apple_direction[1] - snake_direction[1] * apple_direction[0], 
		snake_direction[0] * apple_direction[0] + snake_direction[1] * apple_direction[1]) / math.pi

def collision_with_apple(score, snake_position):
	apple_position = [random.randint(1,h-2),random.randint(1,w-2)]
	while apple_position in snake_position:
		apple_position = [random.randint(1,h-2),random.randint(1,w-2)]
	score += 1
	return apple_position, score

def collision_with_boundaries(snake_head):
	if snake_head[0]>=h-1 or snake_head[0]<=0 or snake_head[1]>=w-1 or snake_head[1]<=0 :
		return 1
	else:
		return 0

def collision_with_self(snake_position):
	snake_head = snake_position[0]
	if snake_head in snake_position[1:]:
		return 1
	else:
		return 0

def move_up(snake_head, prev_direction, direction):
	new_dir = direction
	if prev_direction != 2:
		new_dir = 3
	snake_head[0] += 1
	return snake_head, new_dir

def move_down(snake_head, prev_direction, direction):
	new_dir = direction
	if prev_direction != 3:
		new_dir = 2
	snake_head[0] -= 1
	return snake_head, new_dir

def move_right(snake_head, prev_direction, direction):
	new_dir = direction
	if prev_direction != 0:
		new_dir = 1
	snake_head[1] += 1
	return snake_head, new_dir

def move_left(snake_head, prev_direction, direction):
	new_dir = direction
	if prev_direction != 1:
		new_dir = 0
	snake_head[1] -= 1
	return snake_head, new_dir

def calculate_distance(x1, y1, x2, y2):    
	return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_right_close(snake_head, snake_position, direction):
	head_copy = copy.deepcopy(snake_head)
	position_copy = copy.deepcopy(snake_position)
	if direction == 0:
		head_copy[0] -= 1
		position_copy[0] = head_copy
		if collision_with_boundaries(head_copy) == 1 or collision_with_self(position_copy) == 1:
			return False
		else:
			return True
	elif direction == 1:
		head_copy[0] += 1
		position_copy[0] = head_copy
		if collision_with_boundaries(head_copy) == 1 or collision_with_self(position_copy) == 1:
			return False
		else:
			return True
	elif direction == 2:
		head_copy[1] -= 1
		position_copy[0] = head_copy
		if collision_with_boundaries(head_copy) == 1 or collision_with_self(position_copy) == 1:
			return False
		else:
			return True
	elif direction == 3:
		head_copy[1] += 1
		position_copy[0] = head_copy
		if collision_with_boundaries(head_copy) == 1 or collision_with_self(position_copy) == 1:
			return False
		else:
			return True
	
def check_left_close(snake_head, snake_position, direction):
	head_copy = copy.deepcopy(snake_head)
	position_copy = copy.deepcopy(snake_position)
	if direction == 0:
		head_copy[0] += 1
		position_copy[0] = head_copy
		if collision_with_boundaries(head_copy) == 1 or collision_with_self(position_copy) == 1:
			return False
		else:
			return True
	elif direction == 1:
		head_copy[0] -= 1
		position_copy[0] = head_copy
		if collision_with_boundaries(head_copy) == 1 or collision_with_self(position_copy) == 1:
			return False
		else:
			return True
	elif direction == 2:
		head_copy[1] += 1
		position_copy[0] = head_copy
		if collision_with_boundaries(head_copy) == 1 or collision_with_self(position_copy) == 1:
			return False
		else:
			return True
	elif direction == 3:
		head_copy[1] -= 1
		position_copy[0] = head_copy
		if collision_with_boundaries(head_copy) == 1 or collision_with_self(position_copy) == 1:
			return False
		else:
			return True

def check_front_close(snake_head, snake_position, direction):
	head_copy = copy.deepcopy(snake_head)
	position_copy = copy.deepcopy(snake_position)
	if direction == 0:
		head_copy[1] -= 1
		position_copy[0] = head_copy
		if collision_with_boundaries(head_copy) == 1 or collision_with_self(position_copy) == 1:
			return False
		else:
			return True
	elif direction == 1:
		head_copy[1] += 1
		position_copy[0] = head_copy
		if collision_with_boundaries(head_copy) == 1 or collision_with_self(position_copy) == 1:
			return False
		else:
			return True
	elif direction == 2:
		head_copy[0] += 1
		position_copy[0] = head_copy
		if collision_with_boundaries(head_copy) == 1 or collision_with_self(position_copy) == 1:
			return False
		else:
			return True
	elif direction == 3:
		head_copy[0] -= 1
		position_copy[0] = head_copy
		if collision_with_boundaries(head_copy) == 1 or collision_with_self(position_copy) == 1:
			return False
		else:
			return True


def check_left_down(snake_head, snake_position, apple_position):
	distances = [0 for i in range(3)]
	y, x = snake_head[0], snake_head[1]
	while y!=h-1 and x!=0:
		if [y, x] in snake_position:
			distances[0] = calculate_distance(snake_head[1], snake_head[0], x, y)
			break
		y+=1
		x-=1
	y, x = snake_head[0], snake_head[1]
	while y!=h-1 and x!=0:
		if [y, x] == apple_position:
			distances[1] = calculate_distance(snake_head[1], snake_head[0], x, y)
			break
		y+=1
		x-=1
	y, x = snake_head[0], snake_head[1]
	while y!=h-1 and x!=0:
		y+=1
		x-=1
	distances[2] = calculate_distance(snake_head[1], snake_head[0], x, y)
	return distances


def check_left_forward(snake_head, snake_position, apple_position):
	distances = [0 for i in range(3)]
	y, x = snake_head[0], snake_head[1]
	while x!=0:
		if [y, x] in snake_position:
			distances[0] = calculate_distance(snake_head[1], snake_head[0], x, y)
			break
		x-=1
	y, x = snake_head[0], snake_head[1]
	while x!=0:
		if [y, x] == apple_position:
			distances[1] = calculate_distance(snake_head[1], snake_head[0], x, y)
			break
		x-=1
	y, x = snake_head[0], snake_head[1]
	while x!=0:
		x-=1
	distances[2] = calculate_distance(snake_head[1], snake_head[0], x, y)
	return distances

def check_left_up(snake_head, snake_position, apple_position):
	distances = [0 for i in range(3)]
	y, x = snake_head[0], snake_head[1]
	while y!=0 and x!=0:
		if [y, x] in snake_position:
			distances[0] = calculate_distance(snake_head[1], snake_head[0], x, y)
			break
		y-=1
		x-=1
	y, x = snake_head[0], snake_head[1]
	while y!=0 and x!=0:
		if [y, x] == apple_position:
			distances[1] = calculate_distance(snake_head[1], snake_head[0], x, y)
			break
		y-=1
		x-=1
	y, x = snake_head[0], snake_head[1]
	while y!=0 and x!=0:
		y-=1
		x-=1
	distances[2] = calculate_distance(snake_head[1], snake_head[0], x, y)
	return distances

def check_right_down(snake_head, snake_position, apple_position):
	distances = [0 for i in range(3)]
	y, x = snake_head[0], snake_head[1]
	while y!=h-1 and x!=w-1:
		if [y, x] in snake_position:
			distances[0] = calculate_distance(snake_head[1], snake_head[0], x, y)
			break
		y+=1
		x+=1
	y, x = snake_head[0], snake_head[1]
	while y!=h-1 and x!=w-1:
		if [y, x] == apple_position:
			distances[1] = calculate_distance(snake_head[1], snake_head[0], x, y)
			break
		y+=1
		x+=1
	y, x = snake_head[0], snake_head[1]
	while y!=h-1 and x!=w-1:
		y+=1
		x+=1
	distances[2] = calculate_distance(snake_head[1], snake_head[0], x, y)
	return distances

def check_right_forward(snake_head, snake_position, apple_position):
	distances = [0 for i in range(3)]
	y, x = snake_head[0], snake_head[1]
	while x!=w-1:
		if [y, x] in snake_position:
			distances[0] = calculate_distance(snake_head[1], snake_head[0], x, y)
			break
		x+=1
	y, x = snake_head[0], snake_head[1]
	while x!=w-1:
		if [y, x] == apple_position:
			distances[1] = calculate_distance(snake_head[1], snake_head[0], x, y)
			break
		x+=1
	y, x = snake_head[0], snake_head[1]
	while x!=w-1:
		x+=1
	distances[2] = calculate_distance(snake_head[1], snake_head[0], x, y)
	return distances

def check_right_up(snake_head, snake_position, apple_position):
	distances = [0 for i in range(3)]
	y, x = snake_head[0], snake_head[1]
	while y!=0 and x!=w-1:
		if [y, x] in snake_position:
			distances[0] = calculate_distance(snake_head[1], snake_head[0], x, y)
			break
		y-=1
		x+=1
	y, x = snake_head[0], snake_head[1]
	while y!=0 and x!=w-1:
		if [y, x] == apple_position:
			distances[1] = calculate_distance(snake_head[1], snake_head[0], x, y)
			break
		y-=1
		x+=1
	y, x = snake_head[0], snake_head[1]
	while y!=0 and x!=w-1:
		y-=1
		x+=1
	distances[2] = calculate_distance(snake_head[1], snake_head[0], x, y)
	return distances

def check_down(snake_head, snake_position, apple_position):
	distances = [0 for i in range(3)]
	y, x = snake_head[0], snake_head[1]
	while y!=h-1:
		if [y, x] in snake_position:
			distances[0] = calculate_distance(snake_head[1], snake_head[0], x, y)
			break
		y+=1
	y, x = snake_head[0], snake_head[1]
	while y!=h-1:
		if [y, x] == apple_position:
			distances[1] = calculate_distance(snake_head[1], snake_head[0], x, y)
			break
		y+=1
	y, x = snake_head[0], snake_head[1]
	while y!=h-1:
		y+=1
	distances[2] = calculate_distance(snake_head[1], snake_head[0], x, y)
	return distances

def check_up(snake_head, snake_position, apple_position):
	distances = [0 for i in range(3)]
	y, x = snake_head[0], snake_head[1]
	while y!=0:
		if [y, x] in snake_position:
			distances[0] = calculate_distance(snake_head[1], snake_head[0], x, y)
			break
		y-=1
	y, x = snake_head[0], snake_head[1]
	while y!=0:
		if [y, x] == apple_position:
			distances[1] = calculate_distance(snake_head[1], snake_head[0], x, y)
			break
		y-=1
	y, x = snake_head[0], snake_head[1]
	while y!=0:
		y-=1
	distances[2] = calculate_distance(snake_head[1], snake_head[0], x, y)
	return distances

def run_game(network, iterations, speed, gui=True):
	fitness = 0
	for i in range(iterations):
		win = curses.newwin(h, w, 0, 0)
		win.keypad(1)
		curses.curs_set(0)
		snake_head = [10,15]
		snake_position = [[15,10],[14,10],[13,10]]
		apple_position = [15,20]
		score = 0
		win.addch(apple_position[0], apple_position[1], curses.ACS_DIAMOND)
		prev_direction = 1
		direction = 1
		if gui:
			key = curses.KEY_RIGHT
		steps = 0
		steps_without_apple = 0
		while True:
			win.border(0)
			win.timeout(speed)
			if gui:
				next_key = win.getch()
				if next_key == -1:
					key = key
				else:
					key = next_key
				win.addch(1, 1, 'S')
				win.addch(1, 2, 'C')
				win.addch(1, 3, 'O')
				win.addch(1, 4, 'R')
				win.addch(1, 5, 'E')
				win.addch(1, 6, ':')
				for i in range(len(str(score))):
					win.addch(1, 7+i, str(score)[i])
			actions = [move_right, move_up, move_left, move_down]
			features = []
			features+=check_down(snake_head, snake_position, apple_position)
			features+=check_up(snake_head, snake_position, apple_position)
			features+=check_left_down(snake_head, snake_position, apple_position)
			features+=check_left_forward(snake_head, snake_position, apple_position)
			features+=check_left_up(snake_head, snake_position, apple_position)
			features+=check_right_down(snake_head, snake_position, apple_position)
			features+=check_right_forward(snake_head, snake_position, apple_position)
			features+=check_right_up(snake_head, snake_position, apple_position)
			features+=[check_front_close(snake_head, snake_position, direction), 
			check_left_close(snake_head, snake_position, direction), 
			check_right_close(snake_head, snake_position, direction),
			angle_with_apple(snake_position, apple_position)]
			action = network.activate(tuple(features))
			action = actions[np.argmax(np.array(action))]
			res = action(snake_head, prev_direction, direction)
			direction = res[1]
			snake_head = res[0]
			prev_direction = direction
			if snake_head == apple_position:
				apple_position, score = collision_with_apple(score, snake_position)
				snake_position.insert(0, list(snake_head))
				win.addch(apple_position[0], apple_position[1], curses.ACS_DIAMOND)
				steps_without_apple = 0
			else:
				snake_position.insert(0, list(snake_head))
				last = snake_position.pop()
				win.addch(last[0], last[1], ' ')
				steps_without_apple += 1
			if steps_without_apple >= 300:
				break 
			win.addch(snake_position[0][0], snake_position[0][1], 'O')
			if collision_with_boundaries(snake_head) == 1 or collision_with_self(snake_position) == 1:
				break
			steps += 1
		fitness += fitness_func(steps, score)
		curses.endwin()
	return fitness / iterations
