def basic_salary(hourly_rate, hours_per_week):
    basic_weekly_salary = hourly_rate * min(hours_per_week, 40)
    monthly_salary = basic_weekly_salary * 4
    return monthly_salary


def overtime_salary(hourly_rate, hours_per_week):
    if hours_per_week > 40:
        overtime_hours = hours_per_week - 40
        overtime_weekly_pay = overtime_hours * (hourly_rate * 1.5)
        monthly_overtime_pay = overtime_weekly_pay * 4
        return monthly_overtime_pay
    else:
        return 0


def total_salary(hourly_rate, hours_per_week):
    basic = basic_salary(hourly_rate, hours_per_week)
    overtime = overtime_salary(hourly_rate, hours_per_week)
    return basic + overtime


rate = float(input("Enter hourly rate(Rs): "))
hours = float(input("Enter hours worked per week: ")) 

basic = basic_salary(rate, hours)
overtime = overtime_salary(rate, hours)
total = total_salary(rate, hours)

print("\n--- Salary Details ---")
print(f"Basic Salary per Month: Rs. {basic:,.2f}")
print(f"Overtime Salary per Month: Rs. {overtime:,.2f}")
print(f"Total Monthly Salary: Rs. {total:,.2f}")