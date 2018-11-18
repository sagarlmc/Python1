#Final Project
#Name: Sagar Lamichhane / Gaurav Thapa
#Course: 1411-003/501
#Date: 11/29/2017

#PROBLEM:
# Write a menu-based program for dietician to enter client first and last name, body type, weight, height,age, and level of activity.
# Dietician should be able to select a client to determine daily calorie, fat calories and fat grams needed.
# Choose a menu for breakfast, lunch, and dinner for total daily food and fat calories.
# recommend a reduced calorie intake if the client wishes to lose weight of 10% less calories than the daily calorie need
# the reduced fat calories and gram should be given as well 

#GIVEN:
# BMR for women and men calculation formula for female and male.
# Harris Benedict Formula to calculate the level of activity.
# Foods with total calories and fats in grams. 


#ANALYSIS:
#Input: client's first name and last name, body type(gender), weight, height, age and level of activity.
     
#Output: BMR, Daily calorie need, Daily fat needed
#Output: Calories and daily fats needed to loose weight. 


#METHOD/ALGORITHM:
# Introduce the program
# Ask for client's name, body type, weight, height, age and level of activity.
# If the name is not in the file, build the client's information in the file.
# If the client's information is in the file, access the information to give the BMR, daily calorie need, daily fats in gram.
# Ask clients to choose the food from the menu based on its caloire and fats.
# Ask clients to choose food for breakfast, lunch and dinner.
# Based on the food selected and daily calorie, fat intake, suggest the client about their calories and fats. 


#TEST CASES:


#PROGRAM
def build():
    a = input("Please enter your first name: ")
    b = input("Please enter your last name: ")
    c = input("Please enter your Body type: ")
    d = int(input("Please enter your weight in [0-400] lbs: "))
    e = int(input("Please enter your height in [0-120] inches: "))
    f = int(input("Please enter your age[0-120] years: "))
    g = int(input("Enter your activity level[1-5]: "))

    a_file = open("clients_info.txt","a+")
    a_data = a + "," + b + "," + c + "," + str(d) + "," + str(e) + "," + str(f) + "," + str(g) + "\n"
    a_file.writelines(a_data)
    a_file.close()
    return


def evaluate(a_file, calories, fats):
    flag0 = 0
    while flag0==0:
        client_name = input("Please enter the name of Client: ")
        for i in range(len(a_file)):
            if a_file[i][0] + " " + a_file[i][1] == client_name:
                clients_first_name = a_file[i][0]
                clients_last_name = a_file[i][1]
                body_types = a_file[i][2]
                weight = int(a_file[i][3])
                height = int(a_file[i][4])
                age = int(a_file[i][5])
                level_activity = int(a_file[i][6])

                if body_types == "Male":
                    BMR = 66 + (6.23 * weight) + ( 12.7 * height) - ( 6.8 * age)
                else:
                    BMR = 655 + ( 4.35 * weight) + ( 4.7 * height) - ( 4.7 * age)
                print(BMR)


                if level_activity == 1:
                    Calorie_Calculation = BMR * 1.2
                elif level_activity == 2:
                    Calorie_Calculation = BMR * 1.375
                elif level_activity == 3:
                    Calorie_Calculation = BMR * 1.555
                elif level_activity == 4:
                    Calorie_Calculation = BMR * 1.725
                else:
                    Calorie_Calculation = BMR * 1.9
                    
                print("Daily calorie need is ",Calorie_Calculation)

                #Fat_Calorie_need = [y for y in range (0.2 * Calorie_Calculation , 0.3 * Calorie_Calculation)]
                Fat_Calorie_need1 = 0.2 * Calorie_Calculation
                Fat_Calorie_need2 = 0.3 * Calorie_Calculation

                print("Daily fat calorie need is from 20% ", Fat_Calorie_need1, "to 30% ", Fat_Calorie_need2)

                Fat_grams1 = Fat_Calorie_need1 / 9
                Fat_grams2 = Fat_Calorie_need2 / 9
                print("In fat grams from" ,Fat_grams1, "to" ,Fat_grams2)

                Loose_weight = (Calorie_Calculation - 0.1 * Calorie_Calculation)
                Keep_Fat_Calories1 = Fat_Calorie_need1 - 0.1 * Fat_Calorie_need1
                Keep_Fat_Calories2 = Fat_Calorie_need2 - 0.1 * Fat_Calorie_need2
                Daily_Fat_Calorie1 = 0.2 * Loose_weight
                Daily_Fat_Calorie2 = 0.3 * Loose_weight
                Fat_grams3 = Daily_Fat_Calorie1 / 9
                Fat_grams4 = Daily_Fat_Calorie2 / 9

                
                flag0 = 1
        if flag0!=1:
            print("No such person exists. Please input name properly. ")
                
    calories = function_menu(calories, fats)

    if (calories)< Calorie_Calculation:
        print("You do not exceed total daily calorie intake.")
    else:
        print("I suggest you to eat more and follow these guidelines: ")
        print("To loose Weight, reduce calories to 10%",Loose_weight, "below daily" )
        print("Keep daily fat calories from",Daily_Fat_Calorie1, "to",Daily_Fat_Calorie2)
        print("In fat grams from",Fat_grams3,"to",Fat_grams4)


    

            
            

