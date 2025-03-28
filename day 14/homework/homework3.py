#5)მომხმარებელს შემოატანინეთ 2 რიცხვი, და გამოიანგარიშეთ არის თუ არა რომელიმე 100-ის ტოლი ან 100-ზე მეტი.
#5)პროგრამამ უნდა გამოიანგარიშოს, მოცემული ორი რიცხვიდან რომელიმე 100-ის ტოლი ან მასზე მეტია თუ არა.
num0 = int(input("enter first number:  "))
num1 = int(input("enter second number:  "))
if num0 >= 100 or num1 >= 100:
    print("someone wants higher numbers")