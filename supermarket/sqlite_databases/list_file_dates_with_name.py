import os
import csv
import time

def list_file_dates(directory, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["File", "Creation Date", "Modified Date", "Accessed Date"])  #Folder
        
        for root, dirs, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                creation_time = os.path.getctime(filepath)
                modified_time = os.path.getmtime(filepath)
                accessed_time = os.path.getatime(filepath)
                creation_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(creation_time))
                modified_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(modified_time))
                accessed_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(accessed_time))
                writer.writerow([filename, creation_date, modified_date, accessed_date])

# Provide the directory path here
directory_path = "C://Users//Joseph//Documents//BS_Back_UP"
output_file = "file_dates.csv"
list_file_dates(directory_path, output_file)


