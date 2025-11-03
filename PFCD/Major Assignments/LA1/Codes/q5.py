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


def employee_report(employees):
    print("\n" + "=" * 80)
    print(f"{'EMPLOYEE SALARY REPORT':^80}")
    print("=" * 80)
    print(f"{'Name':<20}{'Basic Salary (Rs)':<20}{'Gross Salary (Rs)':<20}{'Tax (Rs)':<10}{'Bracket':<15}")
    print("-" * 80)

    for emp in employees:
        name = emp["name"]
        rate = emp["hourly_rate"]
        hours = emp["hours_per_week"]

        basic = basic_salary(rate, hours)
        gross = gross_salary(basic)
        tax = tax_amount(basic)
        bracket = salary_bracket(gross)

        print(f"{name:<20}{basic:<20,.2f}{gross:<20,.2f}{tax:<10,.2f}{bracket:<15}")

    print("=" * 80)
    print("End of Report\n")


employees = []

print("Enter details for 3 employees:\n")
for i in range(1, 4):
    print(f"--- Employee {i} ---")
    name = input("Enter employee name: ")
    rate = float(input("Enter hourly rate (Rs.): "))
    hours = float(input("Enter hours worked per week: "))
    employees.append({
        "name": name,
        "hourly_rate": rate,
        "hours_per_week": hours
    })
    print()

employee_report(employees)
