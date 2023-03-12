import random
print(random.randint(1, 9))
import time
print("Ask the Magic 8 ball a question")
time.sleep(5)
print("Searching for an answer.")
print("Please be patient")
for num in range(10):
	print(".")
	time.sleep(.5)	
time.sleep(1)
if(random.randint == 1):
	print("Yes!")
elif(random.randint == 2):
	print("No way!")
elif(random.randint == 3):
	print("Sorry, try again!")
elif(random.randint == 4):
	print("Maybe, it's hard to tell..")
elif(random.randint == 5):
	print("Better not count on it!")
elif(random.randint == 6):
	print("Of course!")
elif(random.randint == 7):
	print("You bet!")
elif(random.randint == 8):
	print("Signs point to a...yes!")
elif(random.randint == 9):
	print("Not today!")