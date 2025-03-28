#4) დაწერე პროგრამა, რომელიც შეამოწმებს, თუ იყოფა შემოტანილი რიცხვი ან 2-ზე, ან 3-ზე.
num = int(input("enter number:  "))
if num % 2 == 0 or num % 3 == 0:
    print("got it")