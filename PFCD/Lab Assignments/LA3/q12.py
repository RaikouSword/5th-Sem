def leap(year):
    return year%400==0 or (year%100!=0 and year%4==0)

weeks = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

date = input("Enter today's date in YYYY-MM-DD format: ")
week =input("Enter current day of the week: ")
days = int(input('Enter no of days: '))
date = date.replace("-","")
year,month,day = int(date[:4]),int(date[4:6]),int(date[6:8])
days_in_month = [31,29 if leap(year) else 28,31,30,31,30,31,31,30,31,30,31]

day+=days
while day>days_in_month[month-1]:
    day-=days_in_month[month-1]
    month+=1
    if month>12:
        month=1
        year+=1
        days_in_month[1] = 29 if leap(year) else 28

new_date = (weeks.index(week)+days)%7
new_day = weeks[new_date]

print(f"New date after {days} days: {year:04d}-{month:02d}-{day:02d}")
print(f"Day of the week: {new_day}")