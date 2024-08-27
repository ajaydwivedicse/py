#1
street = 'North Malaka'
city = 'Prayagraj'
country = 'India'
address = street + '\n' + city + '\n' + country
print(address)
#using f-string
print(f'{street}\n{city}\n{country}')

#2
statement = 'Earth revolves around the sun'
print(statement[6:14])
print(statement[-3:])

#3
x = 5
y = 6
print(f'I eat {x} veggies and {y} fruits daily')

#4
s = "maine 200 banana khaye"
s = s.replace('banana', 'samosa').replace('200', '100')
print(s)