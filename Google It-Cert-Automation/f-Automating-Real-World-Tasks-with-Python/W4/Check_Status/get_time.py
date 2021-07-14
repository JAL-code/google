from datetime import date, datetime

today = date.today()
today_format = today.strftime("%B %d, %Y")
# dateobj = datetime.datetime.strptime(date, r"%Y-%m-%d")
print("Today's date:", today_format)