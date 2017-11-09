# Import the months_needed_with_raise from part b
from ps1b import calc_months_needed_with_raise

# Import the ceiling function from math
from math import ceil

# Store the assumptions from the ps1c PDF
# 1. Your semi-annual raise is .07 (7%)
semi_annual_raise = 0.07
# 2. Your investments have an annual return of 0.04 (4%)
r = 0.04
# 3. The down payment is 0.25 (25%) of the cost of the house
portion_down_payment = 0.25
# 4. The cost of the house that you are saving for is $1M.
total_cost = 1000000
# You would like to purchase a house within three years
goal_month_duration = 36

# Caclulate the down payment from the house cost and down payment portion
down_payment_cost = portion_down_payment * total_cost


# Find the minimum portion of income to save in order to buy a house based on the assumptions from the top of the file.
#
# salary - The salary to search for an income portion for
def find_savings_rate_from_salary(salary):
    # Setup the local variables for the bisection search
    left = 0
    right = 10000
    midpoint = 0
    i = 0
    months_needed_midpoint = 0

    # Search until we converage on a single point
    while right-left > 1:
        midpoint = ceil(right-left) / 2.0 + left

        months_needed_midpoint = calc_months_needed_with_raise(salary, midpoint / 10000.0, total_cost, semi_annual_raise)

        if months_needed_midpoint <= goal_month_duration:
            right = midpoint
        else:
            left = midpoint

        i += 1

    # If we converged, but we still didn't meet the requirement, then it's impossible to pay. Return a negative value.
    if months_needed_midpoint > goal_month_duration:
        return -1, -1

    # Return the savings rate and and the number of iterations it took to get there
    return midpoint / 10000.0, i


# Test that the function performs properly for all test cases from the PDF
def test():
    print 'Testing...'
    assert (find_savings_rate_from_salary(150000)[0] - 0.4411) < 0.01
    assert (find_savings_rate_from_salary(300000)[0] - 0.2206) < 0.01
    assert find_savings_rate_from_salary(10000) == (-1, -1)
    print 'Passed.'


# Ask a user for input an run the calculation
def main():
    salary = input('Enter the starting salary: ')
    x, i = find_savings_rate_from_salary(salary)
    if x > 0:
        print 'Best savings rate: ', x
        print 'Steps in bisection search: ', i
    else:
        print 'It is not possible to pay the down payment in three years.'


# If somebody runs this file, run the tests then run the UI
if __name__ == '__main__':
    test()
    main()