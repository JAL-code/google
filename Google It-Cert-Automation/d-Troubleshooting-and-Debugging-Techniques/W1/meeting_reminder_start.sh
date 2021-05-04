#!/bin/bash

# steps
# 1 - stage 1/stage 2
# 2 - comment stage 2 and output the meeting_info variable

# stage 1 - get meeting information

meeting_info=$(zenity --forms \
    --title 'Meeting' --text 'Reminder information' \
    --add-calendar 'Date' --add-entry 'Title' \
    --add-entry 'Emails' \
    --forms-date-format='%Y-%m-%d \
    2>/dev/null)

# step 2 - see the output

echo $meeting_info

# stage 2 - pass code to python if output not empty.
: ' 
This code does not work. Last three lines are commited until 
the error line in python script was edited.
'
if [[ -n "$meeting_info" ]]; then
    python3 send_reminders.py "$meeting_info"
fi
