import random 

afile = open("data.txt","w")

for x in range(1000): 
  #first column: blood pressure (systolic)
  #second column: blood pressure (diatolic)
  #third column: heartbeat per min 
  #fourth column: oxygen level (in percentage)   
  line = str(random.randint(70,140)) + "	" + str(random.randint(40,90)) + "	"+ str(random.randint(60,100)) + "	" + str(random.randint(0,100))
  afile.write(line + "\n")

afile.close()  