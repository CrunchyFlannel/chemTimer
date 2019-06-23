import math
#this is for python only ^^

#inputs listed as follows: current hour, current minute, delta \/

#in python 'def' means "function" \/

def chemTimer(currentHour, currentMinute, delta):
	#the percent sign means mod() so in your case do mod(currentMinute + delta, 60) if this does not work try flipping the 60 and the currentMinute
	minuteHand = (currentMinute + delta) % 60


	#This tells the elapsed minutes
	elapsedMinute = (currentMinute + delta) / 60
	
	
	#this tells the hour hand not to move up until it has completed a full hour
	hourHand = math.floor(currentHour + elapsedMinute)


	#outputs, do not worry about this stuff matlab does it for you
	print("Hour = " + str(hourHand))
	print("Minute Hand = " + str(minuteHand))

#This calls the function, try any inputs you would like it works everytime. Also the problem states you may have problems in matlab if the delta input is negative. If you do have problems just remember you can multiply the inputs by -1 to flip the sign.\/\/
chemTimer(6, 45, 10)

#hopefully this code isnt to hard to translate back, I tried to explain it as best I could lol