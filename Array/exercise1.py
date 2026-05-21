# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

# Monthly expenses list
expenses = [2200, 2350, 2600, 2130, 2190]

# 1. Extra money spent in February compared to January
extra_spent = expenses[1] - expenses[0]
print("1. Extra spent in February compared to January:", extra_spent)

# 2. Total expense in first quarter (January + February + March)
first_quarter_total = expenses[0] + expenses[1] + expenses[2]
print("2. Total expense in first quarter:", first_quarter_total)

# 3. Check if exactly 2000 dollars were spent in any month
print("3. Did you spend exactly 2000 dollars in any month?")
print(2000 in expenses)

# 4. Add June expense
expenses.append(1980)
print("4. Expenses after adding June:", expenses)

# 5. April refund of 200 dollars
expenses[3] = expenses[3] - 200
print("5. Expenses after April refund correction:", expenses)