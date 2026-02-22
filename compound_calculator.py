import matplotlib.pyplot as plt
import numpy as np

def main():
    # get inputs from user for principal, interest_rate, years, and compounding_frequency
    principal = get_principal_input()
    interest_rate = get_interest_rate_input()
    years = get_years_input()
    monthly_contribution = get_monthly_contribution_input()
    compounding_frequency = 0
    if monthly_contribution == 0:
        compounding_frequency = get_compounding_frequency_input()

    # calculate the final amount and the interest earned (no monthly contribution)
    if monthly_contribution == 0:
        final_amount, interest_earned, periods, portfolio_vals = calculate_compound(
            principal,
            interest_rate,
            years,
            compounding_frequency,
        )
        # if compounding frequency = 12, x-axis in graph will be months, else it will be compounding periods
        if compounding_frequency == 12:
            x_axis_label = "Months"
        else:
            x_axis_label = "Compounding Periods"
    # calculate the final amount and interest earned with monthly contribution
    else:
        final_amount, interest_earned, periods, portfolio_vals = calculate_with_monthly_investment(
            principal,
            interest_rate,
            years,
            monthly_contribution
        )
        x_axis_label = "Months"

    # display formatted final amount and interest earned
    display_results(final_amount, interest_earned)

    plot_portfolio_growth(portfolio_vals, periods, x_axis_label)


# get user inputs methods
def get_principal_input():
    while True:
        try:
            principal_input = float(input("Enter the principal amount: "))
            if principal_input < 0:
                raise ValueError("Principal can't be negative.")
            return principal_input
        except ValueError as e:
            print(f"Invalid input: {e}")

def get_interest_rate_input():
    while True:
        try:
            interest_rate = float(input("Enter the interest rate (in decimal): "))
            if interest_rate < 0:
                raise ValueError("Interest rate can't be negative.")
            return interest_rate
        except ValueError as e:
            print(f"Invalid input: {e}")

def get_years_input():
    while True:
        try:
            years = float(input("Enter the number of years: "))
            if years < 0:
                raise ValueError("Number of years can't be negative.")
            return years
        except ValueError as e:
            print(f"Invalid input: {e}")

def get_compounding_frequency_input():
    while True:
        try:
            compounding_frequency = float(input("Enter the compounding frequency (times per year): "))
            if compounding_frequency <= 0:
                raise ValueError("Compounding frequency must be greater than 0.")
            return compounding_frequency
        except ValueError as e:
            print(f"Invalid input: {e}")

def get_monthly_contribution_input():
    while True:
        try:
            monthly_contribution = float(input("Enter the monthly contribution amount: "))
            if monthly_contribution < 0:
                raise ValueError("Monthly contribution can't be negative.")
            return monthly_contribution
        except ValueError as e:
            print(f"Invalid input: {e}")

# calculate the final amount and interest earned using basic compound interest formula
def calculate_compound(principal, interest_rate, years, compounding_frequency):
    balance = principal
    portfolio_values = [balance]

    total_periods = int(compounding_frequency * years)
    period_rate = interest_rate / compounding_frequency

    for period in range(total_periods):
        balance *= (1 + period_rate)
        portfolio_values.append(balance)

    interest_earned = balance - principal
    return balance, interest_earned, total_periods, portfolio_values

# calculate the final amount and interest earned using compound interest formula with monthly contributions
def calculate_with_monthly_investment(principal, interest_rate, years, monthly_contribution):
    balance = principal
    portfolio_values = [balance]

    # edge case: years = 0
    if years == 0:
        return principal, 0, 0, [principal]

    # convert to monthly compounding for accurate monthly deposits
    total_months = int(years * 12)

    # calculate monthly interest rate
    monthly_rate = interest_rate / 12

    for month in range(total_months):
        # apply monthly interest
        balance *= (1 + monthly_rate)

        # add monthly contribution
        balance += monthly_contribution
        portfolio_values.append(balance)

    total_contributions = principal + (monthly_contribution * total_months)
    interest_earned = balance - total_contributions

    return balance, interest_earned, total_months, portfolio_values

# format the results to 2 decimal places and output final amount and interest earned
def display_results(final_amount, interest):
    final_amount_formatted = f"{final_amount:.2f}"
    interest_formatted = f"{interest:.2f}"
    print(f"The final amount is {final_amount_formatted} and your interest earned is {interest_formatted}")

# plot portfolio growth over time
def plot_portfolio_growth(portfolio_values, x_values, x_axis_label):
    # create a list of x values
    x_axis_list = np.arange(0, x_values + 1)

    plt.figure(figsize=(10, 6))
    plt.plot(x_axis_list, portfolio_values, label="Portfolio Value")

    # Add labels and titles
    plt.xlabel(x_axis_label)
    plt.ylabel("Portfolio Value ($)")
    plt.title("Portfolio Growth Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
