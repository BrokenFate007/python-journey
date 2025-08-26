annual_salary = float(input("Enter your annual salary: "))

semi_annual_raise = 0.07
r = 0.04
total_cost = 1000000
epsilon = 100
down_payment = 0.25*total_cost
month_target = 36


low = 0
high = 10000
steps = 0

while low<=high:
    current_saving = 0
    portion_saved_guess = int((low+high)/2)
    temp_annual_salary = annual_salary
    for month in range(36):
        monthly_contribution = (temp_annual_salary/12)*(portion_saved_guess/10000)
        current_saving +=current_saving*(r/12)+monthly_contribution
        if (month%6 == 0) and ( month > 0):
            temp_annual_salary+=temp_annual_salary*semi_annual_raise
    if abs(current_saving-down_payment)<epsilon:
        print("Best saving rate: ",portion_saved_guess/10000)
        break
    elif current_saving<down_payment:
        low = portion_saved_guess
    elif current_saving>down_payment:
        high = portion_saved_guess
    steps+=1

print("Steps in Bisection search:",steps)
    
