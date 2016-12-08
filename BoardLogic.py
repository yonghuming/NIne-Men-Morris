from MorrisState import *


def adjacentPositions(position):
	'''
	Return pieces adjacent to the piece at position
	@param position: index of the piece
	'''
	adjacent = [
		[1, 3],
		[0, 2, 9],
		[1, 4],
		[0, 5, 11],
		[2, 7, 12],
		[3, 6],
		[5, 7, 14],
		[4, 6],
		[9, 11],
		[1, 8, 10, 17],
		[9, 12],
		[3, 8, 13, 19],
		[4, 10, 15, 20],
		[11, 14],
		[6, 13, 15, 22],
		[12, 14],
		[17, 19],
		[9, 16, 18],
		[17, 20],
		[11, 16, 21],
		[12, 18, 23],
		[19, 22],
		[21, 23, 14],
		[20, 22]
	]
	return adjacent[position]


def isMill(player, board, pos1, pos2):
	'''
	Return True if pos1 and pos2 on board both belong to player
	@param player: string representation of the board piece color
	@param board: current MorrisState
	@param pos1: first position index
	@param pos2: second position index
	'''
	if (board.getPositionValue(pos1) == player \
		and board.getPositionValue(pos2) == player):
		return True
	return False


def checkMill(position, board, player):
	'''
	Return True if there's a mill at position for player on given board
	@param position: the index of the position we're checking
	@param board: the MorrisState of the current board
	@param player: string representation of the board piece color
	'''
	mill = [
		(isMill(player, board, 1, 2) or isMill(player, board, 3, 5)),
		(isMill(player, board, 0, 2) or isMill(player, board, 9, 17)),
		(isMill(player, board, 0, 1) or isMill(player, board, 4, 7)),
		(isMill(player, board, 0, 5) or isMill(player, board, 11, 19)),
		(isMill(player, board, 2, 7) or isMill(player, board, 12, 20)),
		(isMill(player, board, 0, 3) or isMill(player, board, 6, 7)),
		(isMill(player, board, 5, 7) or isMill(player, board, 14, 22)),
		(isMill(player, board, 2, 4) or isMill(player, board, 5, 6)),
		(isMill(player, board, 9, 10) or isMill(player, board, 11, 13)),
		(isMill(player, board, 8, 10) or isMill(player, board, 1, 17)),
		(isMill(player, board, 8, 9) or isMill(player, board, 12, 15)),
		(isMill(player, board, 3, 19) or isMill(player, board, 8, 13)),
		(isMill(player, board, 20, 4) or isMill(player, board, 10, 15)),
		(isMill(player, board, 8, 11) or isMill(player, board, 14, 15)),
		(isMill(player, board, 13, 15) or isMill(player, board, 6, 22)),
		(isMill(player, board, 13, 14) or isMill(player, board, 10, 12)),
		(isMill(player, board, 17, 18) or isMill(player, board, 19, 21)),
		(isMill(player, board, 1, 9) or isMill(player, board, 16, 18)),
		(isMill(player, board, 16, 17) or isMill(player, board, 20, 23)),
		(isMill(player, board, 16, 21) or isMill(player, board, 3, 11)),
		(isMill(player, board, 12, 4) or isMill(player, board, 18, 23)),
		(isMill(player, board, 16, 19) or isMill(player, board, 22, 23)),
		(isMill(player, board, 6, 14) or isMill(player, board, 21, 23)),
		(isMill(player, board, 18, 20) or isMill(player, board, 21, 22)),
	]
	return mill[position]


def hasMill(position, board):
	'''
	Return True if any player has a mill on position
	@param position: the index of the position we're checking
	@param board: the MorrisState of the current board
	'''
	player = board.getPositionValue(position):
	# if position is not empty
	if (player != "-"):
		return checkMill(position, board, player)
	return False

def addPieces(MorrisState board):
	'''
	'''
	board_list = []

	for i in range(len(board.gameboard)):
		# fill empty positions with white
		if (board.getPositionValue(i) == "-"):
			board_clone = board.getCloneBoard()
			board_clone.setValue("2", i)

			if (isMill(i, board_clone)):
				board_list = removePiece(board_clone, board_list)
			else:
				board_list.append(boardCopy)
	return board_list


def removePiece(board_clone, board_list):
	'''
	'''
	for i in range(len(board_clone.gameboard)):
		if (board_clone.getPositionValue(i) == "1"):

			if !isMill(i, board_clone):
				new_board = board_clone.getPositionValue()
				new_board.setPositionValue("-", i)
				board_list.add(new_board)
	return board_list


def addPiecesStage2(board):
	'''

	@param board: current MorrisState
	'''
	board_list = []
	for i in range(len(board.gameboard)):
		if (board.getPositionValue(i) == "2"):
			adjacent_list = adjacentPositions(i)

			for pos in adjacent_list:
				if (board.getPositionValue(pos) == "-"):
					board_clone = board.getCloneBoard()
					board_clone.setPositionValue("-", i)
					board_clone.setPositionValue("2", pos)

					if isMill(pos, board_clone):
						board_list = removePiece(board_clone, board_list)
					else:
						board_list.append(board_clone)
	return board_list


