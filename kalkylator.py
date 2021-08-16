#Uppgift: Projektuppgift alternativ 1. Enkel miniräknare.
class Kalkylator:
#Create a class that enables the four arithmetic methods

    def addera(self,x,y):                                           		#define addition method                          
        self.x=x
        self.y=y
        return x+y

    def subtrahera(self, x, y):                                     		#define subtraction method
        self.x=x
        self.y=y
        return x-y

    def mult(self, x, y):                                           		#define multiplication method
        self.x=x
        self.y=y
        return x*y
    
    def div(self,x,y):                                              		#define division method 
        self.x=x
        self.y=y
        return x/y
        

uträkning=Kalkylator()                                              		#Instantiate the object uträkning

#While loop to get user input
while True:
	str = input('Vad vill du räkna ut: ')                           	#Get input from user in the form 5 + 2
	list = str.split()                                              	#Split string and add to list            
	x = float(list[0])                                              	#Convert list element 0 to floating point variable, the first operand
	operator = list[1]                                              	#Assign variable element 1 from list, the arithmetic operator
	y = float(list[2])                                              	#Assign y element 2 from list, the second operand
	if operator in ('+', '-', '*', '/'):                            	#Check that only the four arithmetic method are used

		if operator == ('+'):                                       	#If operator is + then calculate sum of operands    
			print(f'{x} + {y} = {uträkning.addera(x,y):.2f}')       #Call addera method from object uträkning

		elif operator == ('-'):
			print(f'{x} - {y} = {uträkning.subtrahera(x,y):.2f}')   #Calculate subtraction

		elif operator == ('*'):                                     	#Calculate multiplication
			print(f'{x} * {y} = {uträkning.mult(x,y):.2f}')

		elif operator == ('/'):                                     	#Calculate division
		    if y==0:                                                	#Check if denominator is 0, in such case print error message    
		        print('Error! Division med 0!')
		    else:
		            
		      print(f'{x} / {y} = {uträkning.div(x,y):.2f}')        	#Calculate division

	else:                                                           	#If operator not one of four arithmetic methods print error message
		print('Felaktig operator!')
