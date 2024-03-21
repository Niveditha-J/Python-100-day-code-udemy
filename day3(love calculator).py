print("The Love Calculator is calculating your score...")
name1 = input("Enter ur name") 
name2 = input("Enter ur loved one name")
combine_name=name1+name2
lower_name=combine_name.lower()
T=lower_name.count("t")
R=lower_name.count("r")
U=lower_name.count("u")
E=lower_name.count("e")
first_letter=T+R+U+E
L=lower_name.count("l")
O=lower_name.count("o")
V=lower_name.count("v")
E=lower_name.count("e")
second_letter=L+O+V+E
score=int(str(first_letter)+str(second_letter))
if(score<10 or score>90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif(score>=40 and score<=50):
  print(f"Your score is {score}, you are alright together.")
else:
   print(f"Your score is {score}.")