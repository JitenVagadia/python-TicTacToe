from IPython.display import clear_output
#display Tictactoe board
def display_board(marker_list):
	clear_output()
	print('_________')
	print('         ')
	print(marker_list[7]+' | '+marker_list[8]+' | '+marker_list[9])
	print('_________')
	print('         ')
	print(marker_list[4]+' | '+marker_list[5]+' | '+marker_list[6])
	print('_________')
	print('         ')
	print(marker_list[1]+' | '+marker_list[2]+' | '+marker_list[3])
	print('_________')
	print('         ')

#choose marker for players
def choose_marker():
	player1_marker=0
	player2_marker=0
	while player1_marker!='X' and player1_marker!='O':
		x=(input('player1 choose marker "X" or "O":'));
		if x=='X':
			player1_marker='X'
			player2_marker='O'
		elif x=='O':
			player1_marker='O'
			player2_marker='X'
	return (player1_marker,player2_marker)

#actual instance of game
def game(marker1,marker2):
	marker_list=[' ' for x in range(10)]
	col={'X':[0,0,0],'O':[0,0,0]}
	row={'X':[0,0,0],'O':[0,0,0]}
	diag={'X':[0,0],'O':[0,0]}
	players=['X','O']
	turn=0
	while(turn!=9 and max(col['X'])!=3 and max(col['O'])!=3 and max(row['X'])!=3 and max(row['O'])!=3 and max(diag['X'])!=3 and max(diag['O'])!=3):
		display_board(marker_list)
		pos=0
		while(pos not in [x for x in range(1,10)]):
			pos=int(input('{} enter valid position(from 1 to 9):'.format(players[turn%2])))
			if(marker_list[pos]=='X' or marker_list[pos]=='O'):
				pos=0
		marker_list[pos]=players[turn%2]
		col[players[turn%2]][(pos-1)%3] +=1
		row[players[turn%2]][int((pos-1)/3)] +=1
		if pos in [7,5,3]:
			diag[players[turn%2]][0]+=1
		if pos in [1,5,9]:
			diag[players[turn%2]][1]+=1	
		turn=turn+1
	if (max(max(col['X']),max(row['X']),max(diag['X']))==3):
		if marker1=='X':
			return 'Player1 wins!'
		else:
			return 'Player2 wins!' 
	elif (max(max(col['O']),max(row['O']),max(diag['O']))==3):
		if marker1=='X':
			return 'Player2 wins!'
		else:
			return 'Player1 wins!'
	else:
		return 'Game if a tie!!!'

#main function to play games
def play_game():
	playing=1
	while(playing>0):
		player1_marker,player2_marker=choose_marker()
		print(game(player1_marker,player2_marker))
		playing=int(input('Enter 0 to exit,any other key to continue:'))
play_game()


