import datetime as date
x = date.datetime.now()
then = date.datetime.now() + date.timedelta(days=1)

print((then - x).total_seconds())