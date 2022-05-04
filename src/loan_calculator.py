LOAN_AMOUNT = 10000.00
INTEREST_RATE = 0.06
TERM = 10
# LOAN_REPAYMENT = LOAN_AMOUNT / TERM + (LOAN_AMOUNT * INTEREST_RATE)
LOAN_TABLE = []

'''
    CALCULATE THE PAYMENT VALUE INCLUDING INTEREST WHEN LOAN REPAID AT THE END OF EACH YEAR
    WITH 10 EQUAL PAYMENTS.
'''


def calc_end_of_year(amount, interest, time):
    """
        The formula to calculate equal payments, where L = loan amount, r = rate, t = time is:
        L * r * 1 + i ^ t / 1 + i ^ t - 1
    """
    repayment = amount * (interest * pow(1 + interest, time)) / (pow(1 + interest, time) - 1)
    return repayment


"""
    CALCULATE THE PAYMENT VALUE INCLUDING COMPOUNDING INTEREST 
    IF THE LOAN IS REPAID AT THE BEGINNING OF EACH YEAR
"""


def calc_beg_of_year(amount, interest_rate, term):
    """
        because the interest is annual, applying compound interest
        is required. first the interest rate is calculated
    """
    interest = interest_rate / 12
    """
        Beginning of the year is a vague term, so I have made the assumption
        that the payment could be made at the end of any month within the first
        quarter of the year.
    """
    months = ['Jan', 'Feb', 'March']
    print(f'taking into account compounding interest')
    for month in months:
        if month == 'Jan':
            value = amount / term + ((amount * interest) * 1)
        elif month == 'Feb':
            value = amount / term + ((amount * interest) * 2)
        else:
            value = amount / term + ((amount * interest) * 3)
        print(f'If the annual payment is made in {month}: ${value},')


"""
    Create a multidimensional array to act as an Amortization table
    with a row for each: 
        year, 
        loan value,
        interest accrued,
        payment value,
        remaining value
"""
def generate_table(amount, interest, term):
    repayment_value = calc_end_of_year(amount, interest, term)
    for i in range(1, TERM + 1):
        if i == 1:
            LOAN_TABLE.append([i, LOAN_AMOUNT, round(LOAN_AMOUNT * INTEREST_RATE, 2), round(repayment_value, 2),
                               LOAN_AMOUNT + LOAN_AMOUNT * INTEREST_RATE - round(repayment_value, 2)])
        else:
            LOAN_TABLE.append(
                [
                    i,
                    round(LOAN_TABLE[i - 2][1] + LOAN_TABLE[i - 2][2] - LOAN_TABLE[i - 2][3], 2),
                    round((LOAN_TABLE[i - 2][1] + LOAN_TABLE[i - 2][2] - LOAN_TABLE[i - 2][3]) * INTEREST_RATE, 2),
                    round(repayment_value, 2),
                    round((LOAN_TABLE[i - 2][1] +
                           LOAN_TABLE[i - 2][2] - LOAN_TABLE[i - 2][3] +
                           (
                                   (LOAN_TABLE[i - 2][1] + LOAN_TABLE[i - 2][2] -
                             LOAN_TABLE[i - 2][3]) * INTEREST_RATE
                           ) - round(repayment_value, 2)), 2)
                ]
            )
    print(['Y', 'L Val', 'I', 'P Val', 'Rem Amount'])
    for i in range(0, len(LOAN_TABLE)):
        print(str(LOAN_TABLE[i]))


def mid_year_six(table, interest_rate):
    year_six_beg = table[5][1]
    paym = 2000.00
    interest = year_six_beg * ((interest_rate/12) * 0.5)
    remaining = year_six_beg + interest - paym
    return remaining


def how_many_years(remaining_val):
    repayment_val = calc_end_of_year(remaining_val, INTEREST_RATE, 4)
    print(f'new repayment value: ${round(repayment_val, 2)}')
    eoy_six_val = remaining_val
    eoy_seven_val = round((remaining_val + (eoy_six_val * INTEREST_RATE) - repayment_val), 2)
    eoy_eight_val = round((eoy_seven_val + (eoy_seven_val * INTEREST_RATE) - repayment_val), 2)
    eoy_nine_val = round((eoy_eight_val + (eoy_eight_val * INTEREST_RATE) - repayment_val), 2)
    eoy_ten_val = round((eoy_nine_val + eoy_nine_val * INTEREST_RATE - repayment_val), 2)
    if eoy_ten_val >= 1:
        x = 5
    else:
        x = 4
    print(f'considering the new repayment value, the loan will be paid of in {x} years')


"""
    START RUNNING PROGRAM
"""
if __name__ == '__main__':
    print('Question 2a.')
    eoy_val = calc_end_of_year(LOAN_AMOUNT, INTEREST_RATE, TERM)
    print(f'${round(eoy_val, 2)} is the value of the 10 equal payments.')
    print('\n')
    print('Question 2b.')
    calc_beg_of_year(LOAN_AMOUNT, INTEREST_RATE, TERM)
    print(f'else, the annual payment will be ${LOAN_AMOUNT / TERM}.')
    print('\n')
    print('LOAN TABLE')
    generate_table(LOAN_AMOUNT, INTEREST_RATE, TERM)
    print('\n')
    print('Question 2c.')
    print(f'The EOY value for year six will be: ${LOAN_TABLE[5][4]}')
    print(f'The amount paying off the principle will be ${round(LOAN_TABLE[5][3] - LOAN_TABLE[5][2], 2)}')
    print('\n')
    print('Question 2d.')
    remainder = mid_year_six(LOAN_TABLE, INTEREST_RATE)
    print(f'The remaining value after paying $2000 halfway through year six is: {round(remainder, 2)}')
    how_many_years(remainder)
