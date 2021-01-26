print("Welcome to Tip Calcultor")
totalbill  = float(input("Whats the total bill $"))
tippercent = float(input("What percent tip you want to give 5,10,15 and 20 ?"))
splitbill  = float(input("How many people the bill need to be split across?"))
tippercent = (totalbill*tippercent)/100
grandtotalbill = totalbill + tippercent
personbill = grandtotalbill/splitbill
print("The total bill value including tip %f" %(grandtotalbill))
print("Each person should pay bill off {:.2f}".format(round(personbill,2)))