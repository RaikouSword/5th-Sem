rooms ={
    'standard':100,
    'deluxe':150,
    'suite':250
}
seasons = {
    'peak':0.2,
    'off':0.15
}

room = input("Enter the type of room (Standard,Deluxe,Suite): ")
room.lower()
nights = int(input("How many nights do you want to stay: "))
season = input("Which season is this(Peak or Off): ")
season.lower()
member = input("Are you a loyalty member(y/n): ")
member.lower()

rent = dis= 0
if room in rooms:
    rent+=rooms[room]
if season in seasons:
    rent+=(rent*seasons[season])
rent = rent*nights
if nights>3 and nights<=7:
    dis+=0.1
elif nights>7:
    dis+=0.2
if member=='y':
    dis+=0.05
print("Bill: ",rent - rent*dis)