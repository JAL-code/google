#!/usr/bin/env python3

import json
import locale
import sys
# Add this text
import emails
import os
import reports

# Leave out this method
def get_temp_location_for_code():
    """ Temporary function to get script location """
    temp_location = __file__
    return os.path.split(temp_location)[0]

# Allows the user to process files at other folders.
dup_folder = get_temp_location_for_code()
user_path = "/data/feedback"

def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  max_revenue = {"revenue": 0}
  max_sales = {"car": 0, "total_sales": 0}
  yearly_sales = {}
  max_year = { "year": 0, "total_sales": 0}
  new_total = 0
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    # TODO: also handle max sales
    if item["total_sales"] > max_sales["total_sales"]:
      # print("New: {}, Old: {}".format(item["total_sales"], max_sales["total_sales"]))
      max_sales["total_sales"] = item["total_sales"]
      max_sales["car"] = format_car(item["car"])
      # print("Car: {}, Total_Sales: {}".format(max_sales["car"], max_sales["total_sales"]))
    # Print the car name:
    # Print(format_car(item["car"]))
    # TODO: also handle most popular car_year
    year_key_item = item["car"]["car_year"]
    year_key_sold = item["total_sales"]
    if year_key_item in yearly_sales:
      """Add to key (year) value additional sold. """
      # print("Key: {}, Total: {}".format(year_key_item, year_key_sold))
      # print("Add to key: {}".format(yearly_sales[year_key_item]))
      new_total = year_key_sold + yearly_sales[year_key_item]
      # print("{} is new total for year_key_sold".format(new_total))
      yearly_sales[year_key_item] = new_total
    else:
      """ Add the key (year) and initial total to yearly_sales """
      yearly_sales[year_key_item] = year_key_sold
    # print(yearly_sales)
      
  for item, (key_item, key_value) in enumerate(yearly_sales.items()):
    # print("Key: {}, Value: {}".format(key_item, key_value))
    if key_value > max_year["total_sales"]:
      max_year["total_sales"] = key_value
      max_year["year"] = key_item
    
  summary1 = [
      "The {} generated the most revenue: ${}".format(
        format_car(max_revenue["car"]), max_revenue["revenue"]),
  ]
  summary2 = [
      "The {} had the most sales: {}".format(
        max_sales["car"], max_sales["total_sales"]),
  ]
  summary3 = [
      "The most popular year was {} with {} sales.".format(
        max_year["year"], max_year["total_sales"]),
  ]
  return summary1, summary2, summary3


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  # get the current directory, not required for lab
  # Allows the user to process files at other folders.
  # ---------------
  dup_folder = get_temp_location_for_code()
  print(dup_folder)

  # keep this line
  data = load_data("{}/car_sales.json".format(dup_folder))
  summary1, summary2, summary3 = process_data(data)
  # print(summary1)
  # print(summary2)
  # print(summary3)
  summary4 = cars_dict_to_table(data)
  # print(summary4)
  
  # TODO: turn this into a PDF report
  print("Preparing summary of data")
  
  report_totals =  "{}\n<br/>{}\n<br/>{}".format(summary1[0], summary2[0], summary3[0])
  reports.generate("/tmp/report_cars.pdf", "Sales summary for last month", report_totals, summary4)

  print("Preparing email")
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Sales summary for last month"
  body = "{}\n {}\n {}".format(summary1[0], summary2[0], summary3[0])

  # TODO: send the PDF report as an email attachment
  message = emails.generate(sender, receiver, subject, body, "/tmp/report_cars.pdf")
  # print(message)
  emails.send(message)

if __name__ == "__main__":
  main(sys.argv)
