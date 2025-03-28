#2) მომხმარებელმა ფასდაკლება უნდა მიიღოს თუ 100 ლარზე მეტ რამეს ყიდულობს ან არის vip მომხმარებელი
cash = int(input("how much money you are spending?:  "))
vip = input("are you vip?(yes/no):  ")
if cash >= 100 or vip == "yes":
    print("you got discount")
else:
  print("you didnt get discount")