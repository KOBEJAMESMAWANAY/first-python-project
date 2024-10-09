print("Welcome to the registration fee!")
age = int(input("Please enter your age: "))
member = (input("Are you a Member or Non-member? (Please type yes or no) ")).strip().lower()

if age< 18:
    if member == "yes":
        print("your fee is 450.00 pesos.")
    else:
        print("your fee is 650.00")
elif age >= 18 and age <= 65:
    if member == "yes":
        print("your fee is 550.00 pesos")
    else:
        print("your fee is 750.00 pesos")
elif age >= 65 and age <100:
    if member == "yes":
        print("your fee is 400.00 pesos")
    else:
        print("your fee is 600.00 pesos")
elif age> 100:
    print("Invalid age, please be realistic.")