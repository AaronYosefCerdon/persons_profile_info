#Use try and except to display an error message.
try:
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

     #Use read and write to put in all entries in a txt file.
     with open("./profile_list.txt", "a") as profile_list:
     	profile_list.write("\nProfile Information\n")
     	profile_list.write(f"\nName: {full_name}\n")
     	profile_list.write(f"Age: {age}\n")
     	profile_list.write(f"Contact No: {contact_number}\n")
     	profile_list.write(f"Address: {address}\n")
     	profile_list.write(f"Email: {email}\n")	 
     	profile_list.write(f"Eye Color: {eye_color}\n")
     	profile_list.write(f"Favorite Color: {favorite_color}\n")
     	profile_list.write(f"Favorite Food: {favorite_food}\n")
     	profile_list.write(f"Dream Job: {dream_job}\n")
     	profile_list.write(f"MBTI Result: {mbti_result}\n")
     	profile_list.write(f"Birthday: {birthday}\n")
     	profile_list.write(f"Zodiac Sign: {zodiac_sign}\n")

     #Ask the user if they want to continue.
     another_profile = input("Do you want to enter another profile? (yes/no): ")

     #Use an if statement to continue or end the loop.
     if another_profile == "no":
     	break
#Use an except command to display an error message.
except ValueError:
	print("Your input is invalid. Please try again.")
         


