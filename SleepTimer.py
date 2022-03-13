import os
import time
tester = 0


print("Enter time in minutes until sleep, defaults to 3 hours/180 minutes: ")

userInput = input()
if (userInput == ""):
    userInput = 180


sleepTimeHours  = round(int(userInput)) / 60 #convert hours to minutes
sleepTimeMinutes = int(userInput)  #stores the Minutes 20
sleepTimeSec = sleepTimeMinutes * 60 # convert minutes to seconds

timeWaiting = 0
Minutes = 60
Seconds = 0
Hours = round(sleepTimeHours)

if (sleepTimeMinutes < Minutes):
    Minutes = sleepTimeMinutes

print("\r" + str(round(Hours)) + ":" + str(round(Minutes)) + ":" + str(Seconds) + "\r")
if (Hours <= 1):
    Hours = 0
else:
    Hours = Hours - 1

while ( timeWaiting <= sleepTimeSec-1):
    timeWaiting = timeWaiting + 1
    
    time.sleep(1)

    os.system('cls||clear')


    if (Seconds <= 0):
        Seconds = 60
        Minutes = Minutes - 1

    

    if (Minutes <= 0 and Hours != 0):
        Minutes = 60
        Hours = Hours - 1


    
    
    Seconds = Seconds - 1

    if ((sleepTimeSec - timeWaiting) <= 60):
        Second = 0
        Minute = 0
        Hour = 0

    print( "\r" + (str(Hours)) + ":" + str(Minutes) + ":" + str(Seconds) + "\r")

    tester = tester + 1
    
print( tester )
print("goodnight <3")
os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
