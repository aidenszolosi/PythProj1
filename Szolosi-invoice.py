#Programmer - Aiden Szolosi
#Date - 10/23/22 
#File Name - Szolosi-invoice.py
#This program........

Books = 52.99
LabFees = 25
Tuition = 157.93*3

PrintedTotal = Books + LabFees + Tuition


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

PrintedTotal = str(PrintedTotal)
#total part
print("\t\t\tTotal")
print("\t\t\t$" + PrintedTotal)
print("-"*50)
print()
print("\tThank you for being a Columbus State Student")
print("*"*50)

