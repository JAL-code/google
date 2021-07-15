import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename,'w+') as file:
    pass

  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string

  fulldate=str(datetime.datetime.fromtimestamp(timestamp))
  # Return just the date portion 

  #date=fulldate.date() #
  # Hint: how many characters are in “yyyy-mm-dd”? 

  return ("{}".format(fulldate[:10]))

print(file_date("newfile.txt")) 