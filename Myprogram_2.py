#Royce Daniel 2/27/2026 "Tax Calculator"

#START

# Set state tax rate = 0.05
# Set county tax rate = 0.025
#
# Define Function taxCalculation(sales)
#
#     Set stateTax = sales × state tax rate
#     Set countyTax = sales × county tax rate
#     Set grandTaxes = stateTax + countyTax
#
#     Return stateTax, countyTax, grandTaxes
#
# End Function
#
#
# Display "Enter in the total sales for the month:"
# Input totalSales
#
# Call taxCalculation(totalSales)
# Store returned values as:
#     stateTax
#     countyTax
#     grandTaxes
#
# Display "State sales tax: $" , stateTax
# Display "County sales tax: $" , countyTax
# Display "Total sales tax: $" , grandTaxes
#
# END
srate=0.05
crate=0.025
def taxcalculation(sales):
    statetax = sales * srate
    countytax = sales * crate
    grandtaxes= countytax + statetax


    return statetax, countytax, grandtaxes

total_sales = float(input("Enter in the total sales for the month: "))
statetax, countytax, grandtaxes = taxcalculation(total_sales)
print("State sales tax: $", statetax)
print("County sales tax: $", countytax)
print("Total sales tax: $", grandtaxes)
