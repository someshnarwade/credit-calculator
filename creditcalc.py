import argparse
import math
import sys

parser = argparse.ArgumentParser(description='Credit Calculator - calculate annuity and differentiated payements')

parser.add_argument('--type', help='the type of payment', type=str)
parser.add_argument('--payment', help='the monthly payment', type=float)
parser.add_argument('--principal', type=float)
parser.add_argument('--periods', help='the number of months', type=int)
parser.add_argument('--interest', type=float)

args = parser.parse_args()

def annuity_calculator():
    print('Hello, annuity')

if len(sys.argv) < 4:
    print('Incorrect parameters')
    sys.exit()
if args.type not in ['diff', 'annuity']:
    print('Incorrect parameters')
    sys.exit()
if args.type == 'diff' and args.payment:
    print('Incorrect parameters')
    sys.exit()
if args.interest is None:
    print('Incorrect parameters')
    sys.exit()

if args.type == 'diff':
    if args.principal < 0 or args.periods < 0 or args.interest < 0:
        print('Incorrect parameters')
        sys.exit()
        
    principal = args.principal
    months = args.periods
    interest = args.interest/1200
    total = 0

    for month in range(1, months+1):
        payment = math.ceil((principal/months) + interest * (principal - ((principal * (month - 1)/months))))
        print(f'Month {month}: paid out {payment}')
        total += payment
    print('Overpayment =', round(total - principal))
        
else:
    if args.periods is None:
        # Get all variables
        if args.principal < 0 or args.payment < 0 or args.interest < 0:
            print('Incorrect parameters')
            sys.exit()
        principal = args.principal
        payment = args.payment
        interest = args.interest/1200
    
        # Calculating number of months
        x = payment/(payment - interest * principal)
        months = round(math.log(x, 1 + interest), 2)
        overpayment = round(payment * math.ceil(months) - principal)
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
        print(f'Overpayment = {overpayment}')

    elif args.payment is None:
        # Get all the variables
        if args.principal < 0 or args.periods < 0 or args.interest < 0:
            print('Incorrect parameters')
            sys.exit()
        principal = args.principal
        months = args.periods
        interest = args.interest/1200
    
        # Calculating Annuity Monthly payment
        c = math.pow(1 + interest, months)   # (1+i) ** n
        payment = math.ceil(principal * ((interest * c) / (c - 1)))
        overpayment = round(payment * months - principal)
        # Output Logic
        print(f'Your annuity payment = {payment}!')
        print(f'Overpayment = {overpayment}')
     
    elif args.principal is None:
        # Get all variables
        if args.payment < 0 or args.periods < 0 or args.interest < 0:
            print('Incorrect parameters')
            sys.exit()
        payment = args.payment
        months = args.periods
        interest = args.interest/1200
    
        # Calculating Credit Principal
        c = math.pow(1 + interest, months)
        principal = math.floor(payment / ((interest * c) / (c - 1)))
        overpayment = payment * months - principal
        overpayment = round(overpayment)
        # Output logic
        print(f'Your credit principal: {principal}!')
        print(f'Overpayment = {overpayment}')
