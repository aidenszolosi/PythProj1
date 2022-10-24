#Programmer - Aiden Szolosi

#Date - 10/23/22 

#File Name - Szolosi-invoice.py

#Program Purpose - 
    #This program takes 3 given values and calculates a total in order to generate an invoice.

    #The program uses various methods to format the text, such as \t, \n, 
    #and concatenation of integers turned to string values with other string values
 
Books = 52.99 #given
LabFees = 25 #given
Tuition = 157.93*3 #given

LabFees = round(LabFees, 2) #just in case, not nessasary for this program
LabFees = float(LabFees) #conversion to float value in order to force the cents value to be present

PrintedTotal = Books + LabFees + Tuition
PrintedTotal = str(PrintedTotal)


#top part
print("*"*50)
print("\tColumbus State Community College")
print("\t550 East Spring Street")
print("\tColumbus, OH 43215")
print("-"*50)
#middle part
print("\tProduct Name:\tProduct Price")
print("\tBooks:\t\t$" + str(Books))
print("\tLab Fees:\t$" + str(LabFees))
print("\tTuition:\t$" + str(Tuition))
print("-"*50)


#total part
print("\t\t\tTotal" + "\n\t\t\t$" + PrintedTotal)
print("-"*50)
print("\n" + "  Thank you for being a Columbus State Student")
print("*"*50)

