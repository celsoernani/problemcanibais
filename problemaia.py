import math

class State():
	def __init__(self, cannibalLeft, missionaryLeft, boat, cannibalRight, missionaryRight):
		self.cannibalLeft = cannibalLeft
		self.missionaryLeft = missionaryLeft
		self.boat = boat
		self.cannibalRight = cannibalRight
		self.missionaryRight = missionaryRight
		self.parent = None

	def is_goal(self):
		if self.cannibalLeft == 0 and self.missionaryLeft == 0:
			return True
		else:
			return False

	def is_valid(self):
		if self.missionaryLeft >= 0 and self.missionaryRight >= 0 \
                   and self.cannibalLeft >= 0 and self.cannibalRight >= 0 \
                   and (self.missionaryLeft == 0 or self.missionaryLeft >= self.cannibalLeft) \
                   and (self.missionaryRight == 0 or self.missionaryRight >= self.cannibalRight):
			return True
		else:
			return False

	def __eq__(self, other):
		return self.cannibalLeft == other.cannibalLeft and self.missionaryLeft == other.missionaryLeft \
                   and self.boat == other.boat and self.cannibalRight == other.cannibalRight \
                   and self.missionaryRight == other.missionaryRight

	def __hash__(self):
		return hash((self.cannibalLeft, self.missionaryLeft, self.boat, self.cannibalRight, self.missionaryRight))

def successors(cur_state):
	children = [];
	if cur_state.boat == 'left':
		new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft - 2, 'right',
                                  cur_state.cannibalRight, cur_state.missionaryRight + 2)
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft - 2, cur_state.missionaryLeft, 'right',
                                  cur_state.cannibalRight + 2, cur_state.missionaryRight)
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft - 1, cur_state.missionaryLeft - 1, 'right',
                                  cur_state.cannibalRight + 1, cur_state.missionaryRight + 1)
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft - 1, 'right',
                                  cur_state.cannibalRight, cur_state.missionaryRight + 1)
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft - 1, cur_state.missionaryLeft, 'right',
                                  cur_state.cannibalRight + 1, cur_state.missionaryRight)
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
	else:
		new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft + 2, 'left',
                                  cur_state.cannibalRight, cur_state.missionaryRight - 2)
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft + 2, cur_state.missionaryLeft, 'left',
                                  cur_state.cannibalRight - 2, cur_state.missionaryRight)
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft + 1, cur_state.missionaryLeft + 1, 'left',
                                  cur_state.cannibalRight - 1, cur_state.missionaryRight - 1)
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft + 1, 'left',
                                  cur_state.cannibalRight, cur_state.missionaryRight - 1)
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft + 1, cur_state.missionaryLeft, 'left',
                                  cur_state.cannibalRight - 1, cur_state.missionaryRight)
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
	return children

def breadth_first_search():
	initial_state = State(3,3,'left',0,0)
	if initial_state.is_goal():
		return initial_state
	frontier = list()
	explored = set()
	frontier.append(initial_state)
	while frontier:
		state = frontier.pop(0)
		if state.is_goal():
			return state
		explored.add(state)
		children = successors(state)
		for child in children:
			if (child not in explored) or (child not in frontier):
				frontier.append(child)
	return None

def print_solution(solution):
		path = []
		path.append(solution)
		parent = solution.parent
		while parent:
			path.append(parent)
			parent = parent.parent

		for t in range(len(path)):
			state = path[len(path) - t - 1]
			print ("(" + str(state.cannibalLeft) + "," + str(state.missionaryLeft) \
                              + "," + state.boat + "," + str(state.cannibalRight) + "," + \
                              str(state.missionaryRight) + ")")
#FORÇA BRUTA COM LISTAS -> TODO IMPLEMNTAR SEM SER SOMA, MAS COM APPEND E REMOVE IN LISTS
def brute_force():
    mission = [1,1,1]
    canibais = [2,2,2]
    barco = []
    margem1 = [mission, canibais]
    margem2 = []
    barco = [mission[0], canibais[0]]
    margem1[0].remove(1)
    margem1[1].remove(2)
    margem2.append(barco[1])
    barco.remove(2)
    margem1[0].append(barco[0])
    barco.remove(1)
    barco.append(margem1[1][0])
    barco.append(margem1[1][0])
    margem1[1].remove(2)
    margem1[1].remove(2)
    margem2.append(barco[0])
    barco.remove(2)
    margem1[1].append(barco[0])
    barco.remove(2)
    barco.append(margem1[0][0])
    barco.append(margem1[0][1])
    margem1[0].remove(1)
    margem1[0].remove(1)
    margem2.append(barco[0])
    margem2.remove(2)
    barco.remove(1)
    barco.append(margem2[0])
    margem1[1].append(barco[1])
    barco.remove(2)
    barco.append(margem1[0][0])
    margem1[0].remove(1)
    margem2.append(barco[0])
    margem2.append(barco[1])
    barco.remove(1)
    barco.remove(1)
    barco.append(margem2[0])
    margem2.remove(2)
    barco.append(margem1[1][0])
    margem1[1].remove(2)
    margem2.append(barco[0])
    barco.remove(2)
    barco.append(margem1[1][0])
    margem1[1].remove(2)
    margem2.append(barco[0])
    margem2.append(barco[1])
    barco.remove(2)
    barco.remove(2)
    print("Atualmente a margem1 contem: " , margem1)
    print("Atualmente a margem2 contem: " , margem2)
    print("Atualmente o barco contem: " , barco)


def main():
	solution = breadth_first_search()
	print_solution(solution)
    # brute_force()
if __name__ == "__main__":
    main()

