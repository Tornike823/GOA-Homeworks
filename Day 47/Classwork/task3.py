def age_category():
   
    age = int(input("Enter your age: "))

   
    if age < 0:
        print("Invalid age. Age cannot be negative.")
    elif age <= 12:
        print("You are a child.")
    elif age <= 17:
        print("You are a teenager.")
    elif age <= 64:
        print("You are an adult.")
    else:
        print("You are a senior.")