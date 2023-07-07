from datetime import datetime, timedelta

current_time=datetime.now()
print("current time: ",current_time)

formatted_time=current_time.strftime("%Y-%m-%d %H:%M:%S")
print("formatted time: ",formatted_time)

day_before=current_time-timedelta(days=1)
print("a day before: ",day_before)