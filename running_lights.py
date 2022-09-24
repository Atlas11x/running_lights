#import libraris
import os
import time

#init arr
array = [0, 0, 0, 0]

#init varriables
delay = int(1)




#setup
os.system("clear")
print("Thanks for doenload! --Atlas11x")
time.sleep(delay)
os.system("clear")
#loop
while True:
	for i in range(len(array) + 1):


		#reset list
		array[0] = 0
		array[1] = 0
		array[2] = 0
		array[3] = 0


		#light on
		array[i - 1] = 1

		#output
		print (str(array[0]) + " " + str(array[1]) + " " + str(array[2]) + " " + str(array[3]))

		#delay
		time.sleep(delay)

		#display reset
		os.system("clear")
