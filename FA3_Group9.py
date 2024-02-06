#Practice using the Python interpreter as a calculator:

#1. The volume of a sphere with radius r is 4/3pir^3. What is the volume of a sphere with radius 5?

radius = int(input('Enter the radius of the sphere >> ')) #Takes the input from the user of the radius.
pi = 3.14

volume = 4/3 * pi * radius ** 3 #Calculates the volume

print('The volume of a sphere with a radius of', radius, 'is', volume,'.')

#2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?

quantity = int(input('Enter the amount of copies >> ')) #Gets input from user of how many copies should be sold.
bookstore_discount = 0.4
price = 24.95

#Calculates the shipping cost, as well as the total price and discounted price of the copies.
shipping = 3 + 0.75 * (quantity - 1)
total_price = price * quantity
discounted_price = total_price * bookstore_discount

wholesale_price = discounted_price - shipping

#Displays the output of the calculations
print('The total cost is $', wholesale_price,'including the shipping fee')
print('The wholesale price of the copies is $', total_price,', with the discount, it amounts to $', discounted_price)

#3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at an easy pace again, what time do I get home for breakfast?

easy_pace = 8.25
tempo_pace = 7.2

first_run = easy_pace * 1
second_run = tempo_pace * 3
last_run = easy_pace * 1

total_time_run = first_run + second_run + last_run

print('The total minutes ran is', total_time_run,'minutes. Which is equivalent to 38 minutes and 6 seconds')
print('Adding 38 minutes and 6 seconds to the starting time, the time to get home for breakfast is 7:30')

