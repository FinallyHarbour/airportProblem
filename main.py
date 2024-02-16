import math
import numpy as np
takenSeats = []
inputCode = str('')
rowUpper = 127
rowLower = 0
cUpper = 7
cLower = 0
rLowest = 127
rHighest = 0
################################################################
def filehandling(takenSeats):
    with open("C:\\Users\\Adisi\\Downloads\\airportProject\\airportProblem\\input.txt", "r") as file:
        takenSeats = file.readlines() #array of taken seats from textfile
    #print(len(takenSeats))
    seatfinding(inputCode, takenSeats, rowUpper, rowLower, cUpper, cLower, rLowest, rHighest)
    
################################################################
def seatfinding(inputCode, takenSeats, rowUpper, rowLower, cUpper, cLower, rLowest, rHighest):
    sarr = np.zeros((128,8), dtype=int)
    block = []
    flag = True
    flag2 = True
    cofrLowest = 7
    cofrHighest = 0
    lowestS = 0
    highestS = 0
    for j in range (0, len(takenSeats)):
        inputCode = takenSeats[j]
        #print(inputCode)
        rowUpper = 127
        rowLower = 0
        cUpper = 7
        cLower = 0
        #print(str(rLowest), str(rHighest))
        for i in range (0,7):
            if inputCode[i] == 'F':
                rowUpper = math.floor((rowUpper+rowLower)/2)
            elif inputCode[i] == 'B':
                rowLower = math.ceil((rowUpper+rowLower)/2) 
        for i in range (7,10):
            if inputCode[i] == 'L':
                cUpper = math.floor((cUpper+cLower)/2)
            elif inputCode[i] == 'R':
                cLower = math.ceil((cUpper+cLower)/2) 
        #print ("Row number is " + str(rowUpper) + " column number is " + str(cLower))
        sarr[rowUpper][cLower] = 1 #sets value in board to 1
        if rowUpper <= rLowest: #if the row number of the seat is smaller than the current lowest
             # set the lowest row number to the row number of this seat
            #save the lowest value 
            if rowUpper < rLowest:
                rLowest = rowUpper
                cofrLowest = cLower
            if rowUpper == rLowest:
                #print('current row' + str(rowUpper) + 'previous lowest row' + str(rLowest))
                rLowest = rowUpper
                if cLower < cofrLowest:
                    #print('New lowest column'+ str(cLower) + 'Is lower than the previous' + str(cofrLowest))
                    cofrLowest = cLower
            lowestS = rLowest*8+ 1 + cofrLowest
            #print(str(rowUpper) + ' Is smaller than the lowest')
        if rowUpper >= rHighest:
            if rowUpper > rHighest:
                rHighest = rowUpper
                cofrHighest = cUpper
            if rowUpper == rHighest:
                rHighest = rowUpper
                if cUpper > cofrHighest:
                    cofrHighest = cLower
            highestS = rHighest*8+ 1 + cofrHighest
            #print(str(rowLower) + ' Is bigger than the highest')
    print ("Due to seating arrangement, rows are between " + str(rLowest) + " and " + str(rHighest))
    for j in range (cofrLowest, 8):
        if sarr [rLowest][j] == 0:
            block.append(str(i*8+1+j))
    for j in range (cofrHighest,-1,-1):
        if sarr [rHighest][j] == 0:
            block.append(str(i*8+1+j))
    for i in range (rLowest+1,rHighest):
        for j in range (0, 8):
            if sarr[i][j] == 0:
                block.append(str(i*8+1+j))                
    cBlock = ", ".join(block)
    print('Many taken seats from ' + str(lowestS) + 'to' + str(highestS) + ' but there is/are free seats in the middle ' + cBlock)
    
###############################################################
def tool(inputCode, rowUpper, rowLower, cUpper, cLower, takenSeats, rLowest, rHighest):
    filehandling(takenSeats)#takenSeats returned
    #print(takenSeats)
tool(inputCode, rowUpper, rowLower, cUpper, cLower, takenSeats, rLowest, rHighest)