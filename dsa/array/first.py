# this is first question

spent = [2200, 2350, 2600, 2130, 2190]
# 1
print(spent[1] - spent[0])

# 2
first_quarter = spent[0] + spent[1] + spent[2]
print(first_quarter)
# 3
spent.append(2000)
print("monthly expense is exactly 2000 in any of the given months: ", 2000 in spent)
spent.pop()

# 4
spent.append(1980)
for i in spent:
    print(i)

# 5
spent[3] -= 200
print("In the month of april we spent: ", spent[3])
