import math
import numpy as np
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
        sarr[rowUpper][cLower] = 1
        if rowUpper < rLowest:
            rLowest = rowUpper
            #print(str(rowUpper) + ' Is smaller than the lowest')
        if rowUpper > rHighest:
            rHighest = rowUpper
            #print(str(rowLower) + ' Is bigger than the highest')
    print ("Due to seating arrangement, rows are between " + str(rLowest) + " and " + str(rHighest))
    for i in range (0,128):
        for j in range (0,8):
            if sarr[i][j] == 0:
                print('Space free at ' + str(i*8 + 1 +j))
###############################################################
def tool(inputCode, rowUpper, rowLower, cUpper, cLower, takenSeats, rLowest, rHighest):
    filehandling(takenSeats)#takenSeats returned
    #print(takenSeats)
tool(inputCode, rowUpper, rowLower, cUpper, cLower, takenSeats, rLowest, rHighest)
#find length of text file
#take input from the text file
#line by line scan and then
#find lowest seat
#find highest seat
#find search between them