def function_menu(calories, fats):
    choice = True
    while choice:
        choose1 = input("Choose a MENU: \n [B] for Breakfast \n [L] for Lunch \n [D] for Dinner\n[T] to count your total calorie and fats\n- ")
        #if choose1 == "[B]" or choose1 == "[L]" or choose1 == "[D]":
        if choose1 == "B" or choose1 == "L" or choose1 == "D":
            print(25 * "*" ,"FOODS MENU", 25 * "*")
            print("\n")
            print("{:>29s} {:>14s} {:>16s}".format("FOOD ITEMS", "CALORIES", "FAT IN GRAMS"))
            print(62 * "-")
            print("{:>3s} {:>26s} {:>10s} {:>10s}".format("1","French Fries", "570", "30"))
            print("{:>3s} {:>26s} {:>10s} {:>10s}".format("2","Onion Rings", "350", "16"))
            print("{:>3s} {:>26s} {:>10s} {:>10s}".format("3","Hamburger", "670", "39"))
            print("{:>3s} {:>26s} {:>10s} {:>10s}".format("4","Cheeseburger", "760", "47"))
            print("{:>3s} {:>26s} {:>10s} {:>10s}".format("5","Grilled Chicken Sandwich", "420", "10"))
            print("{:>3s} {:>26s} {:>10s} {:>10s}".format("6","Egg Biscuit", "300", "12"))
            print("{:>3s} {:>26s} {:>10s} {:>10s}".format("7","Mozzarella Sticks", "849", "56"))
            print("{:>3s} {:>26s} {:>10s} {:>10s}".format("8","Cheese Pizza", "300", "11"))
            print("{:>3s} {:>26s} {:>10s} {:>10s}".format("9","Macaroni and Cheese", "300", "7"))
            print("{:>3s} {:>26s} {:>10s} {:>10s}".format("10","Glazed Chicken and Veggies", "497", "7"))
            print("\n\n")
            print(62 * "*")
            
            choices = True
            while choices:
                selection = input("Please select foods from the MENU [1-10]")
                selection = int(selection)
                if selection in range(1,11):
                    selection = str(selection)
                    if selection =="1":
                        calories += 570
                        fats += 30
                        print("Your order is French Fries, with",calories, "Calories and", fats, "fats in gram")
                        
                        
                    elif selection =="2":
                        calories += 350
                        fats += 16
                        print("Your order is Onion Rings, with",calories, "Calories and", fats, "in gram")
                        
                        
                    elif selection =="3":
                        calories += 670
                        fats += 39
                        print("Your order is Hamburger, with",calories, "Calories and", fats, "fats in gram")
                        
                        
                    elif selection =="4":
                        calories += 760
                        fats += 47
                        print("Your order is Cheeseburger, with",calories, "Calories and", fats, "fats in gram")
                    
                       
                    elif selection =="5":
                        calories += 420
                        fats += 10
                        print("Your order is Grilled Chicken Sandwich, with",calories, "Calories and", fats, "fats in gram")
                        

                    elif selection =="6":
                        calories += 300
                        fats += 12
                        print("Your order is Egg Biscuit, with",calories, "Calories and", fats, "fats in gram")
                        
                        
                    elif selection =="7": 
                        calories += 849
                        fats += 56
                        print("Your order is Mozzarella Stick, with",calories, "Calories and", fats, "fats in gram")
                        
                        
                    elif selection =="8":
                        calories += 300
                        fats += 11
                        print("Your order is Cheese Pizza, with",calories, "Calories and", fats, "fats in gram")
                        
                        
                    elif selection =="9":
                        calories += 500
                        fats += 7
                        print("Your order is Macaroni and Cheese, with",calories, "Calories and", fats, "fats in gram")
                        
                        
                    else:
                        calories += 497
                        fats += 7
                        print("Your order is Glazed Chicken and Veggies, with",calories, "Calories and", fats, "fats in gram")
                    
                    ch = input("Press [A] if you would like to add more items. \nPress any other key if you want to go back.")
                    if ch == "A" or ch == "a":
                        continue
                    else:
                        break     
                           
                else:
                    print("Please review the MENU choices carefully")
                
                
          
        elif choose1 == "T":
            total_cal = calories
            total_fat = fats
            print("Your Total Calorie is {} , and Fat in gram is {}".format(total_cal,total_fat))
            break
                                  
        else:
            print("Please review the MENU choices carefully")

    return calories

    


    
def function1():
    while True:
        b_file= open("clients_info.txt","r")
        b_file.seek(0)
        a_list = [lines.strip("\n").split(",") for lines in b_file]

        #print(a_list)
        calorie = 0
        fat = 0
        print("Welcome to the diet program")
        print("Please make a selection from the choices given below")
        print("[1] to build a new records")
        print("[2] to access client's information and evaluate daily calorie and fats")
        print("Enter any key to exit the program")

        pick = input()
        if pick == "1":
            build()
              

        elif pick == "2":
            evaluate(a_list, calorie, fat)
            
            
            
        else:
            print("Thank You")
            print("Have a nice day")
            break
    return


function1()
