import time
import random


""" Initialize game data. """
# Game board.
board = [" " for i in range(9)]

# Available spaces on board.
available = [i for i in range(9)]

# Who starts the game?
starter = random.choice(["player", "computer"])


# Display the game board with the actual data.
def print_board():
	row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
	row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
	row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

	print()
	print(row1)
	print(row2)
	print(row3)
	print()


# Display a numbered board to help player.
def print_help_board():
	row1 = "| 1 | 2 | 3 |"
	row2 = "| 4 | 5 | 6 |"
	row3 = "| 7 | 8 | 9 |"

	print()
	print(row1)
	print(row2)
	print(row3)
	print()


# Logic for player movement.
def player_move():
	print("It's your move {}.".format(name))
	choice = int(input("Enter your move (1-9): ").strip())

	if board[choice - 1] == " ":
		board[choice - 1] = "X"

		# Update available spaces.
		available.remove(choice - 1)
	else:
		print()
		print("THAT SPACE IS TAKEN!\n")
		player_move()


# Logic for computer movement.
def computer_move():
	print("Computer is thinking...")
	time.sleep(2)

	# If center space is available, make the move.
	if board[4] == " ":
		choice = 4
	else:
		# Is it possible to win with a single move?
		choice = power_move("O")
		if choice == None:
			# Is it needed to defend from the opponent's winning move?
			choice = power_move("X")
			if choice == None:
				# Pick a random choice from the available spaces.
				choice = random.choice(available)

	# Make the move.
	board[choice] = "O"

	# Update available spaces.
	available.remove(choice)


# Check for victory (either player or computer).
def is_victory(icon):
	if (board[0] == icon and board[1] == icon and board[2] == icon) or \
	   (board[3] == icon and board[4] == icon and board[5] == icon) or \
	   (board[6] == icon and board[7] == icon and board[8] == icon) or \
	   (board[0] == icon and board[3] == icon and board[6] == icon) or \
	   (board[1] == icon and board[4] == icon and board[7] == icon) or \
	   (board[2] == icon and board[5] == icon and board[8] == icon) or \
	   (board[0] == icon and board[4] == icon and board[8] == icon) or \
	   (board[2] == icon and board[4] == icon and board[6] == icon):
		return True
	else:
		return False


# Check for a draw.
def is_draw():
	if " " not in board:
		return True
	else:
		return False


# Reset all game data for a new game.
def reset_board():
	global board
	global available
	global starter

	# Reset global variables for a new game.
	board = [" " for i in range(9)]
	available = [i for i in range(9)]
	starter = random.choice(["player", "computer"])

	# Display an empty board when starting a new game.
	print_board()


# Where to move if winning or losing is only one move away.
def power_move(icon):
	# Horizontal plane.
	if board[0] == icon and board[1] == icon and board[2] == " ":
		move = 2
	elif board[1] == icon and board[2] == icon and board[0] == " ":
		move = 0
	elif board[3] == icon and board[4] == icon and board[5] == " ":
		move = 5
	elif board[4] == icon and board[5] == icon and board[3] == " ":
		move = 3
	elif board[6] == icon and board[7] == icon and board[8] == " ":
		move = 8
	elif board[7] == icon and board[8] == icon and board[6] == " ":
		move = 6
	elif board[0] == icon and board[2] == icon and board[1] == " ":
		move = 1
	elif board[3] == icon and board[5] == icon and board[4] == " ":
		move = 4
	elif board[6] == icon and board[8] == icon and board[7] == " ":
		move = 7
	# Vertical plane.
	elif board[0] == icon and board[3] == icon and board[6] == " ":
		move = 6
	elif board[3] == icon and board[6] == icon and board[0] == " ":
		move = 0
	elif board[1] == icon and board[4] == icon and board[7] == " ":
		move = 7
	elif board[4] == icon and board[7] == icon and board[1] == " ":
		move = 1
	elif board[2] == icon and board[5] == icon and board[8] == " ":
		move = 8
	elif board[5] == icon and board[8] == icon and board[2] == " ":
		move = 2
	elif board[0] == icon and board[6] == icon and board[3] == " ":
		move = 3
	elif board[1] == icon and board[7] == icon and board[4] == " ":
		move = 4
	elif board[2] == icon and board[8] == icon and board[5] == " ":
		move = 5
	# Diagonal plane.
	elif board[0] == icon and board[4] == icon and board[8] == " ":
		move = 8
	elif board[4] == icon and board[8] == icon and board[0] == " ":
		move = 0
	elif board[2] == icon and board[4] == icon and board[6] == " ":
		move = 6
	elif board[4] == icon and board[6] == icon and board[2] == " ":
		move = 2
	elif board[0] == icon and board[8] == icon and board[4] == " ":
		move = 4
	elif board[2] == icon and board[6] == icon and board[4] == " ":
		move = 4
	else:
		move = None

	return move


# Start game. Runs only once.
game_title = "Welcome to Tic-Tac-Toe"
print()
print("*" * len(game_title))
print(game_title)
print("Version: 24.08.01.".center(len(game_title)))
print("*" * len(game_title))
print()

# Ask for player's name.
name = input("Enter your name: ").strip()

print("\nYou can move by entering any of the following numbers:")
time.sleep(2)

# Display move instructions.
print_help_board()


# Main game loop.
while True:
	# Player move.
	if starter == "player" or starter == None:
		player_move()
		print_board()

		if is_victory("X"):
			print("{} WINS! Congratulations!".format(name))
			new_game = input("Start a new game? [Y/n]: ").strip().lower()
			if new_game == "y" or new_game == "":
				reset_board()
				continue
			else:
				break
		elif is_draw():
			print("IT'S A DRAW!")
			new_game = input("Start a new game? [Y/n]: ").strip().lower()
			if new_game == "y" or new_game == "":
				reset_board()
				continue
			else:
				break

	# Computer move.
	computer_move()
	print_board()

	if is_victory("O"):
		print("COMPUTER WINS! Better luck next time...")
		new_game = input("Start a new game? [Y/n]: ").strip().lower()
		if new_game == "y" or new_game == "":
			reset_board()
			continue
		else:
			break
	elif is_draw():
		print("IT'S A DRAW!")
		new_game = input("Start a new game? [Y/n]: ").strip().lower()
		if new_game == "y" or new_game == "":
			reset_board()
			continue
		else:
			break


	# Reset starter for next round.
	starter = None

# Add an empty line when user quits the game.
print()
