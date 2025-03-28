#1) დაწერეთ პროგრამა რომელიც თუ მოქალაქე არის 18 წლის და მას აქვს მართვის მოწმობა შეუშვებს ქვეყანაში
age = int(input("enter age:  "))
card = input("do you have car card?(yes/no):  ")
if age >= 18 and card == "yes":
    print("you can enter country")
else:
    print("you can't enter country")
