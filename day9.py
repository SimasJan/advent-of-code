#SOURCE: https://adventofcode.com/2021/day/6
def simulate_lanternfish(fishes, days):
	for day in range(days):
		index = 0
		endIndex = len(fishes)
		while index < endIndex:
			if fishes[index] == 0:
				fishes[index] = 6
				fishes.append(8)
			else:
				fishes[index] -= 1
			index += 1
	# print(f'{len(fishes)}')
	return fishes

	# print(f'Total lanternfish after 80 days: {len(fishes)}')
	return fishes


def test_simulate_lanternfish_base_case(base_case_no=0):
	EXAMPLE_INITIAL_STATE = [3,4,3,1,2]
	EXAMPLE_NO_OF_DAYS = 18
	EXAMPLE_RESULT_LST = [6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8]
	# base case test
	if base_case_no == 0:
		res = simulate_lanternfish(EXAMPLE_INITIAL_STATE, EXAMPLE_NO_OF_DAYS)
		assert res == EXAMPLE_RESULT_LST, "Base case #1 failed!. Result list = {}".format(len(res))
	
	elif base_case_no == 1:
		EXAMPLE_NO_OF_DAYS = 80
		res = simulate_lanternfish(EXAMPLE_INITIAL_STATE, EXAMPLE_NO_OF_DAYS)
		assert len(res) == 5934, "Base case #2 failed!. Result list = {}".format(len(res))



def test_simulate_lanternfish():
	INPUT_VALUES = [3,5,3,1,4,4,5,5,2,1,4,3,5,1,3,5,3,2,4,3,5,3,1,1,2,1,4,5,3,1,4,5,4,3,3,4,3,1,1,2,2,4,1,1,4,3,4,4,2,4,3,1,5,1,2,3,2,4,4,1,1,1,3,3,5,1,4,5,5,2,5,3,3,1,1,2,3,3,3,1,4,1,5,1,5,3,3,1,5,3,4,3,1,4,1,1,1,2,1,2,3,2,2,4,3,5,5,4,5,3,1,4,4,2,4,4,5,1,5,3,3,5,5,4,4,1,3,2,3,1,2,4,5,3,3,5,4,1,1,5,2,5,1,5,5,4,1,1,1,1,5,3,3,4,4,2,2,1,5,1,1,1,4,4,2,2,2,2,2,5,5,2,4,4,4,1,2,5,4,5,2,5,4,3,1,1,5,4,5,3,2,3,4,1,4,1,1,3,5,1,2,5,1,1,1,5,1,1,4,2,3,4,1,3,3,2,3,1,1,4,4,3,2,1,2,1,4,2,5,4,2,5,3,2,3,3,4,1,3,5,5,1,3,4,5,1,1,3,1,2,1,1,1,1,5,1,1,2,1,4,5,2,1,5,4,2,2,5,5,1,5,1,2,1,5,2,4,3,2,3,1,1,1,2,3,1,4,3,1,2,3,2,1,3,3,2,1,2,5,2]
	DAYS = 80
	res = simulate_lanternfish(INPUT_VALUES, DAYS)
	print(f'Total fishes after {DAYS} = {len(res)}')


if __name__ == "__main__":
	# test_simulate_lanternfish_base_case(0)
	# test_simulate_lanternfish_base_case(1)
	# test_simulate_lanternfish()