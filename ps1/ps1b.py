# Write a program to calculate how many months it will take you save up enough money for a down payment. Like before,
# assume that your investments earn a return of r = 0.04 (or 4%) and the required down payment perventage is 0.25
# (or 25%).
#
# Have the user enter the following variables:
# 1. The starting annual salary (annual_salary)
# 2. The percentage of salary to be saved (portion_saved)
# 3. The cost of your dream home (total_cost)
# 4. The semi-annual salary raise (semi_annual_raise)

# Assumed constants
portion_down_payment = 0.25  # 25% down payment on a house
r = 0.04  # ROI on investments


# Function to test-ably perform the functionality of the lab
def calc_months_needed_with_raise(annual_salary, portion_saved, total_cost, semi_annual_raise):
    # Calculate the cost of the down payment
    cost_down_payment = portion_down_payment * total_cost

    # Initialize current savings and months to 0
    current_savings = 0
    month = 0

    while current_savings <= cost_down_payment:
        # Add interest BEFORE adding paycheck
        current_savings += (r/12.0 * current_savings)

        # Add the monthly salary
        current_savings += (annual_salary / 12.0 * portion_saved)

        # Increment the month
        month += 1

        # Increase the annual salary according to semi annual raise every 6 months
        #  Do this after the month += 1 and savings contributions so that it doesn't
        #  run on month 0
        if month % 6 == 0:
            annual_salary += semi_annual_raise * annual_salary

    return month


# Test using the HW test cases
def test():
    print 'Testing...'
    assert calc_months_needed_with_raise(120000, .05, 500000, .03) == 142
    assert calc_months_needed_with_raise(80000, .1, 800000, .03) == 159
    assert calc_months_needed_with_raise(75000, .05, 1500000, .05) == 261
    print 'Passed.'


# If somebody runs this file, test the stuff
if __name__ == '__main__':
    test()
