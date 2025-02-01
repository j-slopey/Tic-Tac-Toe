# Author: James Slopey (2021)

from tkinter import *
import random
import time

class ConnectFour():
    
    def __init__(self):
        # Set up the root window, frame, and canvas
        self.tk = Tk()
        self.tk.title("Connect Four")
        self.tk.resizable(0, 0)
        # Create the frame and initialize the grid layout manager
        frame = Frame(self.tk)
        frame.grid()
        # Create a canvas to indicate which player
        self.canvasPlayer = Canvas(frame, width=675, height=40)
        self.canvasPlayer.grid(row = 1, column = 1)
        # Create a canvas for the connect four grid board
        self.canvas = Canvas(frame, width=1230/2, height=910/2)
        self.canvas.grid(row=2, column=1)
        
        
# ->    # Draw the grid on the canvas
        #GRID
        self.canvas.create_rectangle(10/2,10/2,910/2,910/2, outline = 'blue', width = 6)
        self.canvas.create_rectangle(310/2,10/2,610/2,910/2, outline = 'blue', width = 6)
        self.canvas.create_rectangle(10/2,310/2,910/2,610/2, outline = 'blue', width = 6)
        
        #O's

        self.circle0 = self.canvas.create_oval(920/2,310/2,1210/2,610/2, width = 4, outline = 'red')
        self.circle1 = self.canvas.create_oval(920/2,310/2,1210/2,610/2, width = 4, outline = 'red')
        self.circle2 = self.canvas.create_oval(920/2,310/2,1210/2,610/2, width = 4, outline = 'red')
        self.circle3 = self.canvas.create_oval(920/2,310/2,1210/2,610/2, width = 4, outline = 'red')
        self.circle4 = self.canvas.create_oval(920/2,310/2,1210/2,610/2, width = 4, outline = 'red')
        
        #X's
        self.x01 = self.canvas.create_line(920/2,310/2,1220/2,610/2, width = 4, fill = 'green')
        self.x02 = self.canvas.create_line(920/2,610/2,1220/2,310/2, width = 4, fill = 'green')

        self.x11 = self.canvas.create_line(920/2,310/2,1220/2,610/2, width = 4, fill = 'green')
        self.x12 = self.canvas.create_line(920/2,610/2,1220/2,310/2, width = 4, fill = 'green')

        self.x21 = self.canvas.create_line(920/2,310/2,1220/2,610/2, width = 4, fill = 'green')
        self.x22 = self.canvas.create_line(920/2,610/2,1220/2,310/2, width = 4, fill = 'green')

        self.x31 = self.canvas.create_line(920/2,310/2,1220/2,610/2, width = 4, fill = 'green')
        self.x32 = self.canvas.create_line(920/2,610/2,1220/2,310/2, width = 4, fill = 'green')

        self.x41 = self.canvas.create_line(920/2,310/2,1220/2,610/2, width = 4, fill = 'green')
        self.x42 = self.canvas.create_line(920/2,610/2,1220/2,310/2, width = 4, fill = 'green')

        
        

        self.olist = [self.circle0,self.circle1,self.circle2,self.circle3,self.circle4]
        self.xlist = [self.x01,self.x02,self.x11,self.x12,self.x21,self.x22,self.x31,self.x32,self.x41,self.x42]
        self.playO = 0
        self.playX = 0
        
        #   (the supplied discs are 90 pixels in diameter)        
        # Bind the mouse button to play
        self.canvas.bind_all("<Button-1>", self.choose)
        # Create the images of the playing pieces
        self.yspeed = 0
        self.xspeed = 0
        # Set up the stop button
        self.stopb = Button(frame, text="Close", command=self.endProgram)
        self.stopb.grid(row=3, column=1)
        self.stop = False
        # Initialize class variables
        self.play = [[0,0,0],
                     [0,0,0],
                     [0,0,0]]
        self.player = 1
        self.gameOver = False
        self.turn = ["It's Player 1's Turn", "It's Player 2's Turn"]
        self.pturn = self.canvasPlayer.create_text(338, 25, text=self.turn[0], font=("Arial", "20"))
        self.winner = 0

        self.xcount = 0
        self.xmoving = False

        self.ocount = 0
        self.omoving = False

        

    
    def endProgram(self):
        # Method called with stop buttion pressed
        self.stop = True

    def choose(self, evt):
        column = 0
        row = 0

