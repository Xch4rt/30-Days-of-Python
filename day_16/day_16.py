#Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime, time, date

now = datetime.now()
time = now.strftime("%d/%m/%Y, %H:%M:%S")
print(time)


#Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
time1 = now.strftime("%m/%d/%Y, %H:%M:%S")
print(time1)
#Today is 5 December, 2019. Change this time string to time.
dat = "5 December, 2019"
print(datetime.strptime(dat, "%d %B, %Y"))
#Calculate the time difference between now and new year.
dat1 = date(year = 2021,month=10,day=5)
dat2 = date(year = 2018,month=2,day=20)
print(dat1 - dat2)
#Calculate the time difference between 1 January 1970 and now.
datJ = date(year=1970, month = 1, day=1)
datNow = date(year=2021, month=10, day=5)
print(datNow - datJ)
