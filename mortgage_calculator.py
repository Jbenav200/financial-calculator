LOAN_AMOUNT = 10000
INTEREST_RATE = 0.06
TERM = 10
LOAN_REPAYMENT = LOAN_AMOUNT / TERM + (LOAN_AMOUNT * INTEREST_RATE)

'''
    CALCULATE THE PAYMENT VALUE INCLUDING INTEREST WHEN LOAN REPAID AT THE END OF EACH YEAR
    WITH 10 EQUAL PAYMENTS.
'''


def calc_end_of_year():
    value = LOAN_AMOUNT
    for i in range(1, TERM + 1):
        value = value + (LOAN_AMOUNT * INTEREST_RATE) - LOAN_REPAYMENT
        print(f'Repaid for year {i}: ${LOAN_REPAYMENT}')
        print(f'End of year {i} Value: ${value}')
    return value


'''
    CALCULATE THE PAYMENT VALUE INCLUDING COMPOUNDING INTEREST 
    IF THE LOAN IS REPAID AT THE BEGINNING OF EACH YEAR
'''


def calc_beg_of_year():
    '''
        because the interest is annual, applying compound interest
        is required. first the interest rate is calculated
    '''
    interest = INTEREST_RATE / 12
    '''
        Beginning of the year is a vague term, so I have made the assumption
        that the payment could be made at the end of any month within the first
        quarter of the year.
    '''
    months = ['Jan', 'Feb', 'March']
    print(f'taking into account compounding interest')
    for month in months:
        if month == 'Jan':
            value = LOAN_AMOUNT / TERM + ((LOAN_AMOUNT * interest) * 1)
        elif month == 'Feb':
            value = LOAN_AMOUNT / TERM + ((LOAN_AMOUNT * interest) * 2)
        else:
            value = LOAN_AMOUNT / TERM + ((LOAN_AMOUNT * interest) * 3)
        print(f'If the annual payment is made in {month}: ${value}')


def six_year_payment():
    pass


if __name__ == '__main__':
    print('Question 2a.')
    eoyVal = calc_end_of_year()
    print(f'If the annual payment is made at the end of the year each payment will be: ${round(LOAN_REPAYMENT,2)}')
    print('Question 2b.')
    calc_beg_of_year()
