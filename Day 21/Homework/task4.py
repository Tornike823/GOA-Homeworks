"""დაწერეთ პროგრამა სადაც შეამოწმებთ, აქვს თუ არა ადამიანს მართვის მოწმობის აღების უფლება მისი ასაკისა და მართვის გამოცდილებიდან გამომდინარე. დარწმუნდით, რომ მომხმარებელი შეიყვანს თავისი ასაკს და წლების რაოდენობა, რომელსაც მანქანას მართავდა.მომხმარებელმა უნდა შეიყვანოს დადებითი მთელი რიცხვები ასაკისა და მართვის გამოცდილებისთვის. (დაგნა მოხდეს ოპერაციები)
გამოიყენეთ შემდეგი საკვალიფიკაციო კრიტერიუმები: პირი უნდა იყოს მინიმუმ 18 წლის მართვის მოწმობის მისაღებად. თუ პირი 18 წლამდეა, მას არ შეეძლება მართვის მოწმობის აღება. თუ პირი არის 18 წლის ან მეტი, მას უნდა ჰქონდეს მინიმუმ 1 წლიანი მართვის გამოცდილება, რომ დაშვებული იყოს მართვის მოწმობის აღებისთვის.
მომხმარებლისთვის აჩვენეთ შეტყობინება, რომელშიც მითითებულია მართვის მოწმობის მიღების უფლება."""


ask = int(input("შეიყვანეთ ასაკი: "))
ask1 = int(input("შეიყვანეთ თქვენი ავტომობილის მართვის გამოცდილება: "))


print(ask)
print(ask1)

  
if ask >= 17 and ask1 > 0:
    print("თქვენ გაქვთ უფლება ავტომობილის მართვის")


if ask <= 18 and ask1 < 1:
    print("თქვენ არ გაქვთ უფლება ავტომობილის მართვის")    
    
    

