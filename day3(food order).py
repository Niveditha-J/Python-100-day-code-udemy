print("Thank you for choosing Python Pizza Deliveries!")
size = input("Select the size S,M,L?") # What size pizza do you want? S, M, or L
add_pepperoni = input("If u want to add pepperoni? Y or N:") # Do you want pepperoni? Y or N
extra_cheese = input("If u want to add cheese? Y or N:") # Do you want extra cheese? Y or N

bill=0

if size=="S":
  bill+=15
elif size=="M":
  bill+=20
else:
  bill+=25

if add_pepperoni=="Y":
  if(size=="S"):
    bill+=2
  else:
    bill+=3
if extra_cheese=="Y":
  bill+=1
print(f"Your final bill is: ${bill}")