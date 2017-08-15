#  File: Queens.py
#  Description: This program prints all valid queen placements.
#  Student's Name: Justin Liu
#  Student's UT EID: jll4234
#  Course Name: CS 313E 
#  Unique Number: 51325
#
#  Date Created: November 4, 2016
#  Date Last Modified: November 9, 2016

class QueensProblem:
    def __init__(self, dimension):
        self.dim = dimension
        self.grid = []
        self.counter = 1
        for i in range(0,dimension):
            temp = []
            self.grid.append(temp)
            for j in range(0, dimension):
                temp.append("*")

    def __str__(self):
        string = ""
        for i in range(0, len(self.grid)):

            for j in range(0, len(self.grid[i])):
                string = string + self.grid[i][j] + " "

            string = string + "\n"

        return string

    def isValidPlace(self,row,col):
        for i in range(0,self.dim):
            # checks up and down
            if (self.grid[i][col] == "Q"):
                return False
            # checks left to right
            elif (self.grid[row][i] == "Q"):
                return False

        # checks LL UR diagonal
        testRow1 = row + 1
        testCol1 = col - 1
        testRow2 = row - 1
        testCol2 = col + 1
        
        while(self.onBoard(testRow1) and self.onBoard(testCol1) or self.onBoard(testRow2) and self.onBoard(testCol2)):
  
            if self.onBoard(testRow1) and self.onBoard(testCol1) and self.grid[testRow1][testCol1] == "Q":
                return False
            if self.onBoard(testRow2) and self.onBoard(testCol2) and self.grid[testRow2][testCol2] == "Q":
                return False

            testRow1 += 1
            testCol1 -= 1
            testRow2 -= 1
            testCol2 += 1

        # checks UL LR diagonal
        testRow1 = row + 1
        testCol1 = col + 1
        testRow2 = row - 1
        testCol2 = col - 1
        
        while(self.onBoard(testRow1) and self.onBoard(testCol1) or self.onBoard(testRow2) and self.onBoard(testCol2)):
  
            if self.onBoard(testRow1) and self.onBoard(testCol1) and self.grid[testRow1][testCol1] == "Q":
                return False
            if self.onBoard(testRow2) and self.onBoard(testCol2) and self.grid[testRow2][testCol2] == "Q":
                return False

            testRow1 += 1
            testCol1 += 1
            testRow2 -= 1
            testCol2 -= 1

        return True
                

    def onBoard(self, num):
        return (num >= 0 and num < self.dim)

    def solve(self, n):
        if n == 1:
            i = 0
            for i in range(0,self.dim):
                if self.isValidPlace(n-1,i):
                    self.grid[n-1][i] = "Q"
                    print("Iteration " + str(self.counter))
                    self.counter += 1
                    print(self)
                    self.grid[n-1][i] = "*"
                else:
                    #self.grid[n-1][i] = "N"
                    #print(self)
                    self.grid[n-1][i] = "*"
        else:
            i = 0
            for i in range(0,self.dim):
                if self.isValidPlace(n-1,i):
                    self.grid[n-1][i] = "Q"
                    #print(self)
                    self.solve(n-1)
                    self.grid[n-1][i] = "*"
                else:
                    #self.grid[n-1][i] = "N"
                    #print(self)
                    self.grid[n-1][i] = "*"
                    
        


def main():
    userInput = input("Enter the size of the square board: ")
    while int(userInput) < 4:
        print("Invalid input.")
        userInput = input("Enter the size of the square board: ")
    q = QueensProblem(int(userInput))
    q.solve(int(userInput))

main()
