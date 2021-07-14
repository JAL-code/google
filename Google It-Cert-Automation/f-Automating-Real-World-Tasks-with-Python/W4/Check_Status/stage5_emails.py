#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib

def generate(sender, recipient, subject, body, attachment_path):
    """Creates an email with an attachment."""
    message = email.message.EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    # Add the body to the email
    # body = body_text
    message.set_content(body)

    # Add an attachment path and filename
    attachment_filename = os.path.basename(attachment_path)
    # Get the mime type and subtype
    mime_type, _ = mimetypes.guess_type(attachment_path)
    # split the text to separate MIME type and subtype
    mime_type, mime_subtype = mime_type.split('/', 1)
    # Check the type
    print("Mime:         {}".format(mime_type))
    print("Mime subtype: {}".format(mime_subtype))
    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(),
                           maintype=mime_type,
                           subtype=mime_subtype,
                           filename=attachment_filename)
    return message

def send_it(message):
    # Create the object that will represent our mail server
    # and handle sending messages using a Linux computer.
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
