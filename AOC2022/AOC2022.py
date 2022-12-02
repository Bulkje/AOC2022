def Day1():
	print("Day 1")
	f = open("day1.txt", "r")
	#f = open("test1.txt", "r")
	lines = f.readlines()

	i = 0
	elves = []
	elf = 0
	while i < len(lines):
		if lines[i] == '\n':
			elves.append(elf)
			elf = 0
		else:
			elf += int(lines[i])
		i += 1

	print("The elf with the most food carries", max(elves), "calories")

	highest = []
	highest.append(max(elves))
	elves.remove(max(elves))
	highest.append(max(elves))
	elves.remove(max(elves))
	highest.append(max(elves))

	print("The top 3 elves carry", sum(highest), "calories toghether\n\n")

def Day2_1():
	print("Day 2")
	# A for Rock = 1pnt
	# B for Paper = 2pts
	# C for Scissors = 3pts

	# X Rock
	# Y Paper
	# Z Scissors

	# 0pts for loss, 3pts for draw, 6pts for win
	
	f = open("day2.txt", "r")
	#f = open("test2.txt", "r")
	lines = f.readlines()
	
	Rock = 1
	Paper = 2
	Scissors = 3

	loss = 0
	draw = 3
	win = 6

	playerMoves = []
	opponentMoves = []
	

	for line in lines:
		if line[0] == 'A':
			opponentMoves.append(Rock)
		elif line[0] == 'B':
			opponentMoves.append(Paper)
		elif line[0] == 'C':
			opponentMoves.append(Scissors)

		if line[2] == 'X':
			playerMoves.append(Rock)
		elif line[2] == 'Y':
			playerMoves.append(Paper)
		elif line[2] == 'Z':
			playerMoves.append(Scissors)

	i = 0
	totalScore = sum(playerMoves)

	while i < len(playerMoves):
		if playerMoves[i] == opponentMoves[i]:
			totalScore += draw
		elif (playerMoves[i] == Rock and opponentMoves[i] == Scissors) or (playerMoves[i] == Paper and opponentMoves[i] == Rock) or (playerMoves[i] == Scissors and opponentMoves[i] == Paper):
			totalScore += win
		i += 1




	print("The total score is:", totalScore)

def Day2_2():
	print("Day 2")
	# A for Rock = 1pnt
	# B for Paper = 2pts
	# C for Scissors = 3pts

	# X lose
	# Y draw
	# Z win

	# 0pts for loss, 3pts for draw, 6pts for win
	
	f = open("day2.txt", "r")
	#f = open("test2.txt", "r")
	lines = f.readlines()
	
	Rock = 1
	Paper = 2
	Scissors = 3

	loss = 0
	draw = 3
	win = 6

	opponentMoves = []
	outcomes = []
	

	for line in lines:
		if line[0] == 'A':
			opponentMoves.append(Rock)
		elif line[0] == 'B':
			opponentMoves.append(Paper)
		elif line[0] == 'C':
			opponentMoves.append(Scissors)

		if line[2] == 'X':
			outcomes.append(loss)
		elif line[2] == 'Y':
			outcomes.append(draw)
		elif line[2] == 'Z':
			outcomes.append(win)

	i = 0
	totalScore = sum(outcomes)

	while i < len(outcomes):
		if outcomes[i] == draw:
			totalScore += opponentMoves[i]

		elif opponentMoves[i] == Rock:
			if outcomes[i] == loss:
				totalScore += Scissors
			else:
				totalScore += Paper

		elif opponentMoves[i] == Paper:
			if outcomes[i] == loss:
				totalScore += Rock
			else:
				totalScore += Scissors

		elif opponentMoves[i] == Scissors:
			if outcomes[i] == loss:
				totalScore += Paper
			else:
				totalScore += Rock
		i += 1

	print("The total score is:", totalScore)
	#5388 too low



Day2_2()
	