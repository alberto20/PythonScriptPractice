#! /usr/bin/python
import sys
from p5Dict import declareVar, printVariables, declareLab, printLables
file = open(sys.argv[1] , "r")
count = 1

#read file loop
while True:
    inputLine = file.readline() # reads one text line from the file
    #if NULL break out of loop
    if inputLine == "":
        break

    #splits the inputline into a tokenlist
    tokenM = inputLine.split()

    # if the there is a token list of length greater then 0 continue
    if len(tokenM) != 0:
       #saves the first work to use for VAR string check
       isVar = tokenM[0]

        #gets the size of the token list
       tokenMLeng = len(tokenM)

       #if the line is a variable
       if isVar == "VAR":
            # if list is 4 length uses this function call
           if tokenMLeng == 4:
                declareVar(tokenM[2].upper(), tokenM[1].upper(), tokenM[3])
           # if list is 3 length uses this function call
           if tokenMLeng == 3:
                 declareVar(tokenM[1].upper(), tokenM[2].upper(), "")

       #save first work to check if is a label
       isLabel = tokenM[0]

        # if for if it is a label
       if isLabel[-1] == ":":
           declareLab(isLabel.upper(), count)
    
    count += 1
    inputLine = inputLine.rstrip('\n') #remove the newline
    print(inputLine)
	
file.close()
#print (count)
# vaiable pring section
print ("")
print ("Variables:")
print ("%-4s %-13s %-9s %s"%("", "Variable", "Type", "Value"))
printVariables()

#label printSection
print ("")
print ("Labels:")
print ("%-4s %-13s %s"%("", "Label", "Statement"))
printLables()