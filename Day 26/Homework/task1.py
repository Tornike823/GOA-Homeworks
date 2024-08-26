

weight = int(input("Enter your weight :"))
height = float(input("enter your height :"))

jami = weight / height
print(jami)

if jami < 18.5:
  print("under weight")
  if jami >= 18.5:
    print("normal")
  else: jami < 25
  print("normal")
  if jami >= 25:
    print("Overweight")
  else: jami < 30
  print("Overweight")
  if jami >= 30:
    print("Obesity")