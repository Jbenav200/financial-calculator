import math

# Par Value of the bond
PARVAL = 1000
# Coupon rate of the bond is 1.5% represented as a float that is 0.015
COUPON = 0.015
# Each quarter has a different annual spot rate
Q1RATE = 0.05
Q2RATE = 0.06
Q3RATE = 0.07
Q4RATE = 0.08
# add the spot rates to an array/list
quarter_rates = [Q1RATE, Q2RATE, Q3RATE, Q4RATE]
quarter_times = [0.25, 0.5, 0.75, 1]

# sort the list to ensure that it is lowest to highest
# as each quarter the annual spot rate increases by 1%.
quarter_rates.sort()
quarter_times.sort()
'''
    Calculate the present value of the cash flows by doing the following:
    1. apply the coupon value to the par value to get the first three quarter's payments 1000 * 0.015 = 15.0
    2. apply the coupon value to the par value and add the par value to get the final quarter value 1000 * 0.015 + 1000 = 1015.0
    3. for each quarter apply the rate for that quarter into the equation: couponValue / (1 + rate ) ^ t where t = 1
    4. return the value 
'''


def calculate_pv_of_bond():
    coupon_payment_value = PARVAL * COUPON
    final_coupon = PARVAL + PARVAL * COUPON
    pv_of_cash_flow = 0.0
    totals = []
    for rate, time in zip(quarter_rates, quarter_times):
        if rate != 0.08:
            pv_of_cash_flow = coupon_payment_value / pow((1 + (rate/4)), time)
            totals.append(pv_of_cash_flow)
        else:
            pv_of_cash_flow = final_coupon / pow((1 + (rate/4)), time)
            totals.append(pv_of_cash_flow)
    pv_of_cash_flow = sum(totals)
    return pv_of_cash_flow


if __name__ == '__main__':
    '''
        the present value of the bond can be calculated by adding the present value of capital returned
        and present value of the cash flows together.
    '''
    value = calculate_pv_of_bond()
    print(f'If a bond is issued with a par value of £{PARVAL} and a quarterly Coupon rate of 1.5%')
    print(f'and compounds interest quarterly with the respective annual spot rates: {quarter_rates}')
    print(f'The value of the bond is: £{round(value, 2)}')
