#1
monthly_expense = [2200, 2350, 2600, 2130, 2190]
extra_in_feb = monthly_expense[1] - monthly_expense[0]
print('Extra expense in february as compared to januray: ', extra_in_feb)
expense_in_first_quarter = monthly_expense[0] + monthly_expense[1] + monthly_expense[2]
print('Expense in first quarter', expense_in_first_quarter)
print("Did I spend 2000 dollors in any of month? ", 2000 in monthly_expense)
monthly_expense.append(1980)
print(monthly_expense)
monthly_expense[-2] -= 200
print(monthly_expense)

#_______2________
heros=['spider man','thor','hulk','iron man','captain america']
print('Length of the list: ', len(heros))
heros.append('black panther')
print(heros)
heros.remove('black panther')
heros.insert(3, 'black panther')
heros[1:3] = ['doctor strange']
heros.sort()
print(heros)
