import math

# print the welcome message 
welcome_message = '''
investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan
'''
print(welcome_message)

# request which calculation the user would like
while (True):
    calculation = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
    # ensuring the input is not case-sensitive
    lowercase_calculation = ''.join([character.lower() for character in calculation])

    # if 'investment' is entered
    if (lowercase_calculation == "investment"):
        
        # asking user to enter quantity they will deposit
        while (True): 
            money_amount_str = input("How much money are you depositing? £")
            
            # casting from a string to a float in order to ensure it can be used in formula
            try:
                money_amount = float(money_amount_str)
            
            # if casting is not possible, printing error message and returning user to re-enter quantity
            except:
                print("Error. Please enter a valid amount.")
                continue     
            break

        # asking user for interest rate
        while (True): 
            interest_rate_str = input("What is the interest rate? ")
            
            # casting from a string to a float in order to ensure it can be used in formula
            try:
                interest_rate = float(interest_rate_str)
                
                # converting float into a percentage by dividing by 100
                interest_rate_perc = interest_rate / 100
            
            # if casting not possible, printing error message and returning user to re-enter interest rate
            except:
                print("Error. Please enter a valid amount.")
                continue     
            break

        # asking user for number of years investing
        while (True): 
            num_years_str = input("For how many years do you want to invest? ")
            
            # casting from a string to a float in order to ensure it can be used in formula
            try:
                num_years = float(num_years_str)
            
            # if casting not possible, printing error message and returning user to re-enter number of years
            except:
                print("Error. Please enter a valid amount.")
                continue     
            break

        # asking what type of interest the user wants - simple or compound
        while (True): 
            interest = input("Do you want your interest to be simple or compound? ")
            # ensuring the input is not case-sensitive
            lowercase_interest = ''.join([character.lower() for character in interest])

            # if 'simple' is entered
            if (lowercase_interest == "simple"):
                # calculate simple interest using formula
                total_simple_balance = money_amount * (1 + interest_rate_perc * num_years)
                
                # printing balance to two decimal points and all the values entered for clarity of printed statment for user
                print(f"Your total balance starting with £{money_amount_str} deposited; an interest rate of {interest_rate_str}%; for {num_years_str} years; and simple interest will be £{total_simple_balance:.2f}.")

            # if 'compound' is entered
            elif (lowercase_interest == "compound"):
                # calculate compound interest using formula
                total_compound_balance = money_amount * math.pow((1 + interest_rate_perc), num_years)

                # printing balance to two decimal points and all the values entered for clarity of printed statment for user
                print(f"Your total balance starting with £{money_amount_str} deposited; an interest rate of {interest_rate_str}%; for {num_years_str} years; and compound interest will be £{total_compound_balance:.2f}.")

            # if neither 'simple' nor 'compound' is entered,  printing error message and returning user to re-enter interest selection
            else:
                print("Error. Please enter a valid option from the menu.")
                continue
            break

    # if 'bond' is entered
    elif (lowercase_calculation == "bond"):

        # asking user to enter the value of their house
        while (True): 
            house_value_str = input("What is the value of your house? £")
            
            # casting from a string to a float in order to ensure it can be used in formula
            try:
                house_value = float(house_value_str)
            
            # if casting not possible, printing error message and returning user to re-enter value of house
            except:
                print("Error. Please enter a valid amount.")
                continue     
            break

        # asking user to enter the interest rate
        while (True): 
            interest_rate_str = input("What is the interest rate? ")
            
            # casting from a string to a float in order to ensure it can be used in formula
            try:
                interest_rate = float(interest_rate_str)

                # converting float into a percentage by dividing by 100
                annual_interest_rate_perc = interest_rate / 100

                # dividing percentage by 12 to calculate value per month
                monthly_interest_rate = annual_interest_rate_perc / 12
            
            # if casting not possible, printing error message and returning user to re-enter interest rate
            except:
                print("Error. Please enter a valid amount.")
                continue     
            break

        # asking user to enter over how many months they would like to spread the repayments
        while (True): 
            num_months_str = input("Over how many months do you want to repay? ")
            
            # casting from a string to a float in order to ensure it can be used in formula
            try:
                num_months = float(num_months_str)
            
            # if casting not possible, printing error message and returning user to re-enter months
            except:
                print("Error. Please enter a valid amount.")
                continue     
            break
        
        # calculate repayment amount per month using formula
        repayment_per_month = (monthly_interest_rate * house_value)/(1 - (1 + monthly_interest_rate)**(-num_months))
        
        # formatting monetary figures to print to two decimal points
        rounded_repay_per_month = "{:.2f}".format(repayment_per_month)

        # printing balance to two decimal points and all the values entered for clarity of printed statment for user
        print(f"With a house worth £{house_value_str}; and with an interest rate of {interest_rate_str}%; your monthly repayments will be £{repayment_per_month:.2f}.")

    # if neither 'investment' nor 'bond' is entered,  printing error message and returning user to re-enter calculation selection
    else:
        print("Error. Please enter a valid option from the menu.")
        continue
    break


        
    
