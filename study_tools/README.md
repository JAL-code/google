Going to save study notes and other tips for working with Coursera here:

Tips:

1. Run the code for the labs and modify them for your own use.
2. Copy the text of the lectures to a text file before highlighting notes.
3. Take note when text is flashed on the screen and save it. I would save the note at the same time.
4. Write down and note the commands the instructor is using in the video.

Created a program that will parse the text from the lectures into separate files.

See class_highlights_list_lines.py.

How to guide:
1. Open a text file.
2. Note the video title.
  - [Week number]-[Quiz section]-[Item number: video, reading, etc]
  - W1-Q2-01 (for week1 quiz2 section and item 1 in list of videos/readings)
  - Ex., The sectionw will be saved as:  W1-Q2-01-It_Doesnt_Work.txt
4. Enter the following: [* Caption:"Video Title":"order of item in list" *] to create your file header.
  - Ex: [ * Caption : "It Doesn't Work" : 01 * ]
  - No spaces at 'colons' and '[*', '*]'
5. Review the text as you watch the video. 
  - Bracket any text you want to save. 
  - Brackets can be independent for each line.  THe code will join the lines until a bracket pair is created.
  - Try for only one bracket per line or several lines.
6. Repeat steps 1-5 for all videos: See W1-Q2-NO.txt as example input.
7. Create a file named access.py with the folder for your notes.  This file will store your folder for the macro. See line bound by VVVV at top and ^^^ at bottom.
9. Tip: The program can be modified to output the a text file with only the headers and highlights.
  - See PRO_W1-Q2-NO.txt.
10. The program will generate a file for each file header encountered.
  - Ex: W1-Q2-01-It_Doesnt_Work.txt or another other W1-Q2-##-[Video_title].txt.
11. If there are problems with the program, toggle the test constaints at the top of the program.  Including a staged testing scheme for programs in the past has been most crucial in my coding career when debugging the programs due to data errors.
12. End the file wiht the following header (again no spaces except at the title).
  - [ * Caption : "The End" : 07 * ]

```
# this line is only used to pass text to checks
STAGE_ONE_TEST = False      # Test finding closed brackets on one line
STAGE_TWO_TEST = False      # Test finding closed brackets on multilines
STAGE_THREE_TEST = False    # View found highlights and quantify
STAGE_FOUR_TEST = False     # View the headers found
STAGE_FIVE_TEST = False     # Check range of highlights verses orginal file
STAGE_SIX_TEST = True       # Toggle the printing of files to directory.
```
Sample access script:

```
#!/usr/bin/env python3

def get_location_for_code():
    # :releative location
    # access_area = 'files_and_exceptions/'
    access_area = '/home/<user>/<folder>/'
    return access_area
```
Note: run a profile of the program with pprofile3 and kcachegrind.  The file can be any name with a out extension. (.out):
```
$ pprofile3 -f callgrind -o profile_ch_2155_1.out python3 ./class_highlights_list_lines.py
```
View the output:
```
kcachegrind profile_ch_2155_1.out
```
For setup and Terminal example from class:
```

 1788  sudo apt-get update
 1789  sudo apt-get upgrade
 1790  sudo apt autoremove
 1791  sudo apt install python3-pprofile
 1792  pprofile3 -f callgrind -o profile.out python3 ./send_reminders.py "2020-01-13|Example|tests1,test2,test3,test4,test5,test6,test6,test8,test9"
 1793  pprofile3 -f callgrind -o profile.out ./send_reminders.py "2020-01-13|Example|tests1,test2,test3,test4,test5,test6,test6,test8,test9"
 1794  kcachegrind profile.out
 1795  sudo apt install kcachegrind
 1796  kcachegrind profile.out
 1797  pprofile3 -f callgrind -o profile.out ./send_reminders.py "2021-01-13|Example|test1,test2,test3,test4,test5,test6,test6,test8,test9"
 1798  kcachegrind profile.out

```
