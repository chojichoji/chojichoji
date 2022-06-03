"""
import random
number_of_doors=5
print("Welcome to the Angry Globin Hunt")
print("An award-winning game full of adventure and excitement!")
user_name= input("Type in your name: ")
print(user_name + ", do you think you can find the globin hiding in the kitchen cupboards?")
print("|_|" * number_of_doors)

while True:
    globin_location= random.randint(1, 5)
    pick_globin=int(input("Which cupboard do you think the globin is in: "))

    if pick_globin!=globin_location:
        print("Sorry! The globin is still lucking somewhere else.")
    else:
        print("Well done! You have found the globin. He was so scared he ran away")
        break
print("Thank you for playing. Now get back to work!")
"""