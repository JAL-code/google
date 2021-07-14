#!/usr/bin/env python3
# Use pythons Email module and EmailMessage method to send email.
# https://docs.python.org/3/library/email.html
# https://docs.python.org/3/library/email.message.html
from email.message import EmailMessage
import os.path
# tell the recipient what you are sending.
# See the Internet Assigned Numbers Authority (IANA) (iana.org)
# Multipurpose Internet Mail Extensions (MIME)
# https://tools.ietf.org/html/rfc2045
import mimetypes
# Simple Mail Transfer Protocol (SMTP)
# Specify how the email will be delivered.
# https://datatracker.ietf.org/doc/html/rfc2821.html
import smtplib
# authenticate to the SMTP server
# https://docs.python.org/3/library/getpass.html
import getpass

def setup_the_message(sender, recipient, subject, body_text, attachment_path):
    message = EmailMessage()
    # Add sender and recipient fields
    # Change the email addresses to match
    # Add From and To fields
    message['From'] = sender
    message['To'] = recipient
    # Add a subject:
    message['Subject'] = subject
    # Add the body to the email
    body = body_text
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
                           filename=os.path.basename(attachment_path))
    return message

def send_it(message):
    # Create the object that will represent our mail server
    # and handle sending messages using a Linux computer.
    try:
        # Use a configured SMTP server like postfix or sendmail
        mail_server = smtplib.SMTP('localhost')
    except ConnectionRefusedError:
        # No local SMTP server configured!
        # Search for local service and "SMTP connection settings"

        # So connect using Transport Layer Security (TLS).
        # earlier version: Secure Sockets Layer (SSL)
        # SSL/TLS protocol adds a secure transmission layer to HTTP, making it HTTPS.
        # Use a secure transport layer by accessing the smtplib module
        # https://docs.python.org/3/library/smtplib.html#smtplib.SMTP
        # SMTP_SSL class will make a SMTP connection over SSL/TLS
        # https://docs.python.org/3/library/smtplib.html#smtplib.SMTP_SSL
        mail_server = smtplib.SMTP_SSL('smtp.example.com')
        mail_server.set_debuglevel(1)

        # Get the password without showing it.
        mail_pass = getpass.getpass('Password? ')

    # With email user/password, authenticate to the email server
    # https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.login
    try:
        mail_server.login(sender, mail_pass)
        # Login method returns a tuple of SMTP status code
        # # https://datatracker.ietf.org/doc/html/rfc4954#section-6
        # 235, '2.7.0 Accepted' Authentication Succeeded
        # If unsuccessful print the error.
    except SMTPAuthenticationError:
        print("Check setup: {}".format(SMTPauthticationError))
        # Send the message (send_message)
        # https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.send_message
    mail_server.send_message(message)
    # If successful the send message method will return an empty dictionary.
    # Of emails unable to recieve to message.
    mail_server.quit()

