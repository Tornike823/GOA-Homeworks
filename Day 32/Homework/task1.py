"""განსაზღვრეთ ფუნქცია სახელწოდებით simple_calculator, რომელიც იღებს სამ არგუმენტს:

num1: პირველი რიცხვი (მთლიანი ან float).
num2: მეორე რიცხვი (მთლიანი ან float).

ოპერაცია: სტრიქონი, რომელიც განსაზღვრავს შესასრულებლად ოპერაციას. ის შეიძლება იყოს „დამატება“, „გამოკლება“, „გამრავლება“ ან „გაყოფა“.
ფუნქციის შიგნით,

გამოიყენეთ if და elif განცხადებები, რათა დაადგინოთ რომელი ოპერაცია უნდა შეასრულოთ ოპერაციის არგუმენტის მნიშვნელობიდან გამომდინარე.

ფუნქციამ უნდა დააბრუნოს ოპერაციის შედეგი.

თუ ოპერაცია არის „გაყოფა“ და num2 არის 0, ფუნქციამ უნდა დააბრუნოს „შეცდომა: ნულზე გაყოფა შეუძლებელია“.
ჩაწერეთ კოდი, რომ გამოიძახოთ ფუნქცია სხვადასხვა ოპერაციებით და დაბეჭდოთ შედეგები. 
"""

def simple_calculator(num1, num2, operation):
    if operation == "add":
        return num1+num2
    elif operation == "subtract":
        return num1-num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "error: division by zero is impossible"
        else:
            return num1 / num2
    else: 
        return "error: invalid operation"
simple_calculator(int(input("enter your number: ")), int(input("enter your number: ")), input("enter oparation: "))
