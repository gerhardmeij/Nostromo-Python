import time

#Basic Elements in a Program

###Literals - Numbers and string that appear directly in the program without allocating them to a variable. This data will not be stored in memory.

print("NOSTROMO Booting...") # String Linteral

time.sleep(3) # Sleep for 3 seconds - We will use sleep just for affect

print('''Welcom to the USCSS NOSTROMO
Curretn Mission: Save and rescue
''') # Multi Line Literal

time.sleep(0.8) 

print("Fuel Level: ",50.5) # 50.5 = Floating-point literal
time.sleep(0.8)
print("Water Level: ",90.6j) # 90.6j = Imaginary literal
time.sleep(0.8)
print("Number of crew: ",5)  # 5 = Integer literal
time.sleep(0.8)

###Variables - Variables are used for storing data in a program. A name is selected then an = sign followed by the value you want to store in the variable.

crewStringList = ['','',''] #String List
crewRank = ('','','') # Tuple variable - tuples are ordered, non changable set of values of any data type.
milesTraveledInt = 51214656865 # Int varaible
oxygenLevel = 80.5 #Float point variable
shipName = "USCSS NOSTROMO" # String variable - Strings can be incapsulated with either single quotes or double quotes.

#Now lets use the variables, notive the difference between the variable use and the literal use
print("Oxygen Level: ",oxygenLevel)
time.sleep(0.8)
print("Miles Traveled: ",milesTraveledInt)
time.sleep(0.8)

###Keywords - Python reserved for special use. lower case letters.

###Continuation lines - notes

###Printing
#Auto goes to new line after print
print("Distance to destination: ",35468465168)
time.sleep(0.8)

#Print two print() statements in same line
print("Time to destination is", end='')
print("7 months and 14 days")
time.sleep(0.8)

#Concat lines
print('System' + ' checks: ') # using "+""
time.sleep(0.8)

print('Fire suppression system: ' , 'Pass') #Using ","
time.sleep(0.8)

#Concat with variable
batteryLevel = 95
print('Battery System: ',batteryLevel , '%')
time.sleep(0.8)

#Substitute variable in line using format codes %d
heatSystem = 'Pass'
currentTemprature = '30'
print('Heat System: %s, current temp: %s degrees'%(heatSystem,currentTemprature))
time.sleep(0.8)

#Format codes - see notes

###Arithmetic Operations
#Multiplication
remainingTravelMonths = 7
remainingTravelDays = 14

totalTravelDaysLeft = remainingTravelMonths * 31 + remainingTravelDays
#Division
# / = To get real division result. Will convert to integer if both division values are integers.
# // = Throws away the remainder of the division.
remainingFoodSuppliesKg = 9000.00
print("Food suppllies: ")
print("Remaining Food Supplies: ",remainingFoodSuppliesKg)
remainingFoodPerDay = remainingFoodSuppliesKg / totalTravelDaysLeft
print("Remaining food per day: %.2f Kg" %remainingFoodPerDay) #.2f to the second decimal, change the number 2 to increase/ecrease precision.
remainingFoodPerCrewPerDay = remainingFoodPerDay // 5
print("Remaining food per crew member per day: ",remainingFoodPerCrewPerDay, " kg")


###Exponents
exponentialExample = 50**90
print("Exponential1: ", exponentialExample)
exponentialExample2 = pow(60,80)
print("Exponential2: ", exponentialExample2)

###Assignment statements



