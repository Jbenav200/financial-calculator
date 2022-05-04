def calc_end_of_year_helper(amount, interest, time):
    repayment = amount * (interest * pow(1 + interest, time)) / (pow(1 + interest, time) - 1)
    return repayment
