# After flipping a coin 10 times you got this result,
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# Using for loop figure out how many times you got heads
#
# Print square of all numbers between 1 to 10 except even numbers
# Your monthly expense list (from Jan to May) looks like this,
# expense_list = [2340, 2500, 2100, 3100, 2980]
# Write a program that asks you to enter an expense amount and program should tell
# you in which month that expense occurred. If expense is not found then it should print that as well.
#
# Lets say you are running a 5 km race. Write a program that,
#
# Upon completing each 1 km asks you "are you tired?"
# If you reply "yes" then it should break and print "you didn't finish the race"
# If you reply "no" then it should continue and ask "are you tired" on every km
# If you finish all 5 km then it should print congratulations message
# Write a program that prints following shape
#
# *
# **
# ***
# ****
# *****

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count = 0
for i in result:
    if i == 'heads':
        count += 1
print('No. of \'heads\' found:  ', count)
print('Square of all numbers between 1 to 10 except even numbers... ')
# print(list(range(1, 10, 2)))
for i in range(1, 10, 2):
    print(i)
expense_list = [2340, 2500, 2100, 3100, 2980]
month_list = ['jan', 'feb', 'march', 'april', 'may']
expense = int(input('Enter the expense: '))
for i in range(len(expense_list)):
    if expense == expense_list[i]:
        print(f'Expense of {expense} was found in {month_list[i]}')
        break
    else:
        print(f'Expense of {expense} was not found in {month_list[i]}')
km = 0
for i in range(5):
    print(f'you ran {i + 1} miles')
    msg = input('are you tired? ')
    if msg == 'yes':
        print(f"you didn't finish the race but anyways, you still ran {i + 1} miles")
        break
    elif i == 4:
        print('Congratulations!!!, you have finished the race')
    elif msg == 'no':
        continue

# for i in range(5):
#     for j in range(i):
#         print('*', end = '')
#     print('\n')

for i in range(5):
    s = ''
    for j in range(i):
        s += '*'
    print(s)







