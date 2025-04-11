from datetime import datetime

now = datetime.now()
print("unformatted datetime:" ,now)
formatted_date = now.strftime("%Y/%m/%d %H:%M:%S ")
print("Formatted datetime:", formatted_date)

dtstr = "2023/10/01 12:38:00"
dt = datetime.strptime(dtstr, "%Y/%m/%d %H:%M:%S")
print(dt)

print(datetime.weekday)