def addPiecesStage3(board):
	'''
	'''
	board_list = []

	for i in range(len(board.gameboard)):
		if (board.getPositionValue(i) == "2"):

			for j in range(len(board.gameboard)):
				if (board.getPositionValue(j) == "-"):
					board_clone = board.getCloneBoard()

					board_clone.setPositionValue("-", i)
					board_clone.setPositionValue("2", j)

					if (isMill(j, board_clone)):
						board_list = removePiece(board_clone, board_list)
					else:
						board_list.append(board_clone)
	return board_list


def addPiecesStage1(board):
	'''
	'''
	return addPieces(board)


def addPiecesStage1Player1(board):
	'''
	'''
	inv_board = board.InvertedBoard()

	positions = addPiecesStage1(inv_board)
	possible_moves = generateInvertedBoards(positions)

	return possible_moves


def addPiecesStage23(board):
	if (board.getNumPieces("2") == _END_GAME_PIECES):
		return addPiecesStage3(board)
	else:
		addPiecesStage2(board)


def addPiecesStage23Player1(board):
	'''
	'''
	inv_Board = board.InvertedBoard()

	return generateInvertedBoards(addPiecesStage23(inv_board))


def generateInvertedBoards(black_positions):
	'''
	'''
	for i in range(len(black_positions)):
		temp = black_positions[i].InvertedBoard()
		black_positions[i] = temp

	return black_positions


def getPossibleMills(board, player):
	'''
	'''
	mills = 0

	for i in range(len(board.gameboard)):
		if (board.getPositionValue(i) == "-"):
			if checkMill(i, board, player):
				mills += 1
	return mills


def getEvaluationStage1(board):
	'''
	'''
	pieces1 = board.getNumPieces("1")
	pieces2 = board.getNumPieces("2")
	mills = getPossibleMills(board, "2")

	return pieces2 - pieces1 + mills


def getEvaluationStage23(board):
	'''
	'''
	pieces1 = board.getNumPieces("1")
	pieces2 = board.getNumPieces("2")
	mills = getPossibleMills(board, "2")

	evaluation = 0

	board_list = addPiecesStage23(board)

	moves1 = len(board_list)

	if (pieces1 <= 2):
		evaluation = 10000
	elif moves1 == 0:
		evaluation = 10000
	elif pieces2 <= 2:
		evaluation = -10000
	else:
		evaluation = (1000 * (pieces2 + mills - pieces1) - moves1)
	return evaluation


def potentialMill(position, board, player):
	'''
	'''
	adjacent_list = adjacentPositions(position)

	for i in adjacent_list:
		if (board.getPositionValue(i) == player) \
			and (!checkMill(position, board, player)):
			return True
	return False


def getPiecesInPotentialMill(board, player):
	'''
	'''
	count = 0

	for i in range(len(board.gameboard)):
		if (board.getPositionValue(i) == player):
			adjacent_list = adjacentPositions(i)
			for pos in adjacent_list:
				if (player == "2"):
					if (board.getPositionValue(pos) == "1"):
						board.setPositionValue("1", i)
						if hasMill(i, board):
							count += 1
						board.setPositionValue(player, i)
				else:
					if (board.getPositionValue(pos) == "2" \
						and potentialMill(pos, board, "2")):
						count += 1
	return count


def getEvaluationImproved(board, isStage1):
	'''
	'''
	evaluation = 0

	pieces1 = board.getNumPieces("1")
	pieces2 = board.getNumPieces("2")

	possible_mills1 = getPossibleMills(board, "1")
	possible_mills2 = getPossibleMills(board, "2")

	moves1 = 0
	moves2 = 0

	if (!isStage1):
		board_list1 = addPiecesStage23Player1(board)

		moves1 = len(board_list1)

	potential_mills1 = getPiecesInPotentialMill(board, "1")
	potential_mills2 = getPiecesInPotentialMill(board, "2")

	if (!isStage1):
		if pieces1 <= 2:
			evaluation = 100000
		elif (moves1 == 0):
			evaluation = 100000
		elif (pieces2 <= 2):
			evaluation = -100000
		else:
			evaluation = 100 * (pieces2 - pieces1)
			if (pieces2 < 4):
				evaluation += 500 * possible_mills2
				evaluation += 1000 * potential_mills1
			else:
				evaluation += 1000 * possible_mills2
				evaluation += 500 * potential_mills1
			evaluation -= 10 * moves1
	else:
		evaluation = 100 * pieces2 - pieces1
		if pieces2 < 4:
			evaluation += 500 * possible_mills2
			evaluation += 1000 * potential_mills1
		else:
			evaluation += 1000 * possible_mills2
			evaluation += 500 * potential_mills1
		evaluation -= 10 * moves1
	return evaluation

if __name__ == "__main__":
	for i in range(24):
		print(checkMill(i, MorrisState(["1" for i in range(24)]), "2"))