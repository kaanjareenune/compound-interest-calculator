# compound-interest-calculator

A Python command-line application that calculates compound interest (with or without monthly contributions) and visualizes portfolio growth over time.

## Features
- Calculates compound interest with custom principal amount, interest rate (decimal), number of years, monthly contribution, and compounding frequency (if no monthly contributions)
- Calculates final portfolio value and the total interest earned
- Visualizes portfolio growth using matplotlib
- Input validation with user-friendly error handling

## How it Works
- Without monthly contributions
  - Used the basic compound interest formula (A = P(1 + (r/n))^(nt)) where P = principal, r = annual interest rate (decimal), n = compounding frequency per year, t = number of years, and A = final amount
  - Applied interest per compounding period, tracks portfolio value at each period, and then displays growth on a graph
- With monthly contributions
  - Converts annual interest rate to monthly rate, applies monthly compounding, adds monthly contribution after each interest is applied, tracks portfolio growth over time, and displays a growth chart
- Visualization
  - Graph shows portfolio growth over time
  - X-axis = Months or Compounding Periods (depending on compounding frequency and monthly contributions amount)
  - Y-axis = Portfolio Values ($)
  - Automatically updates based on input
 
## Requirements
- Python 3
- matplotlib
- numpy

## Run Application
- First clone and the cd to repository
- Run following commands:
  - pip install -r requirements.txt
  - python compound_calculator.py


