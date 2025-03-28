#3) ოთახის გათბობა აქტიურდება თუ ტემპერატურა ან ძალიან დაბალია ან ძალიან მაღალი
temperature = int(input("enter temperature:"))
if temperature <= 10 or temperature >= 40:
    print("cooling system activated")