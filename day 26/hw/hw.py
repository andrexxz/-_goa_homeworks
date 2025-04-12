

#1)მომხმარებელს შემოატანინეთ რიცხვი და გამოიტანეთ ყველა მის წინ მდგომი რიცხვები მაგ: input:"3" output:(2, 1).

num = int(input("შეიყვანეთ რიცხვი: "))

lst = []
for i in range(num-1,0,-1):
   lst.append(i)
print(lst) 


#2)1'დან 100'ის ჩათვლით გამოიტანეთ ყველა კენტი რიცხვი და დაამატეთ ლისტში, შემდეგ დაბეჭდეთ ეს ლისტი.
lst = []
for i in range(1,101,2):
    if i % 2 != 0:
        lst.append(i)
print(lst)


#3)მომხმარებელს შემოატანინეთ რიცხვი და დაადგინეთ ლუწია თუ კენტი ეს რიცხვი.

number = int(input("შეიყვანეთ რიცხვი: "))
if number % 2 == 0:
    print("ეს რიცხვი ლუწია")
else:
    print("ეს რიცხვი კენტია")

#4)მომხმარებელს შემოატანინეთ რიცხვი და უთხარით მისი grade ამ რიცხვის მიხედვით:
#(ანუ თუ მაგალითად 90'დან 100'ის ჩათვლით ექნება ქულა გამოუტანეთ "Grade A",
#თუ 80'დან 89'ის ჩათვლით გამოუტანეთ "Grade B" და ა.შ)
grade = int(input("შეიყვანეთ ქულა: "))

if grade >= 90 and grade <= 100:
    print("Grade A")
elif grade >= 80 and grade < 90:
    print("Grade B")
elif grade >= 70 and grade < 80:
    print("grade C")
elif grade >= 60 and grade < 70:
    print("grade D")

#5)დაპრინტეთ რიცხვები 16'იდან 57'მდე while loop'ის მეშვეობით
while True:
    for i in range(16, 58):
        print(i)
        if i == 57:
            break
    break


#6)დაპრინტეთ Hello world 5'ჯერ (while loop'ით)

while True:
    for i in range(5):
        print("hello world")
        if i == 4:
            break
    break
