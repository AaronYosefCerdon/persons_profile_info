#Use a while loop to repeatedly ask for inputs per person.
while True:
	 
	 #Define variables that will store the data collected for each person.
     full_name = input("Please input your full name: ")
     age = int(input("Please input your age: "))
     contact_number = int(input("Please input your contact number: "))
     address = input("Please input your address: ")
     email = input("Please input your email address: ")
     eye_color = input("Please input your eye color: ")
     favorite_color = input("Please input your favorite color: ")
     favorite_food = input("Please input your favorite food: ")
     dream_job = input("Please state your dream job: ")
     mbti_result = input("Please input your MBTI result: ")
     birthday = input("Please input your date of birth: ")
     zodiac_sign = input("Please input your zodiac sign: ")	 

     #Ask the user if they want to continue.
     another_profile = input("Do you want to enter another profile? (Yes/No): ")
    
     #Use an if statement to continue or end the loop.
     if another_profile == "No" or "no":
     	break
    

#Use read and write to put in all entries in a txt file.

