import math

print('''What do you want to calculate?
type "n" for the count of months,
type "a" for the annuity monthly payment,
type "p" for the credit principal:''')

choice = input()

if (choice.lower() == 'n'):
    # Get all variables
    print('Enter the credit principal:')
    principal = float(input())
    print('Enter the monthly payment:')
    annuity_payment = float(input())
    print('Enter the credit interest:')
    interest = float(input())/1200
    
    # Calculating number of months
    x = annuity_payment/(annuity_payment - interest * principal)
    months = round(math.log(x, 1 + interest), 2)
    if months % 1 > 0.00:
        months = round(months) + 1
    # Output Logic
    if months == 12:
        print('You need 1 year to repay this credit!')
    elif months > 12:
        years = math.floor(months/12)
        remaining_months = months % 12          
        print(f'You need {years} years and {remaining_months} months to repay this credit!')
    else:
        print(f'You need {months} months to repay this credit!')  

elif (choice.lower() == 'a'):
    # Get all the variables
    print('Enter the credit principal:')
    principal = float(input())
    print('Enter the number of periods:')
    months = int(input())
    print('Enter the credit interest:')
    interest = float(input())/1200
    
    # Calculating Annuity Monthly payment
    c = math.pow(1 + interest, months)   # (1+i) ** n
    annuity_payment = math.ceil(principal * ((interest * c) / (c - 1)))
    
    # Output Logic
    print(f'Your annuity payment = {annuity_payment}')
     
elif (choice.lower() == 'p'):
    # Get all variables
    print('Enter the annuity payment:')
    annuity_payment = float(input())
    print('Enter the count of periods:')
    months = float(input())
    print('Enter the credit interest:')
    interest = float(input())/1200
    
    # Calculating Credit Principal
    c = math.pow(1 + interest, months)
    principal = round(annuity_payment / ((interest * c) / (c - 1)))
    
    # Output logic
    print(f'Your credit principal: {principal}!')
        
