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

def tax_amount(basic_salary):
    if basic_salary < 60000:
        tax = basic_salary * 0.10
    elif 60000 <= basic_salary <= 85000:
        tax = basic_salary * 0.15
    else:
        tax = basic_salary * 0.20
    return tax

def gross_salary(basic_salary):
    allowances = basic_salary * 0.20
    tax = tax_amount(basic_salary)
    gross = basic_salary + allowances - tax
    return gross

def salary_bracket(gross_salary):
    if gross_salary < 50000:
        return "Low income"
    elif 50000 <= gross_salary <= 80000:
        return "Middle income"
    else:
        return "High income"


rate = float(input("Enter hourly rate(Rs): "))
hours = float(input("Enter hours worked per week: ")) 

basic = basic_salary(rate, hours)
overtime = overtime_salary(rate, hours)
total = total_salary(rate, hours)
tax = tax_amount(basic)
gross = gross_salary(basic)
bracket = salary_bracket(gross)

print("\n--- Salary Details ---")
print(f"Basic Salary per Month: Rs. {basic:,.2f}")
print(f"Overtime Salary per Month: Rs. {overtime:,.2f}")
print(f"Total Monthly Salary: Rs. {total:,.2f}")
print(f"Tax Deducted (on Basic Salary): Rs. {tax:,.2f}")
print(f"Gross Salary (Basic + 20% Allowances - Tax): Rs. {gross:,.2f}")
print(f"Income Category: {bracket}")