#Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime

now = datetime.now()
time = now.strftime("%d/%m/%Y, %H:%M:%S")
print(time)


#Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
time1 = now.strftime("%m/%d/%Y, %H:%M:%S")
print(time1)
#Today is 5 December, 2019. Change this time string to time.

#Calculate the time difference between now and new year.


#Calculate the time difference between 1 January 1970 and now.


'''
Think, what can you use the datetime module for? Examples:

    Time series analysis
    To get a timestamp of any activities in an application
    Adding posts on a blog

'''