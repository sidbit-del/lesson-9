print("welcome to ride builder")

print("menu:1-bike and 2-car")
choice=int(input("do you want a car or a bike"))

if choice==1:
    print("menu:1-scooty and 2-mountain bike")
    bike_type=int(input("do you want a scooty or mountain bike"))
    if bike_type==1:
        print("you picked scooty,top speed:80kmp/h best for city and flat areas")
    else:
        print("you picked mountain bike,top speed:40kmp/h best for bumpy mountanious terrain")
elif choice==2:
    print("menu:1-electric 2-SUV")
    car_type=int(input("do you want an electric car or an SUV"))
    if car_type==1:
        print("you chose electric best for city and places with chargers")
    else:
        print("you chose SUV best for remote and rough terrain")
else:
    print("invalid choice")

print("your custom ride is finished")

