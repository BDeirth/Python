#variables

div30 = 0
div5 = 0
div3 = 0
div2 = 0
div3_2 = 0
divNone = 0

#input larger than 0

while True:
	try:
		lower = int(input("Enter the lower number...not zero: "))
		if lower > 0:
			break
	except:
		print("Please enter a valid number: ")
		
#input larger than lower

while True:
	try:
		upper = int(input("Enter the upper number, larger than the lower number: "))
		if upper > lower:
			break
	except:
		print("Please enter a number larger than the lower number: ")

#create range based off the lower number and upper number inclusive

for number in range(lower, upper + 1):
#omit zero if chosen
	if number > 0:
    if(number%30==0):
        print("Foo")
		div30 += 1
    elif(number%3==0 and number%2==0):
        print("FizzBuzz")
		div3_2 += 1
    elif(number%5==0):
        print("Bar")
		div5 += 1
    elif(number%3==0):
        print("Fizz")
		div3 += 1
    elif(number%2==0):
        print("Buzz")
		div2 += 1
    else:
        print("Bazz")
		divNone += 1
    
#output

print("The total numbers evaluated was " + str(number) + ".")
print("There were", div30, "that were divisible by 30.")
print("There were", div5, "that were divisible by 5.")
print("There were", div3, "that were divisible by 3.")
print("There were", div2, "that were divisible by 2.")
print("There were", div3_2, "that were divisible by both 3 and 2.")
print("There were", divNone, "numbers that didn't meet any of the requirements above.")