# ->    # Check that the game is not over
        if self.gameOver:
            return
        
        
        # Determine which column and row was clicked on by the player
        if evt.x > 10/2 and evt.x < 900/2:
            if evt.x < 300/2:
                column = 0
            elif evt.x > 600/2:
                column = 2
            else:
                column = 1
        if evt.y > 10 and evt.y < 900/2:
            if evt.y < 300/2:
                row = 0
            elif evt.y > 600/2:
                row = 2
            else:
                row = 1
        
        

        # Place the player appropriate disc in the lowest empty slot
        self.setSpeeds(row,column)
        # Update the play board matrix with the current player
        # Determine if the player won and take appropriate action
        # Switch players
        # Change the message to indicate the current player
        



        #    row and column and put them on the canvas
        
            

    def setSpeeds(self,row,column):
        if self.gameOver:
            return
        if self.omoving or self.xmoving:
            return
        #XSPEED
        if column == 0:
            self.xspeed = -910/20
        if column == 1:
            self.xspeed = -610/20
        if column == 2:
            self.xspeed = -310/20
        #YSPEED
        if row == 0:
            self.yspeed = -300/20
        if row == 1:
            self.yspeed = 0
        if row == 2:
            self.yspeed = 300/20


        if self.play[row][column] == 0:
            self.play[row][column] = self.player
            if self.player == 1:
                self.xmoving = True
            elif self.player == 2:
                self.omoving = True
                
            
        #MOVE
    def move(self):
        
        #XPLACE
        if self.player == 1 and self.xmoving:
            self.xcount += 1
            if self.xcount == 11:
                self.xmoving = False
                self.player = 2
                self.playX+=2
                self.CPU()
                self.xcount  = 0
               
                
            else:
                self.canvas.move(self.xlist[self.playX],self.xspeed,self.yspeed)
                self.canvas.move(self.xlist[self.playX+1],self.xspeed,self.yspeed)
            
            
        #OPLACE    
        if self.player == 2 and self.omoving:
            self.ocount+=1
            if self.ocount == 11:
                self.omoving = False                
                self.playO+=1
                self.player = 1
                self.ocount = 0
            else:
                self.canvas.move(self.olist[self.playO],self.xspeed,self.yspeed)
        if self.gameOver:
            return   
        self.isWinner()

            
        

    def CPU(self):
        if self.gameOver:
            return
        if self.play[1][1] == 0:
            row = 1
            column = 1
            self.setSpeeds(row,column)
            return
        
      
        for x in range(3):
            if sum(self.play[x]) == 0:
                row = x
                column = 0
                self.setSpeeds(row,column)
                return
        for x  in range(3):
            for y in range(3):
                if self.play[x][y] == 0:
                    row = x
                    column = y
                    self.setSpeeds(row,column)
                    return
        
        
            
        
        
    def isWinner(self):
        # This is a helper method called from self.choose
        if self.winHorizontal() > 0:
            self.win()
            self.winner = True
        if self.winVertical() > 0:
            self.win()
            self.winner = True
        if self.winDiagonal() > 0:
            self.win()
            self.winner = True
        

    def winHorizontal(self):
        w = 0
        for x in self.play:
            if x[0] == x[1] and x[0] == x[2]:
                w = x[0]
                self.winner = w
        return w
        # This is a helper method called from self.isWinner
# ->    # Determine if the player wins with four in a row horizontally



        
    def winVertical(self):
        w = 0
        for x in range(3):
            if self.play[0][x] == self.play[1][x] and self.play[0][x] == self.play[2][x]:
                w = self.play[0][x]
                self.winner = w
        return w
            
                
        # This is a helper method called from self.isWinner
# ->    # Determine if the player wins with four in a row vertically



        
    def winDiagonal(self):
        w = 0
        if self.play[0][0] == self.play[1][1] and self.play[0][0] == self.play[2][2]:
            w = self.play[0][0]
        if self.play[2][0] == self.play[1][1] and self.play[2][0] == self.play[0][2]:
            w = self.play[2][0]
        self.winner = w
        
        
                    
        return w
        # This is a helper method called from self.isWinner
# ->    # Determine if the player wins with four in a row diagonally

    def win(self):
        self.gameOver = True
        if self.winner == 1:
            self.canvas.create_text(338, 290, text="X Wins!", font=("Arial", "60"))
            self.canvasPlayer.itemconfig(self.pturn,text="Game Over")

        if self.winner == 2:
            self.canvas.create_text(338, 290, text="CPU Wins!", font=("Arial", "60"))
            self.canvasPlayer.itemconfig(self.pturn,text="Game Over")


    def main(self):
        # Main loop that runs the game
        while True:
            time.sleep(.1)
            self.move()
            self.tk.update()
            self.tk.update_idletasks()
            if self.stop == True:
                self.tk.destroy()
                break

# Instantiate the class and run the main method
c4 = ConnectFour()
c4.main()
