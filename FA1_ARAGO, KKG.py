#Start the Python interpreter and use it as a calculator.
#Exercises 1-2

#Calculates how many seconds there are in 42 minutes and 42 seconds.
def calculate_seconds(minute, second):
    minutes_to_seconds = minute * 60
    total_seconds = minutes_to_seconds + second

    return total_seconds

final_seconds = calculate_seconds(42, 42)
print('There is a total of', final_seconds, 'seconds')

#Determines how many miles there are in 10 kilometers.
def converts_kilometer_to_miles(kilometer):
    miles_per_kilometer = 0.621371
    converted_miles = kilometer * miles_per_kilometer

    return converted_miles

final_miles = converts_kilometer_to_miles(10)
print('10 kilometers is equal to', final_miles, 'miles')

#Determines the average speed in miles per hour, minutes and seconds.

#Converts minutes and seconds to hours.
def conversion_to_hour(hour, minutes, seconds):
    seconds_to_minutes = seconds/60
    minutes_and_seconds = minutes + seconds_to_minutes
    minutes_to_hour = minutes_and_seconds/60
    total_time_hours = minutes_to_hour + hour

    return total_time_hours

#Converts hours and seconds to minutes.
def conversion_to_minutes(hour, minutes, seconds):
    seconds_to_minutes = seconds/60
    hours_to_minutes = hour * 60
    total_time_minutes = hours_to_minutes + seconds_to_minutes + minutes

    return total_time_minutes

#Converts hours and minutes to seconds.
def conversion_to_seconds(hour, minutes, seconds):
    hour_to_seconds = hour * 60 * 60
    minutes_to_seconds =  minutes * 60
    total_time_seconds = seconds + hour_to_seconds + minutes_to_seconds

    return total_time_seconds

time_in_hours = conversion_to_hour(0, 42, 42)
print('There is a total of', time_in_hours, 'hours in 42 minutes and 42 seconds')

average_miles_per_hour = 10 / time_in_hours
print('The average miles per hour is', average_miles_per_hour, 'mph')

time_in_minutes = conversion_to_minutes(0, 42, 42)
print('There is a total of', time_in_minutes, 'minutes in 42 minutes and 42 seconds')

average_pace_per_minute = 10 / time_in_minutes
print('The average pace per minute is', average_pace_per_minute)

time_in_seconds = conversion_to_seconds(0, 42, 42)
print('There is a total of', time_in_seconds,'seconds in 42 minutes and 42 seconds')

average_pace_per_second = 10 / time_in_seconds
print('The average pace per second is', average_pace_per_second)




