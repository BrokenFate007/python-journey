## Part A: House Hunting

You've just graduated from MIT and have a great new job. [cite_start]You've moved to the San Francisco Bay Area and want to start saving for a house[cite: 14, 15]. [cite_start]As housing prices are high, you'll need to save for several years to afford a down payment[cite: 16].

In Part A, your task is to determine how many months it will take to save enough for a down payment, based on the following assumptions:

1.  [cite_start]**total_cost**: The cost of your dream home[cite: 18].
2.  [cite_start]**portion_down_payment**: The down payment is 25% (0.25) of the `total_cost`[cite: 19].
3.  [cite_start]**current_savings**: You start with \$0 in savings[cite: 20].
4.  [cite_start]**r**: Your savings earn an annual return of 4% (0.04)[cite: 22]. [cite_start]At the end of each month, your savings increase by `current_savings*r/12`[cite: 21].
5.  [cite_start]**annual_salary**: Your starting annual salary[cite: 23].
6.  [cite_start]**portion_saved**: The percentage of your salary you dedicate to saving each month, in decimal form (e.g., 0.1 for 10%)[cite: 25].
7.  [cite_start]Each month, your savings increase by the investment return plus a portion of your monthly salary (`annual_salary / 12`)[cite: 26].

**Your Program Should:**

* [cite_start]Ask the user to input their `annual_salary`, `portion_saved`, and `total_cost`[cite: 30, 31, 32, 33].
* [cite_start]Calculate and print the number of months it will take to save for the down payment[cite: 27].

***

## Part B: Saving, with a Raise

[cite_start]In this part, you'll build on your solution from Part A by including a raise every six months[cite: 61].

**Assumptions:**

* [cite_start]Investments still have an annual return of 4% (r=0.04) and the down payment is 25% of the total cost[cite: 67].
* [cite_start]You will receive a semi-annual raise[cite: 64]. [cite_start]After the 6th, 12th, 18th month, and so on, your salary will increase by a fixed percentage[cite: 65].

**Your Program Should:**

* [cite_start]Copy your solution from Part A[cite: 62].
* [cite_start]Ask the user for their `annual_salary`, `portion_saved`, `total_cost`, and `semi_annual_raise`[cite: 68, 70, 71, 72].
* [cite_start]Calculate and print the number of months it will take to save for the down payment, accounting for the semi-annual raises[cite: 66].

***

## Part C: Finding the Right Amount to Save Away

[cite_start]For this final part, your goal is to determine the best savings rate (`portion_saved`) to afford a down payment on a \$1M house in exactly 36 months[cite: 115, 116].

**Assumptions:**

* [cite_start]Semi-annual raise is fixed at 7% (0.07)[cite: 112].
* [cite_start]Annual investment return is 4% (0.04)[cite: 113].
* [cite_start]The down payment is 25% of the \$1M house cost[cite: 114].
* [cite_start]Your savings only need to be within \$100 of the required down payment[cite: 117].

**Your Program Should:**

* [cite_start]Ask the user to enter their starting `annual_salary`[cite: 140, 147, 153].
* [cite_start]Use a **bisection search** to efficiently find the savings rate[cite: 119].
* [cite_start]The search range for the savings rate should be integers from 0 to 10,000 to represent two decimal places of accuracy (0% to 100%)[cite: 123, 125].
* [cite_start]Keep track of the number of steps the bisection search takes[cite: 120].
* [cite_start]If a solution is impossible (even a 100% savings rate isn't enough), print a message stating that it is not possible to save for the down payment[cite: 129].
* [cite_start]Print the best savings rate as a decimal and the number of steps in the search[cite: 126, 141, 142].