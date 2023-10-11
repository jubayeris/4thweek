def computepay(hours, rate):
    if hours > 40:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * (1.5 * rate)
        total_pay = regular_pay + overtime_pay
    else:
        total_pay = hours * rate
    return total_pay

try:
    hours = float(input("Enter the number of hours worked: "))
    rate = float(input("Enter the hourly rate: "))
    salary = computepay(hours, rate)
    print(f"Total salary: {salary}")
except ValueError:
    print("Error: Please enter valid numeric values for hours and rate")
