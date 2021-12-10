# Intro Source: https://adventofcode.com/2021/day/2
from typing import List, Tuple, Dict


def navigate_submarine(course_values: str, pos:int=0, verbose=False):
	navigation_value_list = [tuple(x.split(' ')) for x in course_values]

	starting_pos = pos # multiply horiztonal and depth position to get the value
	horizontal_pos = starting_pos
	depth_pos = starting_pos
	position_product = horizontal_pos * depth_pos
	
	if verbose:
		print('Starting positions (Horz./Ver.): {}/{}'.format(horizontal_pos, depth_pos))
		print('Position product: ', position_product)

	for value in navigation_value_list:
		direction, pos_value = value 		# position direction and value
		pos_value = int(pos_value)			# convert to int

		# TODO: doesn't work below as expected on the base case.
		if direction == 'forward':
			horizontal_pos += pos_value
		elif direction == 'down':
			depth_pos += pos_value
		elif direction == 'up':
			depth_pos -= pos_value
		
		# print out the updated submarine position
		if verbose:
			print('Updated position (horizontal/vertical): {}/{}'.format(horizontal_pos, depth_pos))

	position_product = horizontal_pos * depth_pos
	print('Updated position (horizontal/vertical): {}/{}'.format(horizontal_pos, depth_pos))
	print('Position product: ', position_product)
	return position_product

def navigate_submarine_2(course_values: str, pos:int=0, verbose=False):
	navigation_value_list = [tuple(x.split(' ')) for x in course_values]

	aim = pos			# down X = +X; up X = -X; forward X = hor +X & depth +(aim *X)
	starting_pos = pos 	# multiply horiztonal and depth position to get the value
	
	horizontal_pos = starting_pos
	depth_pos = starting_pos
	position_product = horizontal_pos * depth_pos
	
	if verbose:
		print('Starting positions (hor/depth/aim): {}/{}/{}/{}'.format(horizontal_pos, depth_pos, aim))
		# print('Position product: ', position_product)

	for value in navigation_value_list:
		direction, pos_value = value 		# position direction and value
		pos_value = int(pos_value)			# convert to int
		print('>' ,direction, pos_value, aim)

		if direction == 'down':
			depth_pos += pos_value
			aim += pos_value
		elif direction == 'up':
			depth_pos -= pos_value
			aim -= pos_value

		if direction == 'forward':
			depth_pos = (aim * pos_value)
			horizontal_pos += pos_value
		
		# print out the updated submarine position
		if verbose:
			print('Updated position (hor/depth/aim/product): {}/{}/{}/{}'.format(horizontal_pos, depth_pos, aim, position_product))

	position_product = horizontal_pos * depth_pos
	print('Updated position (hor/depth/aim/product): {}/{}/{}'.format(horizontal_pos, depth_pos, aim, position_product))
	# print('Position product: ', position_product)
	return position_product


