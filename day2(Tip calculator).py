print("Welcome to the Tip Calculator")
bill=float(input("Enter Bill amount:Rs-"))
print(f"What is the bill amount{bill}")
tip=int(input("How much tip would u like give 10 or 12 or 15?"))# how many percent u want split
people=int(input("How many person u want to split?")) 
tip_bill=tip/100*bill+bill # so here tip+bill is =tip(percetange)/100*bill amount plus this value is added to original bill again.
final=tip_bill/people #final =total bill/no people need to pay
print(f"The final amount is {round(tip_bill,2)}")
print(f"The each person need to give {round(final,2)}")