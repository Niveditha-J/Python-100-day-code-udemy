import random
names_string=["Niveditha","Sangeetha","Moshika","Monisha","Nikhitha","Sajietha"]
names_len=len(names_string)
random_choice=random.randint(0,names_len-1)
who_pay=names_string[random_choice]
print(who_pay+ ' is going to buy the meal today!')