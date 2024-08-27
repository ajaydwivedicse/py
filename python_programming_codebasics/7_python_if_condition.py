# 1. Using following list of cities per country,
# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]
# Write a program that asks user to enter a city name and it should tell which country the city
# belongs to
# Write a program that asks user to enter two cities and it tells you if they both are in same
# country or not. For example if I enter mumbai and chennai, it will
# print "Both cities are in India" but if I enter mumbai and dhaka it should
# # print "They don't belong to same country"

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
city_name = input("Give the city name: ")
if city_name in india:
    print(f'{city_name} is in India')
elif city_name in pakistan:
    print(f'{city_name} is in Pakistan')
elif city_name in bangladesh:
    print(f'{city_name} is in Bangladesh')
else:
    print(f'I\'ve no idea from which country {city_name} belongs' )

city1 = input("Give the name of city 1: ")
city2 = input("Give the name of city 2: ")
if city1 in india and city2 in india:
    print('Both cities are in India')
elif city1 in pakistan and city2 in pakistan:
    print('Both cities are in Pakistan')
elif city1 in bangladesh and city2 in bangladesh:
    print('Both cities are in Bangladesh')
else:
    print('They don\'t belong to same country')

# 2.Write a python program that can tell you if your sugar is normal or not.
# Normal fasting level sugar range is 80 to 100.
# (i) Ask user to enter his fasting sugar level
# (ii) If it is below 80 to 100 range then print that sugar is low
# (iii) If it is above 100 then print that it is high otherwise print that it is normal
sugar_level = float(input("Enter the Sugar level: "))
if sugar_level < 80:
    print("Sugar is low, go and eat some sweets :) ")
elif sugar_level > 100:
    print("Sugar is high, stop eating all the sweet items!...")
else:
    print("Sugar is normal, go and enjoy your life.")