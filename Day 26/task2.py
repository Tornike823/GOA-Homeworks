maxbid = int(input("enter max bid: "))

bid = int(input("enter bid: "))


while True:
      bid = int(input("enter bid: "))
      print(bid)
      if maxbid <= bid:
            break
print("sold out")