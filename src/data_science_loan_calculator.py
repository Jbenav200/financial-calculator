import pandas as pd

def create_amortization_table(amount, interest, time):
    data = {
        "year": [],
        "loan_value": [],
        "interest": [],
        "repayment": [],
        "remaining": []
    }
    repayment = calculate_repayment(amount, interest, time)
    for i in range(1, time + 1):
        data['year'].append(i)
        data['repayment'].append(round(repayment, 2))
        if i == 1:
            data['loan_value'].append(amount)
            data['interest'].append(amount * interest)
            data['remaining'].append(data['loan_value'][i-1] + data['interest'][i-1] - data['repayment'][i-1])
        else:
            data['loan_value'].append(round(data['remaining'][i-2], 2))
            data['interest'].append(round(data['loan_value'][i-1] * interest, 2))
            data['remaining'].append(round((data['loan_value'][i-1] + data['interest'][i-1] - data['repayment'][i-1]), 2))

    df = pd.DataFrame(data)
    df.set_index('year', inplace=True)
    print(df.head(10))
    return df


def calculate_repayment(amount, interest, time):
    if interest != 0:
        repayment = amount * (interest * pow(1 + interest, time)) / (pow(1 + interest, time) - 1)
    else:
        repayment = amount / time
    return repayment


def edit_table(table, interest, new_pay_val, row_from):
    for row in range(0, len(table)):
        if row == row_from:
            table.iloc[row]['repayment'] = new_pay_val
            table.iloc[row]['remaining'] = table.iloc[row]['loan_value'] + table.iloc[row]['interest'] - table.iloc[row]['repayment']
        elif row > row_from:
            table.iloc[row]['loan_value'] = table.iloc[row-1]['remaining']
            table.iloc[row]['interest'] = table.iloc[row]['loan_value'] * interest
            table.iloc[row]['remaining'] = table.iloc[row]['loan_value'] + table.iloc[row]['interest'] - table.iloc[row]['repayment']
    return table


if __name__ == '__main__':
    print('Amortization Table:')
    df1 = create_amortization_table(10000, 0.06, 10)
    print('\nQuestion 2a.')
    print(f'${round(calculate_repayment(10000, 0.06, 10),2)} is the value of the 10 equal payments.\n')
    print('Question 2b.')
    print(f'${round(calculate_repayment(10000, 0, 10))} is the value of the payments,'
          f'if the payment is made at the beginning of the year. \n')
    print('Question 2c.')
    print(f'the value left at the beginning of year six is: ${df1.iloc[6]["loan_value"]}\n')
    print(f'For the end of year six, the amount paying off the remaining principle is: ${df1.iloc[6]["repayment"] - df1.iloc[6]["interest"]}.\n')
    print('Question 2d.')
    df2 = edit_table(df1, 0.06, 2000, 6)
    print(f'the new amortization table looks like: \n')
    print(df2)
    print(f'thus the loan would be paid off in 2.5 years if the end of year payment were to remain the same.')
