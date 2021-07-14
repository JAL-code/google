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

# Build a dictionary of a fruit collection
fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

print("Introduction to Generating PDFs")
# Create the report object and save it
report = SimpleDocTemplate("/tmp/report.pdf")

# Setup the report styles
styles = getSampleStyleSheet()
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]

# Build the title:
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])

# Check it out
report.build([report_title])

print("Adding Tables to our PDFs")
# Create the report object and save it
report = SimpleDocTemplate("/tmp/report2.pdf")
table_data = []
for k, v in fruit.items():
    table_data.append([k,v])
print(table_data)

report_table = Table(data=table_data)
report.build([report_title, report_table])
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
report.build([report_title, report_table])

print("Adding Graphics to our PDFs")
report = SimpleDocTemplate("/tmp/report3.pdf")
report.build([report_title, report_table])
# Number of pixels per inch.
report_pie = Pie(width=3*inch, height=3*inch)
report_pie.data = []
report_pie.labels = []
for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)

print(report_pie.data)
print(report_pie.labels)

report_chart = Drawing()
report_chart.add(report_pie)
report.build([report_title, report_table, report_chart])