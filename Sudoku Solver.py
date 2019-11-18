class cell():
        def __init__(self):
                self.possibleNumbers = [1,2,3,4,5,6,7,8,9]
                self.Filled = False
                self.FilledValue = " "
        def updateNumbers(self,position):
                self.possibleNumbers[position - 1] = " "
        def updateFilledValue(self,Value):
                self.Filled = True
                self.FilledValue = Value
                self.PossibleNumbers = [" "," "," "," "," "," "," "," "," "]
        def outputValue(self):
                print(self.FilledValue)
# Cell Class structure #

def solved(table):
        filled = True
        for eachRow in table:
                for eachCell in eachRow:
                        if eachCell.Filled == False:
                                filled = False
        return filled
# Check to see if the table has been filled #



def searchSquares(XStart, XEnd, YStart, YEnd):
        filledNumbers = []
        for x in range(XStart, XEnd + 1):
                for y in range(YStart, YEnd + 1):
                        if grid[x][y].Filled == True:
                                filledNumbers.append(grid[x][y].FilledValue)
        for x in range(XStart, XEnd + 1):
                for y in range(YStart, YEnd + 1):
                        for eachNumber in filledNumbers:
                                grid[x][y].updateNumbers(eachNumber)
# Searching through each of the boxes and updating the cells accordingly #



def outputGrid(table):
        count = 0
        for eachrow in table:
                print("|" +str(eachrow[0].FilledValue) + "|" + str(eachrow[1].FilledValue)+ "|" +str(eachrow[2].FilledValue)+ "|/|" +str(eachrow[3].FilledValue)+ "|" +str(eachrow[4].FilledValue)+ "|" +str(eachrow[5].FilledValue)+ "|/|" +str(eachrow[6].FilledValue)+ "|" +str(eachrow[7].FilledValue)+ "|" +str(eachrow[8].FilledValue) + "|")
                count = count + 1
                print("-----------------------")
                if count % 3 == 0:
                        print("-----------------------")
# Outputting the grid #
                        
                        


grid = []
for x in range(9):
        row = []
        for y in range(9):
                newCell = cell()
                row.append(newCell)
        grid.append(row)
# Creation of 81 objects each with their own possible numbers that could be filled #





setupFile = open("SetupFile.txt","r")
for eachline in setupFile:
        grid[int(eachline[0])][int(eachline[2])].updateFilledValue(int(eachline[4]))
setupFile.close()
# Updating the objects according to the Sudoku problem defined in the file #





loopCounter = 0
while solved(grid) != True:
# Space for the actual logic of the algorithm to go #
        for eachrow in grid:
                numbersFilled = []
                for eachCell in eachrow:
                        if eachCell.Filled == True:
                                numbersFilled.append(eachCell.FilledValue)
                for eachCell in eachrow:
                        for eachNumber in numbersFilled:
                                eachCell.updateNumbers(eachNumber)
        # Updating each row's cells possible values #
        
        for eachColumn in range(len(grid)):
                numbersFilled = []
                for eachCell in range(len(grid)):
                        if grid[eachCell][eachColumn].Filled == True:
                                numbersFilled.append(grid[eachCell][eachColumn].FilledValue)
                for eachCell in range(len(grid)):
                        for eachNumber in numbersFilled:
                                grid[eachCell][eachColumn].updateNumbers(eachNumber)

        # Updating each column's cells possible values #
                        
        
        for x in range(3):
                for y in range(3):
                        searchSquares(3*x, (3*x)+2, 3*y, (3*y)+2)
        # Updating each box of cell's possible values #

        for eachrow in grid:
                for eachCell in eachrow:
                        if eachCell.Filled == False:
                                numberOfPossibilities = 0
                                for eachPossibility in eachCell.possibleNumbers:
                                        if eachPossibility != " ":
                                                numberOfPossibilities = numberOfPossibilities + 1
                                if numberOfPossibilities == 1:
                                        for eachPossibility in eachCell.possibleNumbers:
                                                if eachPossibility != " ":
                                                        eachCell.updateFilledValue(eachPossibility)
        # Updating the true value of each cell #
        loopCounter = loopCounter + 1
        print(loopCounter)

print(loopCounter)
outputGrid(grid)
        # Final output of the grid #


                
                
        
