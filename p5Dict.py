#associative arrays
varTypeD = {}
varValueD = {}
labelD = {}


def getVar(varName):
  for name in sorted(varTypeD):
    if name == varName.upper():
     return varValueD[name]

def setVar(varName, ValueD):
  varValueD[varName] = ValueD
  
  
 # print (varValueD[varName])

# declareVar
# 	Parameters:
#
#	varName - name of the variable that is used as the key
#	TypeD - type of variable
#	ValueD - Value of the variable
#	
#	Purpose:
#		Function that saves a value into the varTypeD associative array as the the varName
#		being the key and TypeD as the value. The function also saves the ValueD with
#		varName being the key into the VarValueD associative array
def declareVar(varName, TypeD, ValueD):

    #saves the type with the variable name being the key in type array
    varTypeD[varName] = TypeD
    #removes "" from the strings
    ValueD = ValueD.replace("\"", "")
    #saves the value with name being the key in Value array
    varValueD[varName] = ValueD

# printVariables
# 	Parameters:
#	
#	Purpose:
#		This function when called iterates through the varTypeD associative array
#		and prints a table of the array with its values while also getting the value
#		from the varValueD associative array
def printVariables():
     #iterates through the associative array and prints
    for name in sorted(varTypeD):
        print ("%-4s %-13s %-9s %s"%("", name, varTypeD[name], varValueD[name]))

# declareLab
# 	Parameters:
#	label - The name of the label that will be used as the key
#	subscript - the value that will be used as the value for the associative array
#	
#	Purpose:
#		Function when called upon passes a Label and subscript variable that is used
#		to input into the labelD associative array as the Label being the key and
#		subscript being the value. The function also removes : from the label name
#		and checks if the label as been inserted aswell. if insereted it will print
#		a error message but will not terminate	
def declareLab(Label, subscript):
    Label = Label.replace(":", "")
    
    #prints a error if the label already exists with its lines
    if Label in labelD:
        print ("***Error: label '" + Label + "' appears on multiple lines: " + labelD[Lable] + " and " + subscript)
    #saves the subscript with the label name as the key
    labelD[Label] = subscript

# printVariables
# 	Parameters:
#	
#	Purpose:
#		This function when called iterates through the labelD associative array
#		and prints a table of the array with its value
def printLables():
    #iterates through the associative array and prints
    for name in sorted(labelD):
        print ("%-4s %-13s %s"%("", name, labelD[name]))