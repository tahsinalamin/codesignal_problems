"""
You have deposited a specific amount of money into your bank account. Each year your balance increases at the same growth rate. With the assumption that you don't make any additional deposits, find out how long it would take for your balance to pass a specific threshold.

Example

For deposit = 100, rate = 20, and threshold = 170, the output should be
depositProfit(deposit, rate, threshold) = 3.
"""
def depositProfit(deposit, rate, threshold):
    profit=deposit
    year=0
    while profit<threshold:
        profit=profit+(profit*rate)/100
        year=year+1
    return year
        

