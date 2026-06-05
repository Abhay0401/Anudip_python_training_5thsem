# Customer ke transactions ki list
transactions = [5000, -2000, 3000, -1000, -500, 7000]

# Current balance calculate karne ke liye variable
balance = 0

# Deposits aur withdrawals ko alag store karne ke liye lists
deposits = []
withdrawals = []

# Har transaction par loop chalega
for transaction in transactions:

    # Current balance me transaction add kar do
    balance += transaction

    # Agar value positive hai to deposit hai
    if transaction > 0:
        deposits.append(transaction)

    # Agar value negative hai to withdrawal hai
    elif transaction < 0:
        withdrawals.append(transaction)

# Sabse bada deposit maan lo pehla deposit
largest_deposit = deposits[0]

# Deposits list me sabse bada deposit dhundo
for deposit in deposits:
    if deposit > largest_deposit:
        largest_deposit = deposit

# Sabse bada withdrawal maan lo pehla withdrawal
largest_withdrawal = withdrawals[0]

# Withdrawals list me sabse bada withdrawal dhundo
for withdrawal in withdrawals:
    if withdrawal < largest_withdrawal:
        largest_withdrawal = withdrawal

# Results print karo
print("Current Balance:", balance)
print("Deposits:", deposits)
print("Withdrawals:", withdrawals)
print("Largest Deposit:", largest_deposit)
print("Largest Withdrawal:", largest_withdrawal)
