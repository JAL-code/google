#!/usr/bin/env python3
# See the user guide for ReportLab
# https://www.reportlab.com/docs/reportlab-userguide.pdf
# Build a PDF using ReportLab
from reportlab.platypus import SimpleDocTemplate
# if error:
# sudo pip install --upgrade --force-reinstall reportlab
# Start loading the content for the pdf
# Reportlab uses Flowables, chunks of the pdf can arrange
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# Add graphics
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib.units import inch

def setStyles():
    """ Set the stylesheet and table styles. """
    # Setup the report styles
    styles = getSampleStyleSheet()
    table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),
                   ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                   ('ALIGN', (0, 0), (-1, -1), 'CENTER')
    return styles, table_style

def setFileLocation(file_loaction_name):
    """ Set the report location. """
    report = SimpleDocTemplate(file_loaction_name)
    return report

def add_empty_space(width, height)
    """ Add spaces to separate Flowables. """
    empty_line = Spacer(width, height)
    return empty_line

def build_report(file_location_name, report_title, body_text, table_data, get_report_object):
    """ Build the report. """
    styles, table_style = setStyles()
    print("Introduction to Generating PDFs")
    # Create the report object and save it
    report = setFileLocation(file_loaction_name)
    # Build the title:
    report_title = Paragraph(report_title, styles["h1"])
    report_content = Paragraph(body_text, styles["BodyText"])

    print("Adding Tables to our PDFs")
    report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
    gap = add_empty_space(1, 20)
    report.build([report_title, gap, report_title, gap, report_table])
    if get_report_object:
        return report