game=[[0 ,   0 ,   0 ],
	[0 ,   0 ,   0 ],
	[0 ,   0 ,   0 ]]
def game_board():
	print("     0   1   2")
	for count, row in enumerate(game):
		print(count, row)

game_board()
player1= raw_input("enter player 1st symbol : ")
player2= raw_input("enter player 2nd symbol : ")
row=0 ; column=0
row1=0 ; column1=0
def input1(row,column):
	try:
		if(game[row][column]==player2 or game[row][column]==player1):
			print("invalid row and column number.")
			return False
		else:
			game[row][column]=player1 
			global turn		
			turn+=1
	except IndexError:
		print("invalid row or column number.")
		return False
def input2(row1,column1):
	try:
		if(game[row1][column1]==player1 or game[row1][column1]==player2):
			print("Invalid row and column number.")
			return False
		else:
			game[row1][column1]=player2
			global turn
			turn-=1
	except IndexError:
		print("invalid row or column number")
		return False
turn = 1; i= True
def horizontal():
	if(game[0][0]==game[0][1]==game[0][2]== player1 or game[1][0]==game[1][1]==game[1][2]==player1 or game[2][0]==game[2][1]==game[2][2]==player1):
		print("\n\nplayer 1 is winner")
		global turn;turn+=3
	elif(game[0][0]==game[0][1]==game[0][2]== player2 or game[1][0]==game[1][1]==game[1][2]==player2 or game[2][0]==game[2][1]==game[2][2]==player2):
		print("\n\nplayer 2 is winner")
		global turn;turn+=3
def vertical():
	if(game[0][0]==game[1][0]==game[2][0]== player1 or game[0][1]==game[1][1]==game[2][1]==player1 or game[0][2]==game[1][2]==game[2][2]==player1):
		print("\n\nplayer 1 is winner")
		global turn;turn+=3
	elif(game[0][0]==game[1][0]==game[2][0]== player2 or game[0][1]==game[1][1]==game[2][1]==player2 or game[0][2]==game[1][2]==game[2][2]==player2):
		print("\n\nplayer 2 is winner")
		global turn;turn+=3
def diagonal():
	if(game[0][0]==game[1][1]==game[2][2]== player1 or game[0][2]==game[1][1]==game[2][0]==player1):
		print("\n\nplayer 1 is winner")
		return 3
	elif(game[0][0]==game[1][1]==game[2][2]== player2 or game[0][2]==game[1][1]==game[2][0]==player2):
		print("\n\nplayer 2 is winner")
		return 3

while(i== True) :
	if turn == 1 :
		print("\nPLAYER1'S TURN:")
		row= input("Enter row no : ")
		column= input("Enter column no :")
		input1(row,column)
		game_board()
		run=horizontal()
		run=vertical()
		run=diagonal()
		if(run==3):
			print("\nU WANT TO PLAY ANOTHER GAME Y/N : ")
			i=False
	elif turn == 2:
		print("\nPLAYER2'S TURN")
		row1= input("player2 enter row no :")
		column1= input("enter column no :")
		input2(row1,column1)
		game_board()
		horizontal()
		vertical()
		run=diagonal()
		if (run== 3):
			i=False
