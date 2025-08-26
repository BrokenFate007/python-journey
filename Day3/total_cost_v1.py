annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percentage of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25*total_cost

current_saving = 0
r = 0.04
months_needed = 0

while ((portion_down_payment) >= current_saving):
    current_saving = (current_saving*(12+r)/12) + portion_saved*annual_salary/12
    months_needed = months_needed + 1
print("Number of months:", months_needed)