from datetime import datetime, date, time 

today = date.today()
print(today)

tomorrow = date(202, 8 , 19)
print(tomorrow)

next_week = date.fromisoformat("2023-08-26")
print(next_week)


right_now = datetime.now()
print(right_now)

print (right_now.timestamp())

my_date = datetime.fromtimestamp(6516515)
print(my_date)