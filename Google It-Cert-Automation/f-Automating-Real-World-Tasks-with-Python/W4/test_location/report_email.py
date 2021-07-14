#!/usr/bin/env python3

import sys
# Add this text
import emails
import os
import reports

def main(argv):
  print("Preparing email")
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

  # TODO: send the PDF report as an email attachment
  message = emails.generate(sender, receiver, subject, body, "/tmp/report_cars.pdf")
  # print(message)
  emails.send(message)

if __name__ == "__main__":
  main(sys.argv)

