# 1. We have following information on countries and their population (population is in crores),
#
# Country	Population
# China	143
# India	136
# USA	32
# Pakistan	21
# Using above create a dictionary of countries and its population
# Write a program that asks user for three type of inputs,
# print: if user enter print then it should print all countries with their population in this format,
# china==>143
# india==>136
# usa==>32
# pakistan==>21
# add: if user input add then it should further ask for a country name to add. If country already exist in
# our dataset then it should print that it exist and do nothing.
# If it doesn't then it asks for population and add that new country/population in our dictionary and print it
# remove: when user inputs remove it should ask for a country to remove. If country exist in
# our dictionary then remove it and print new dictionary using format shown above in (a).
# Else print that country doesn't exist!
# query: on this again ask user for which country he or she wants to query.
# When user inputs that country it will print population of that country.
# You are given following list of stocks and their prices in last 3 days,
#
# 2. Stock	Prices
# info	[600,630,620]
# ril	[1430,1490,1567]
# mtl	[234,180,160]
# Write a program that asks user for operation. Value of operations could be,
# print: When user enters print it should print following,
# info ==> [600, 630, 620] ==> avg:  616.67
# ril ==> [1430, 1490, 1567] ==> avg:  1495.67
# mtl ==> [234, 180, 160] ==> avg:  191.33
# add: When user enters 'add', it asks for stock ticker and price.
# If stock already exist in your list (like info, ril etc) then it will append the price to the list.
# Otherwise it will create new entry in your dictionary.
# For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.
# 3. Write circle_calc() function that takes radius of a circle as an input from user and then
#     it calculates and returns area, circumference and diameter.
#     You should get these values in your main program by calling circle_calc function and then print them.

import statistics
import math


def print_query():
    for country, population in countries.items():
        print(f"{country}==>{population}")


def add_query():
    country_name = input('Enter the country name: ')
    country_name = country_name.lower()
    if country_name in countries:
        print('Country name is already present!!!')
        return
    population = float(input(f'Enter the population for {country_name}: '))
    countries[country_name] = population
    print_query()


def remove_query():
    country_name = input('Enter the country name you want to remove: ')
    country_name = country_name.lower()
    if country_name not in countries:
        print('Country name is not present!!!')
        return
    del countries[country_name]
    print_query()


def query_query():
    country_name = input('Enter the country name which you want to query: ')
    country_name = country_name.lower()
    if country_name not in countries:
        print('Country name is not present!!!')
        return
    print(f'Population of {country_name} is: {countries[country_name]} crore')


def print_stock():
    for stock, price in stocks.items():
        avg = statistics.mean(price)
        print(f'{stock} ==> {price} ==> avg: ', round(avg, 2))


def add_stock():
    stock = input('Enter the stock ticker: ')
    price = float(input("Enter the price: "))
    if stock in stocks:
        stocks[stock].append(price)
        print_stock()
        return
    stocks[stock] = [price]
    #   stocks[stock].append(price)
    print_stock()


def circle_calc():
    radius = float(input('Enter the radius of circle: '))
    area = round(math.pi * radius ** 2, 2)
    circumference = round(2 * math.pi * radius, 2)
    diameter = round(2 * radius, 2)

    return area, circumference, diameter


def main():
    inp = input("Enter operation (add, remove, query or print): ")
    inp = inp.lower()

    if inp == 'print':
        print_query()
    elif inp == 'add':
        add_query()
    elif inp == 'remove':
        remove_query()
    elif inp == 'query':
        query_query()


def main_two():
    inp = input("Enter operation (add or print): ")
    inp = inp.lower()
    if inp == 'print':
        print_stock()
    elif inp == 'add':
        add_stock()


def main_three():
    area, circumference, diameter = circle_calc()
    print(f'Area: {area} Circumference: {circumference}, Diameter: {diameter}')


countries = {
    'china': 143,
    'india': 136,
    'usa': 32,
    'pakistan': 21
}

stocks = {
    'info': [600, 630, 620],
    'ril': [1430, 1490, 1567],
    'mtl': [234, 180, 160]
}

if __name__ == '__main__':
    # main()
    # main_two()
    main_three()
