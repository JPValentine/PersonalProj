import random

HUMAN=-1
PC = +1
board=[#main game board that will be manipulated and checked for the game
    [0,0,0],
    [0,0,0],
    [0,0,0],
]
def tieCheck(board):
    """
    The only place this chould be called is AFTER winCheck
    :param board:current board
    """
    depth= len(allEmptySlots(board))
    if depth ==0:
        return True
    else:
        return False

def winCheck(board,checkPlayer):
    """
    identifies a winner where possible
    :param board: takes the game board
    :param checkPlayer: takes in the player to be evaluated for a win
    -1 for player one and +2 for player 2
    """
    win=[
        [board[0][0],board[0][1],board[0][2]],#top row
        [board[1][0],board[1][1],board[1][2]],#mid row
        [board[2][0],board[2][1],board[2][2]],#bot row
        [board[0][0],board[1][0],board[2][0]],#lft col
        [board[0][1],board[1][1],board[2][1]],#mid col
        [board[0][2],board[1][2],board[2][2]],#rght col
        [board[0][0],board[1][1],board[2][2]],#diagonal
        [board[0][2],board[1][1],board[2][0]],#diagonal

    ]
    global pSign,otherSign
    if [checkPlayer,checkPlayer,checkPlayer] in win:
        return True
    else:
        return False

def score(board):
    """
    Need a way to score the game so minimax algorithm can tell what to pick
    :param board: takes in the current board
    :return int:+1 if the current player wins the game -1 for the other player
    wins. a draw is 0
    """
    if winCheck(board,HUMAN):
        return -1
    elif winCheck(board,PC):
        return +1
    else:
        return 0

def allEmptySlots(board):
    """
    making a list of all the open spaces on the board
    :param board: takes int he current board
    :return: list of empty slots
    """
    slots = []
    for i, row in enumerate(board):
        for j, slot in enumerate(row):
            if  slot==0:
                slots.append([i,j])

    return slots

def minimax(board, depth, player):
    """
    Recursive algorithm that lets player 2 make the best possible move.
    A tree is used to calculate these moves. The base case is when the target
    depth is reached in the tree.
    credit: https://github.com/Cledersonbc/tic-tac-toe-minimax as a guide on how to
    run the algorithm
    :param board: take the game board
    :param depth: the depth of the tree
    :param player: comp or the human player
    :return: gives back a list with the move found by minimax [row,col,score]
    """
    if player == PC:#pc is always the 'max' player
        x = [-1,-1, float('-inf')]
    else:
        x = [-1,-1, float('inf')]#human is always the 'min' player

    if depth == 0 or winCheck(board,-1) or winCheck(board,+1):
        s = score(board)
        return[-1,-1, s]

    for slot in allEmptySlots(board):
        i, j = slot[0], slot[1]
        board[i][j] = player#fills slot with -1 if human +1 if pc
        s = minimax(board,depth -1, -player)#looks at all possible slots
        board[i][j] = 0
        s[0], s[1] = i, j

        if player ==PC:
            if s[2]>x[2]:
                x=s
        else:
            if s[2] < x[2]:
                x=s
    return x

def pcTurn(board):
    """
    This is called to run the minimax algorithm
    :param board:current state of the board
    """

    depth= len(allEmptySlots(board))
    if depth == 0 or winCheck(board,+1) or winCheck(board,-1):
        return

    if depth==9:
        randomTurn(board)
    else:
        m=minimax(board,depth,PC)
        board[m[0]][m[1]]=+1

def randomTurn(board):
    """
    used for ez mode. This function randomly finds an open slot and makes a moves
    :param board:current state of the board
    """
    flag =True
    while flag:
        x=random.randint(0,8)
        if x==0 and board[0][0]==0:
            board[0][0]=+1
            flag=False
        elif x==1 and board[0][1]==0:
            board[0][1]=+1
            flag=False
        elif x==2 and board[0][2]==0:
            board[0][2]=+1
            flag=False
        elif x==3 and board[1][0]==0:
            board[1][0]=+1
            flag=False
        elif x==4 and board[1][1]==0:
            board[1][1]=+1
            flag=False
        elif x==5 and board[1][2]==0:
            board[1][2]=+1
            flag=False
        elif x==6 and board[2][0]==0:
            board[2][0]=+1
            flag=False
        elif x==7 and board[2][1]==0:
            board[2][1]=+1
            flag=False
        elif x==8 and board[2][2]==0:
            board[2][2]=+1
            flag=False


"""
#psuedo code for minimax from the book:
    Algorithms in a Nutshell (George Heineman: Hary Pollice: Stanlley Selkow, 2009)
minimax(state, depth, player)

	if (player = max) then
		best = [null, -infinity]
	else
		best = [null, +infinity]

	if (depth = 0 or gameover) then
		score = evaluate this state for player
		return [null, score]

	for each valid move m for player in state s do
		execute move m on s
		[move, score] = minimax(s, depth - 1, -player)
		undo move m on s

		if (player = max) then
			if score > best.score then best = [move, score]
		else
			if score < best.score then best = [move, score]

	return best
end
"""
