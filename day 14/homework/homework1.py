#3) მომხმარებელმა უნდა შეიყვანოს თავისი ასაკი და სახელი. პროგრამამ უნდა შეამოწმოს, რომ ასაკი 18-ზე მეტია და სახელი იწყება "A"-ზე.
name = input("enter name:  ")
age = int(input("enter age:  "))
if age >= 18 and name[0].lower == "a":
    print("good boy:3")