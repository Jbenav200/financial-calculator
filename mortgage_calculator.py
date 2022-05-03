LOAN_AMOUNT = 10000
INTEREST_RATE = 0.06
TERM = 10
# LOAN_REPAYMENT = LOAN_AMOUNT / TERM + (LOAN_AMOUNT * INTEREST_RATE)
TABLE = []
'''
    CALCULATE THE PAYMENT VALUE INCLUDING INTEREST WHEN LOAN REPAID AT THE END OF EACH YEAR
    WITH 10 EQUAL PAYMENTS.
'''


def calc_end_of_year():
    repayment = LOAN_AMOUNT * (INTEREST_RATE * pow(1 + INTEREST_RATE, 10))/(pow(1 + INTEREST_RATE, 10)-1)
    return repayment


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
    repayment_value = calc_end_of_year()
    for i in range(1, TERM + 1):
        if i == 1:
            TABLE.append([i, LOAN_AMOUNT, LOAN_AMOUNT * INTEREST_RATE, round(repayment_value, 2), LOAN_AMOUNT + LOAN_AMOUNT * INTEREST_RATE - round(repayment_value, 2)])
        else:
            TABLE.append(
                [
                    i,
                    round(TABLE[i-2][1] + TABLE[i-2][2] - TABLE[i-2][3], 2),
                    round((TABLE[i-2][1] + TABLE[i-2][2] - TABLE[i-2][3]) * INTEREST_RATE, 2),
                    round(repayment_value, 2),
                    round((TABLE[i-2][1] + TABLE[i-2][2] - TABLE[i-2][3] + ((TABLE[i-2][1] + TABLE[i-2][2] - TABLE[i-2][3]) * INTEREST_RATE) - round(repayment_value, 2)), 2)
                ]
            )
    for i in range(0, len(TABLE)):
        if i == 1:
            str(TABLE[i]) + '\n'
        else:
            print(f'year {i + 1}')
        print(str(TABLE[i]) + '\n')


if __name__ == '__main__':
    print('Question 2a.')
    value = calc_end_of_year()
    print(f'${round(value, 2)}')
    # eoyVal = calc_end_of_year()
    # print(f'If the annual payment is made at the end of the year each payment will be: ${round(LOAN_REPAYMENT,2)}')
    print('Question 2b.')
    calc_beg_of_year()
    print('Question 2c.')
    six_year_payment()
