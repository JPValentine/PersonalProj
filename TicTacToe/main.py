from ttt import *
from tkinter import *

pSign=" "# the X or O depending on players choice
otherSign=" "#player twos sign
global board
turnTrack=1
root = Tk()
root.geometry("200x120")
root.title("Tic-Tac-Toe")
frame = Frame(root)
frame.pack()

b1=Button(frame, text="Two Player",command=lambda:drawBoard(board,1)).pack()
b2=Button(frame, text="Easy mode",command=lambda:drawBoard(board,2)).pack()
b3=Button(frame, text="Impossible",command=lambda:drawBoard(board,3)).pack()

def exit():
    """ends the progam"""
    global root
    root.destroy()

b4=Button(frame, text="Exit",command=exit).pack()

def drawBoard(board, gameType):
    """
    opens a window to play a game of tic-tac-toe!
    :param board: takes in the current board
    :param gameType: 1 if two player game 2 if ez game and 3 if minimax game
    """

    global root
    root.withdraw()
    playerPick = Toplevel(root)
    top = Toplevel(root)
    top.geometry("275x245")
    top.title("Playing Tic-Tac-Toe!")
    top.resizable(False,False)
    playerPick.title("picking =)")
    playerPick.geometry("200x120")
    label = Label(playerPick,text="Player 1 pick X or O!").grid(row=1,column=0)
    pSign=" "
    def pick(p):
        """
        function to determine if the player wants x or o
        it also closes playerpick toplevel window after the click
        :param p: 1 is for x anything else is o
        """
        global pSign,otherSign
        if p==1:
            pSign = "X"
            otherSign="O"
        else:
            pSign = "O"
            otherSign="X"

        playerPick.destroy()

    xButton = Button(playerPick,text="X",command=lambda:pick(1)).grid(row=2,column=0)
    oButton = Button(playerPick,text="O",command=lambda:pick(2)).grid(row=2,column=1)


    def wipe(board):
        """
        """
        global pSign,otherSign
        board[0][0]=0
        board[0][1]=0
        board[0][2]=0
        board[1][0]=0
        board[1][1]=0
        board[1][2]=0
        board[2][0]=0
        board[2][1]=0
        board[2][2]=0
        b1.config(text=" ")
        b2.config(text=" ")
        b3.config(text=" ")
        b4.config(text=" ")
        b5.config(text=" ")
        b6.config(text=" ")
        b7.config(text=" ")
        b8.config(text=" ")
        b9.config(text=" ")
        #pSign=" "
        #otherSign=" "


    def end(board,p,tie):
        """
        pops up message showing player(s) who won. It disables the board screen
        give option to play Again or not.
        :param board:current board
        :param p: the sign that the winning player was given.
        :param tie: boolean showing if the tie is true or not
        """
        stopBtn()#disables all the buttons
        endTop=Toplevel(root)
        endTop.title("Game Over.")
        if tie==True:
            lEnd=Label(endTop,text="Tie Game")
            lEnd.grid(row=1,column=2)
        else:
            lEnd=Label(endTop,text='Player')
            lEnd.grid(row=1,column=1)
            lEnd2=Label(endTop,text=p)
            lEnd2.grid(row=1,column=2)
            lEnd3=Label(endTop,text='Wins!')
            lEnd3.grid(row=1,column=3)
        lEnd3=Label(endTop,text='Play Again?')
        lEnd3.grid(row=2,column=2)

        def yPush():
            wipe(board)
            endTop.destroy()
            normBtn()
        yBtn=Button(endTop,text="Yes",command=lambda:yPush())
        yBtn.grid(row=3,column=1)
        def nPush():
            wipe(board)
            endTop.destroy()
            top.destroy()#gets rid of the game screen
            root.deiconify()#pulls the main root page back into view
        nBtn=Button(endTop,text="No",command=lambda:nPush())
        nBtn.grid(row=3,column=3)
        endTop.mainloop()

    def click(buttons,i,j,type,board):
        """
        when a user clicks a button it checks for valid move
        changes text and the board
        :param buttons: the button that was just pressed will call this function
        :param i: the row in which the board is evaluated
        :param j: the column in which the board is evaluated
        :param type: the type of game that is being played.1 is two players
        2 is ez, and 3 is Impossible
        """
        global pSign,turnTrack
        print([board[0][0],board[0][1],board[0][2]])
        print([board[1][0],board[1][1],board[1][2]])
        print([board[2][0],board[2][1],board[2][2]])
        print("-------------------------")
        if type==1:
            if (turnTrack%2)==0:
                if board[i][j]==0:
                    buttons.config(text=otherSign)
                    board[i][j]=1
                    if winCheck(board,1):
                        end(board,otherSign,False)
                    if tieCheck(board):
                        end(board,pSign,True)
                    p2Click(type)
                    turnTrack=turnTrack+1
                    return True
                else:
                    return False
            else:
                if board[i][j]==0:
                    buttons.config(text=pSign)
                    board[i][j]=-1
                    if winCheck(board,-1):
                        end(board,pSign,False)
                    if tieCheck(board):
                        end(board,pSign,True)
                    p2Click(type)
                    turnTrack=turnTrack+1
                    return True
                else:
                    return False

        else:
            if board[i][j]==0:
                buttons.config(text=pSign)
                board[i][j]=-1
                if winCheck(board,-1):
                    end(board,pSign,False)
                if tieCheck(board):
                    end(board,pSign,True)
                p2Click(type)
                return True
            else:
                return False

    def p2Sign(board):
        """
        adds text change to button board where there is a +1
        :param board:take current board
        """
        slots = []
        for i, row in enumerate(board):
            for j, slot in enumerate(row):
                if  slot==+1:
                    if i==0 and j==0:
                        b1.config(text=otherSign)
                    elif i==0 and j==1:
                        b2.config(text=otherSign)
                    elif i==0 and j==2:
                        b3.config(text=otherSign)
                    elif i==1 and j==0:
                        b4.config(text=otherSign)
                    elif i==1 and j==1:
                        b5.config(text=otherSign)
                    elif i==1 and j==2:
                        b6.config(text=otherSign)
                    elif i==2 and j==0:
                        b7.config(text=otherSign)
                    elif i==2 and j==1:
                        b8.config(text=otherSign)
                    elif i==2 and j==2:
                        b9.config(text=otherSign)

    def p2Click(gameType):
        """
        this function does the player 2 move. Depending on the game type the
        second players move is found here.
        :param gameType:1 for 2 player game, 2 for ez bot, and 3 for Impossible
        :param buttons: button that will be changed by player 2
        """

        print([board[0][0],board[0][1],board[0][2]])
        print([board[1][0],board[1][1],board[1][2]])
        print([board[2][0],board[2][1],board[2][2]])
        print("-------------------------")
        if gameType==2:
            randomTurn(board)#pc changes board
            if winCheck(board,1):
                end(board,otherSign,False)
            if tieCheck(board):
                end(board,pSign,True)
            p2Sign(board)#takes those changes and fixes buttons
        elif gameType==3:
            pcTurn(board)#pc changes board
            if winCheck(board,1):
                end(board,otherSign,False)
            if tieCheck(board):
                end(board,pSign,True)
            p2Sign(board)#takes those changes and fixes buttons


    b1 = Button(top, text=" ",height=4,width=8,command=lambda:click(b1,0,0,gameType,board))
    b1.grid(row=1,column=0)
    b2 = Button(top, text=" ",height=4,width=8,command=lambda:click(b2,0,1,gameType,board))
    b2.grid(row=1,column=1)
    b3 = Button(top, text=" ",height=4,width=8,command=lambda:click(b3,0,2,gameType,board))
    b3.grid(row=1,column=2)
    b4 = Button(top, text=" ",height=4,width=8,command=lambda:click(b4,1,0,gameType,board))
    b4.grid(row=2,column=0)
    b5 = Button(top, text=" ",height=4,width=8,command=lambda:click(b5,1,1,gameType,board))
    b5.grid(row=2,column=1)
    b6 = Button(top, text=" ",height=4,width=8,command=lambda:click(b6,1,2,gameType,board))
    b6.grid(row=2,column=2)
    b7 = Button(top, text=" ",height=4,width=8,command=lambda:click(b7,2,0,gameType,board))
    b7.grid(row=3,column=0)
    b8 = Button(top, text=" ",height=4,width=8,command=lambda:click(b8,2,1,gameType,board))
    b8.grid(row=3,column=1)
    b9 = Button(top, text=" ",height=4,width=8,command=lambda:click(b9,2,2,gameType,board))
    b9.grid(row=3,column=2)

    def stopBtn():
        b1.configure(state=DISABLED)
        b2.configure(state=DISABLED)
        b3.configure(state=DISABLED)
        b4.configure(state=DISABLED)
        b5.configure(state=DISABLED)
        b6.configure(state=DISABLED)
        b7.configure(state=DISABLED)
        b8.configure(state=DISABLED)
        b9.configure(state=DISABLED)

    def normBtn():
        b1.configure(state=NORMAL)
        b2.configure(state=NORMAL)
        b3.configure(state=NORMAL)
        b4.configure(state=NORMAL)
        b5.configure(state=NORMAL)
        b6.configure(state=NORMAL)
        b7.configure(state=NORMAL)
        b8.configure(state=NORMAL)
        b9.configure(state=NORMAL)

    top.mainloop()
    playerPick.mainloop()


root.mainloop()
