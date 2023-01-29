import time

current_time = int(time.time())
seconds_in_a_day = 24 * 60 * 60
seconds_in_an_hour = 60 * 60
seconds_in_a_minute = 60

# calculate days since epoch
days = current_time // seconds_in_a_day

# calculate time in a day
hours = (current_time % seconds_in_a_day) // seconds_in_an_hour
minutes = ((current_time % seconds_in_a_day) % seconds_in_an_hour) // seconds_in_a_minute
seconds = ((current_time % seconds_in_a_day) % seconds_in_an_hour) % seconds_in_a_minute

string = "The current time is {0}:{1}:{2} on {3} days after epoch"
print(string.format(hours, minutes, seconds, days))