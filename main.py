print("Welcome to PyGame 1 !!!") # print statement prints what is inside the bracket to the screen

name = input("What is your name? ") #Assignment operator, here name variable is being assigned the value given by the user
try:
    age = int(input("What is your age? "))
except:
    print("Please enter the right age")     

health = 10
print("You are starting with ", health," health points")    

if age >= 18 and age <= 100:
    print("Welcome to Pygame 1 " + name + ". You are " + str(age) + " years old and old enough to play the game." )

    weapon = input("Pick a weapon (sword/baton)")

    if weapn == "sword"

    wants_toplay = input("Do you want to play? ").lower()
    if wants_toplay == 'yes': 
        print("Let's play! ")

        left_or_right = input("First choice... Left or Right (left/right)? ").lower() 

        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake... Do you swim across or go around(across/around)? ").lower()

            if ans == "around":
                print("You went around and reached the other side of the lake")

            elif ans == "across":
                health -= 5
                print("You managed to get across, but were bit by a fish and lost 5 health points.")

            ans = input("You notice a house and a river.Which would you go to  (river/house)? ")

            if ans == "house":
                print("You go to the house and are greeted by the owner...He doesn't like you and you lose 5 health")
                health -= 5

                if health <= 0:
                    print("You now have 0 health and you lost the game...")
            
                else:
                    print("You survived... You win!!!")

            else:
                print("you fell into the river and lost!!!")        

        else:
             print("You fell down and lost...")      

    else:
        print("See you then.")    

else:
    print("Welcome to Pygame 1 " + name + ". You are " + str(age) + " years old so you are not eligible to play the game." )

