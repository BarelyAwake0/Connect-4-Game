import time

board = [["-","-","-","-"],["-","-","-","-"],["-","-","-","-"],["-","-","-","-"]]
SELECT1 = ["↓"," "," "," "]
SELECT2 = [" ","↓"," "," "]
SELECT3 = [" "," ","↓"," "]
SELECT4 = [" "," "," ","↓"]

round = 1
status = False
player = 0


def gravity(board, play, player):
	board[0][play-1] = player
    
	for row in board:
		print(*row)
	print()

	time.sleep(1)
                
	if board[1][play-1] == "-":
		board[0][play-1] = "-"
		board[1][play-1] = player
        
		for row in board:
			print(*row)
		print()

		time.sleep(1)
                        
		if board[2][play-1] == "-":
			board[1][play-1] = "-"
			board[2][play-1] = player
            
			for row in board:
				print(*row)
			print()

			time.sleep(1)
                                
			if board[3][play-1] == "-":
				board[2][play-1] = "-"
				board[3][play-1] = player
                
				for row in board:
					print(*row)
				print()

				time.sleep(1)


def confirm(play, board):
	if play == 1:
		column = 1
		print()
		print(" ".join(SELECT1))
		for row in board:
			print(*row)
		print()
		return column
	if play == 2:
		column = 2
		print()
		print(" ".join(SELECT2))
		for row in board:
			print(*row)
		print()
		return column
	if play == 3:
		column = 3
		print()
		print(" ".join(SELECT3))
		for row in board:
			print(*row)
		print()
		return column
	if play == 4:
		column = 4
		print()
		print(" ".join(SELECT4))
		for row in board:
			print(*row)
		print()
		return column


def win_check(board):
	score = 0

	# diagonal check
	if board[0][0] == board[1][1] == board[2][2] == board[3][3] == "X":
		print(f"{player1} wins!!!")
		status = True
	elif board[0][0] == board[1][1] == board[2][2] == board[3][3] == "O":
		print(f"{player2} wins!!!")
		status = True
	elif board[0][3] == board[1][2] == board[2][1] == board[3][0] == "X":
		print(f"{player1} wins!!!")
		status = True
	elif board[0][3] == board[1][2] == board[2][1] == board[3][0] == "O":
		print(f"{player2} wins!!!")
		status = True
	else:
		status = False
	
	if status == True:
		return True

	# horizontal check
	if board[0][0] == board[0][1] == board[0][2] ==  board[0][3] == "X":
		print(f"{player1} wins!!!")
		status = True
	elif board[0][0] == board[0][1] == board[0][2] ==  board[0][3] == "O":
		print(f"{player2} wins!!!")
		status = True
	elif board[1][0] == board[1][1] == board[1][2] ==  board[1][3] == "X":
		print(f"{player1} wins!!!")
		status = True
	elif board[1][0] == board[1][1] == board[1][2] ==  board[1][3] == "O":
		print(f"{player2} wins!!!")
		status = True
	elif board[2][0] == board[2][1] == board[2][2] ==  board[2][3] == "X":
		print(f"{player1} wins!!!")
		status = True
	elif board[2][0] == board[2][1] == board[2][2] ==  board[2][3] == "O":
		print(f"{player2} wins!!!")
		status = True
	elif board[3][0] == board[3][1] == board[3][2] ==  board[3][3] == "X":
		print(f"{player1} wins!!!")
		status = True
	elif board[3][0] == board[3][1] == board[3][2] ==  board[3][3] == "O":
		print(f"{player2} wins!!!")
		status = True
	else:
		status = False
	
	if status == True:
		return True

	# vertical check
	if board[0][0] == board[1][0] == board[2][0] == board[3][0] == "X":
		print(f"{player1} wins!!!")
		status = True
	elif board[0][0] == board[1][0] == board[2][0] == board[3][0] == "O":
		print(f"{player2} wins!!!")
		status = True
	elif board[0][1] == board[1][1] == board[2][1] == board[3][1] == "X":
		print(f"{player1} wins!!!")
		status = True
	elif board[0][1] == board[1][1] == board[2][1] == board[3][1] == "O":
		print(f"{player2} wins!!!")
		status = True
	elif board[0][2] == board[1][2] == board[2][2] == board[3][2] == "X":
		print(f"{player1} wins!!!")
		status = True
	elif board[0][2] == board[1][2] == board[2][2] == board[3][2] == "O":
		print(f"{player2} wins!!!")
		status = True
	elif board[0][3] == board[1][3] == board[2][3] == board[3][3] == "X":
		print(f"{player1} wins!!!")
		status = True
	elif board[0][3] == board[1][3] == board[2][3] == board[3][3] == "O":
		print(f"{player2} wins!!!")
		status = True	
	else:
		status = False

	return status


print("---=== CONNECT 4 ===---")
player1 = input("Enter player 1's name...\n")
player2 = input("Enter player 2's name...\n")

while status == False:

	if round % 2 == 0:
		print(f"\n{player2}'s turn...")
		print(f"Round: {round}\n")
		player = "O"
		play = int(input("Which column would you like to play? (1-4) \n"))
		confirmation = False

		while confirmation == False:
			confirm(play, board)
			check = input(f"Are you sure you want to play column {play}? (Y/N) \n")
			if check.upper() == "Y":
				confirm(play, board)
				column = confirm(play, board)
				confirmation = True
			elif check.upper() == "N":
				play = int(input("Which column would you like to play? (1-4) \n"))
				confirmation = False
			else:
				print("Invalid input")

		gravity(board, column, player)

		status = win_check(board)

		round += 1

	elif round % 2 != 0:
		print(f"\n{player1}'s turn...")
		print(f"Round: {round}\n")
		player = "X"
		play = int(input("Which column would you like to play? (1-4) \n"))
		confirmation = False

		while confirmation == False:
			confirm(play, board)
			check = input(f"Are you sure you want to play column {play}? (Y/N) \n")
			if check.upper() == "Y":
				confirm(play, board)
				column = confirm(play, board)
				confirmation = True
			elif check.upper() == "N":
				play = int(input("Which column would you like to play? (1-4) \n"))
				confirmation = False

		gravity(board, column, player)

		status = win_check(board)

		round += 1
	else:
		print("Error")
		status = False
	

print("GAME OVER")
