#!/usr/bin/env python3
import os
from datetime import date, datetime
import reports
from changeImage import get_image_loc
from supplier_image_upload import set_url

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# The following are stages to debug the code
# Check the folder for text files, proceed title
STAGE_ONE = True
# Process the files
STAGE_TWO = True
# Create the pdf body
STAGE_THREE = True
# Save the pdf
TEST_SAVE = True
# View the outputs
VERBOSE = True

def generate_report(attachment, title, paragraph):
    """ Generate the pdf. """
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    title = Paragraph(title, styles["h1"])
    report_info = Paragraph(paragraph, styles["BodyText"])
    empty_line = Spacer(1, 20)
    report.build([title, empty_line, report_info])

# process data from supplier-data/descriptions
if __name__ == "__main__":
    """ Create the pdf. """
    load_fruits = []
    paragraph = ""

    if STAGE_ONE:
        data_loc = get_image_loc('descriptions')
        data = os.listdir(data_loc)
        data.sort()
        today = date.today()
        today_format = today.strftime("%B %d, %Y")
        title = "Processed Update on {}".format(today_format)
        attachment = '/tmp/processed.pdf'
    if VERBOSE:
        print(data)
        print(title)
    for review in data:

        if '.' in review and STAGE_TWO:
            source = "{}/{}".format(data_loc, review)
            print(review.split("."))
            reference = "{}.jpeg".format(review.split(".")[0])
            try:
                file = open("{}/{}".format(data_loc, review), "r")
            except os.error:
                print("File {} can not be opened.".format(review))
            lines = file.readlines()
            if VERBOSE:
                print("Lines:\n {}".format(lines))
                print("Review: {}".format(reference))
            count = 0
            for line in lines:
                lines[count] = line.replace("\n", '')
                count += 1
            temp_dict = dict(name=lines[0].replace("\n", "").capitalize(),
                            weight=lines[1].replace("\n", ""))
            load_fruits.append(temp_dict)
    if VERBOSE:
        print(load_fruits)
    if STAGE_THREE:
        count = 1
        for item in load_fruits:
            """ Create the line for the fruit """
            paragraph += "name: {}\n<br/>".format(item['name'])
            """ Create the line for the weight """
            paragraph += "weight: {}\n<br/>".format(item['weight'])
            """ Create the line return """
            if count < len(load_fruits):
                paragraph += "<br/>"
            count += 1
    if VERBOSE:
        print(paragraph)

    if TEST_SAVE:
        reports.generate_report(attachment, title, paragraph)

