import datetime
file = open("test.txt","w")
currentDT = datetime.datetime.now()
file.write(str(currentDT)) 
file.close()

file = open("test.txt", "r") 
print file.readline() 