def main(which_part=1):
	## INPUTS
	if which_part not in (1,2):
		raise Exception("InvalidArgument: Only '1' or '2' is valid, you passed: %s " % which_part)

	base_case = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
	actual_case = ['forward 4', 'down 8', 'down 8', 'up 2', 'up 7', 'forward 5', 'forward 5', 'up 7', 'down 6', 'down 3', 'down 1', 'forward 5', 'forward 9', 'up 2', 'down 9', 'forward 4', 'up 5', 'forward 7', 'down 2', 'forward 7', 'down 2', 'forward 4', 'up 3', 'down 9', 'up 8', 'down 2', 'down 6', 'up 1', 'forward 3', 'down 6', 'down 2', 'forward 9', 'up 1', 'forward 5', 'down 1', 'forward 2', 'up 2', 'forward 4', 'down 3', 'down 8', 'up 2', 'down 3', 'up 4', 'down 8', 'forward 7', 'forward 9', 'down 7', 'down 1', 'forward 5', 'up 3', 'down 6', 'down 6', 'forward 1', 'down 9', 'forward 6', 'forward 9', 'forward 2', 'forward 5', 'forward 7', 'down 1', 'up 6', 'up 7', 'forward 8', 'forward 6', 'forward 2', 'down 5', 'up 3', 'up 4', 'down 9', 'up 4', 'down 9', 'up 4', 'down 5', 'forward 3', 'down 8', 'up 2', 'down 2', 'forward 7', 'down 7', 'forward 6', 'down 2', 'forward 5', 'down 1', 'forward 9', 'down 9', 'down 5', 'forward 2', 'forward 3', 'forward 6', 'forward 1', 'down 8', 'forward 2', 'forward 1', 'forward 9', 'down 8', 'forward 8', 'up 1', 'up 2', 'forward 2', 'forward 7', 'down 2', 'up 9', 'forward 5', 'forward 5', 'up 5', 'down 1', 'up 8', 'forward 3', 'up 5', 'forward 2', 'up 8', 'up 7', 'forward 4', 'down 6', 'up 1', 'up 6', 'forward 5', 'down 8', 'forward 4', 'down 7', 'forward 5', 'down 4', 'down 9', 'forward 2', 'down 5', 'down 2', 'down 3', 'forward 8', 'down 8', 'down 2', 'down 5', 'down 6', 'up 8', 'down 1', 'up 7', 'up 4', 'up 1', 'up 6', 'forward 6', 'forward 6', 'forward 8', 'up 5', 'forward 4', 'forward 5', 'forward 3', 'down 8', 'forward 9', 'forward 6', 'forward 6', 'up 1', 'up 8', 'forward 2', 'up 9', 'down 1', 'up 7', 'up 3', 'down 3', 'forward 2', 'down 5', 'up 8', 'forward 3', 'up 5', 'down 3', 'down 3', 'up 7', 'forward 2', 'forward 3', 'forward 6', 'forward 9', 'up 3', 'forward 1', 'up 9', 'down 8', 'forward 5', 'down 8', 'forward 9', 'down 1', 'forward 7', 'forward 9', 'forward 2', 'down 6', 'up 6', 'down 2', 'down 1', 'forward 7', 'down 3', 'forward 3', 'down 3', 'forward 1', 'forward 6', 'forward 1', 'down 4', 'down 4', 'down 5', 'forward 3', 'forward 1', 'up 8', 'forward 7', 'down 6', 'up 6', 'down 5', 'up 6', 'down 3', 'down 8', 'down 9', 'forward 2', 'up 8', 'forward 1', 'forward 2', 'forward 7', 'forward 5', 'up 6', 'down 9', 'up 9', 'forward 7', 'forward 6', 'forward 7', 'down 8', 'down 6', 'forward 5', 'down 2', 'down 5', 'down 3', 'down 4', 'up 5', 'down 5', 'forward 7', 'forward 2', 'down 1', 'forward 6', 'up 8', 'down 3', 'down 5', 'down 3', 'forward 3', 'up 2', 'forward 9', 'forward 2', 'up 4', 'down 3', 'down 7', 'forward 9', 'forward 6', 'up 1', 'up 2', 'down 5', 'up 8', 'forward 9', 'forward 2', 'down 3', 'down 6', 'up 3', 'down 9', 'down 2', 'up 4', 'down 3', 'up 7', 'forward 3', 'up 9', 'down 3', 'down 9', 'down 1', 'down 1', 'forward 7', 'down 9', 'forward 3', 'up 6', 'down 8', 'down 3', 'forward 7', 'forward 1', 'up 4', 'forward 8', 'forward 1', 'forward 9', 'up 9', 'forward 4', 'up 2', 'down 6', 'down 5', 'down 8', 'down 2', 'down 4', 'forward 5', 'down 8', 'down 1', 'forward 5', 'forward 9', 'down 4', 'forward 5', 'forward 4', 'forward 4', 'up 6', 'down 7', 'down 2', 'forward 8', 'down 7', 'forward 7', 'forward 7', 'forward 3', 'down 3', 'forward 6', 'down 5', 'down 5', 'forward 3', 'down 7', 'up 3', 'up 6', 'forward 8', 'down 3', 'down 6', 'forward 5', 'forward 4', 'down 4', 'down 3', 'down 1', 'down 4', 'down 2', 'forward 1', 'forward 5', 'down 9', 'forward 8', 'down 7', 'forward 4', 'down 5', 'down 5', 'forward 7', 'forward 9', 'down 5', 'down 8', 'up 9', 'forward 1', 'down 9', 'up 1', 'down 8', 'forward 4', 'up 8', 'up 7', 'down 4', 'forward 2', 'forward 9', 'up 9', 'forward 4', 'forward 5', 'forward 5', 'forward 4', 'forward 4', 'down 8', 'forward 3', 'forward 3', 'forward 1', 'forward 7', 'forward 7', 'up 2', 'forward 9', 'down 8', 'forward 3', 'down 3', 'down 3', 'down 4', 'forward 9', 'forward 9', 'forward 7', 'forward 9', 'down 6', 'forward 6', 'down 4', 'forward 7', 'down 3', 'forward 2', 'down 9', 'down 9', 'up 2', 'down 7', 'down 6', 'up 5', 'forward 6', 'forward 5', 'down 9', 'forward 8', 'down 9', 'forward 9', 'down 7', 'up 8', 'forward 5', 'forward 1', 'down 5', 'forward 1', 'down 4', 'up 6', 'up 1', 'down 5', 'forward 3', 'down 1', 'up 7', 'down 8', 'up 5', 'down 8', 'up 6', 'forward 6', 'down 8', 'up 2', 'forward 5', 'down 5', 'down 7', 'down 7', 'forward 8', 'forward 6', 'forward 2', 'forward 3', 'forward 3', 'forward 9', 'down 7', 'up 8', 'up 1', 'forward 8', 'down 5', 'down 7', 'forward 2', 'down 9', 'down 5', 'down 5', 'forward 6', 'forward 1', 'forward 8', 'down 3', 'down 3', 'down 7', 'up 3', 'down 3', 'down 5', 'down 1', 'forward 3', 'forward 2', 'forward 4', 'forward 1', 'forward 3', 'forward 6', 'down 6', 'down 4', 'forward 2', 'down 8', 'up 1', 'down 7', 'down 6', 'down 3', 'down 6', 'forward 8', 'up 7', 'down 7', 'up 7', 'down 1', 'forward 2', 'forward 9', 'up 8', 'down 2', 'down 3', 'down 7', 'down 2', 'up 2', 'down 1', 'down 7', 'up 6', 'down 4', 'forward 9', 'down 8', 'down 1', 'forward 5', 'forward 1', 'up 7', 'up 9', 'up 9', 'down 5', 'down 7', 'down 2', 'down 6', 'down 3', 'forward 8', 'forward 4', 'up 3', 'down 9', 'up 3', 'down 6', 'up 8', 'forward 7', 'down 7', 'up 5', 'down 1', 'down 3', 'up 4', 'forward 2', 'down 7', 'down 3', 'down 7', 'up 1', 'forward 8', 'down 3', 'forward 7', 'down 8', 'forward 5', 'forward 8', 'down 8', 'up 4', 'up 8', 'forward 3', 'down 7', 'up 6', 'down 9', 'forward 4', 'forward 4', 'forward 3', 'up 4', 'down 4', 'down 7', 'forward 6', 'down 7', 'down 8', 'up 5', 'down 4', 'up 6', 'up 6', 'up 4', 'down 7', 'forward 7', 'up 4', 'down 2', 'up 2', 'forward 6', 'down 5', 'down 1', 'forward 2', 'up 1', 'down 4', 'up 2', 'down 7', 'down 5', 'up 5', 'forward 6', 'up 2', 'forward 2', 'up 9', 'up 4', 'down 1', 'down 3', 'up 7', 'up 5', 'down 9', 'down 2', 'forward 9', 'down 1', 'up 9', 'down 4', 'down 8', 'forward 3', 'forward 1', 'forward 4', 'forward 9', 'down 5', 'down 5', 'down 8', 'up 4', 'up 1', 'down 9', 'up 4', 'forward 9', 'up 1', 'forward 7', 'down 4', 'up 2', 'down 1', 'forward 9', 'down 9', 'down 2', 'forward 8', 'up 2', 'forward 6', 'down 1', 'up 9', 'down 3', 'down 2', 'down 8', 'down 2', 'forward 8', 'forward 2', 'forward 8', 'down 3', 'up 6', 'forward 5', 'forward 4', 'forward 7', 'forward 1', 'down 8', 'forward 7', 'down 9', 'up 7', 'up 5', 'forward 1', 'down 6', 'down 6', 'up 9', 'up 9', 'up 1', 'forward 1', 'forward 5', 'up 1', 'forward 2', 'down 8', 'up 9', 'forward 2', 'forward 8', 'down 2', 'up 5', 'up 9', 'down 5', 'forward 2', 'forward 4', 'forward 2', 'up 7', 'down 9', 'forward 5', 'down 1', 'down 6', 'up 1', 'forward 8', 'down 1', 'down 7', 'up 2', 'forward 4', 'down 2', 'up 6', 'forward 6', 'forward 3', 'down 3', 'forward 2', 'down 2', 'up 9', 'forward 2', 'up 1', 'down 9', 'down 4', 'up 8', 'forward 3', 'down 9', 'down 9', 'forward 9', 'forward 8', 'up 8', 'down 8', 'up 8', 'forward 4', 'down 9', 'up 5', 'forward 8', 'up 6', 'forward 7', 'up 6', 'down 2', 'down 3', 'forward 9', 'forward 5', 'down 6', 'forward 9', 'down 5', 'down 9', 'down 7', 'down 9', 'down 3', 'forward 4', 'forward 2', 'down 2', 'down 7', 'down 7', 'up 2', 'up 3', 'forward 6', 'up 7', 'forward 4', 'down 3', 'forward 2', 'down 1', 'down 8', 'forward 5', 'down 3', 'up 9', 'forward 2', 'forward 7', 'down 4', 'forward 1', 'forward 8', 'forward 9', 'forward 5', 'down 4', 'up 3', 'up 9', 'forward 6', 'forward 4', 'forward 9', 'down 3', 'forward 1', 'forward 9', 'down 9', 'down 5', 'forward 9', 'forward 4', 'down 3', 'down 9', 'down 5', 'up 6', 'up 5', 'forward 5', 'up 8', 'down 3', 'forward 7', 'up 3', 'forward 9', 'down 8', 'forward 2', 'forward 1', 'forward 9', 'down 9', 'forward 1', 'down 6', 'forward 7', 'up 3', 'forward 7', 'up 3', 'down 1', 'forward 5', 'forward 5', 'up 3', 'forward 2', 'down 3', 'forward 8', 'up 9', 'forward 7', 'down 7', 'forward 5', 'up 4', 'forward 8', 'down 1', 'up 4', 'down 2', 'forward 2', 'down 5', 'down 5', 'up 2', 'forward 1', 'down 3', 'down 8', 'forward 6', 'forward 6', 'down 5', 'up 4', 'down 7', 'down 9', 'up 9', 'forward 7', 'forward 4', 'down 7', 'down 5', 'down 2', 'down 9', 'down 6', 'down 7', 'up 6', 'up 7', 'up 6', 'down 4', 'forward 9', 'down 8', 'down 7', 'down 8', 'down 4', 'forward 5', 'forward 1', 'up 5', 'forward 5', 'forward 4', 'down 3', 'forward 8', 'down 7', 'down 9', 'up 1', 'down 1', 'up 8', 'up 6', 'down 9', 'up 9', 'down 9', 'forward 7', 'down 3', 'forward 6', 'down 6', 'forward 6', 'down 9', 'down 7', 'up 1', 'down 2', 'up 2', 'down 3', 'down 1', 'up 4', 'forward 3', 'down 3', 'up 8', 'down 3', 'forward 3', 'forward 6', 'forward 6', 'forward 6', 'forward 7', 'up 2', 'forward 6', 'forward 1', 'up 4', 'up 7', 'down 5', 'down 9', 'forward 6', 'down 4', 'forward 6', 'down 7', 'down 2', 'up 9', 'up 3', 'forward 8', 'forward 5', 'down 1', 'down 6', 'down 7', 'down 5', 'up 3', 'up 9', 'forward 2', 'forward 5', 'down 3', 'down 2', 'up 2', 'forward 6', 'forward 3', 'down 8', 'forward 7', 'up 6', 'forward 4', 'down 8', 'forward 6', 'down 7', 'forward 9', 'forward 6', 'forward 2', 'forward 4', 'up 5', 'up 1', 'forward 3', 'forward 2', 'up 3', 'down 4', 'down 3', 'down 1', 'up 8', 'forward 6', 'down 4', 'down 9', 'down 3', 'up 8', 'down 5', 'forward 2', 'down 3', 'up 7', 'down 3', 'up 1', 'up 1', 'up 2', 'up 1', 'forward 4', 'forward 1', 'forward 4', 'forward 3', 'forward 8', 'down 8', 'up 5', 'down 4', 'down 4', 'down 6', 'down 9', 'down 7', 'forward 5', 'forward 3', 'up 3', 'forward 6', 'forward 5', 'forward 2', 'forward 6', 'up 4', 'forward 2', 'up 3', 'down 2', 'forward 3', 'down 8', 'forward 1', 'forward 2', 'down 3', 'down 5', 'forward 6', 'forward 3', 'forward 6', 'up 3', 'forward 5', 'forward 3', 'forward 5', 'down 6', 'down 4', 'down 4', 'forward 3', 'forward 3', 'up 6', 'up 8', 'forward 5', 'forward 1', 'down 3', 'down 8', 'down 9', 'up 3', 'down 7', 'forward 4', 'forward 2', 'down 2', 'up 6', 'down 1', 'down 8', 'forward 3', 'up 1', 'down 7', 'down 7', 'down 5', 'forward 3', 'down 8', 'forward 3', 'down 7', 'down 5', 'up 2', 'forward 9', 'down 8', 'down 5', 'forward 3', 'forward 2', 'forward 7', 'up 8', 'down 2', 'down 5', 'down 8', 'down 9', 'down 9', 'down 1', 'up 4', 'forward 5', 'up 1', 'up 4', 'forward 1', 'down 1', 'down 7', 'up 9', 'up 7', 'down 5', 'down 9', 'down 9', 'down 8', 'forward 7', 'down 3', 'up 4', 'down 7', 'down 8', 'forward 7', 'forward 4', 'up 9', 'down 2', 'up 7', 'forward 5', 'down 3', 'forward 3', 'forward 5', 'forward 5', 'down 2', 'down 2', 'down 7', 'up 8', 'up 9', 'down 1', 'forward 9', 'forward 3', 'up 3', 'forward 9', 'up 2', 'down 7', 'down 3', 'forward 4', 'down 5', 'down 3', 'up 5', 'forward 4']

	if which_part == 1:
		print('{} PART 1 {}'.format('>'*5, '<'*5))
		assert navigate_submarine(base_case) == 150,  "'{}' function failed!".format(navigate_submarine.__name__)	# base case
		navigate_submarine(actual_case)
	elif which_part == 2:
		print('{} PART 2 {}'.format('>'*5, '<'*5))
		print(navigate_submarine_2(base_case, verbose=True))
		# assert navigate_submarine_2(base_case, verbose=True) == 900, "'{}' function failed!".format(navigate_submarine_2.__name__)	# base case
		# navigate_submarine(actual_case)

if __name__ == '__main__':
	main(2)