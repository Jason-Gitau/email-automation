# sending multiple personalized emails using the smtplib library.
# Modules used:
# - smtplib: This module defines an SMTP client session object that can be used to send mail to any internet machine with an SMTP or ESMTP listener daemon.
# - email.mime.text.MIMEText: This module is used to create MIME objects of major type text.
# - email.mime.multipart.MIMEMultipart: This module is used to create MIME objects of major type multipart, which can contain multiple parts, such as text and attachments.
# """
#

# make a csv file with the relevant  personal data
# import the necessary modules
import csv


 # import the necessary modules to send the email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# set the port number and the SMTP server
port = 1025 # set the port number
smtp_server = "localhost" # set the smtp server
sender_email = "sender@example.com" # set the sender email
receiver_email = "receiver@example.com" # set the receiver email

# Create the message
message = """\
    "Subject: your grade

        "Dear {name},
        "Your grade is {grade}.
            "   """



# loop through the csv file and send personalized emails
with open('personal_data.csv') as file: # open the csv file   to read the file and close it after reading it   
    reader = csv.reader(file) # read the file

    next(reader)  # skip the header row of the file

    # loop through the file
    for name, email, grade in reader:

        # connect to the local SMTP server
        with smtplib.SMTP(smtp_server, port) as server:
            # send the email
            server.sendmail(sender_email, email, message.format(name=name, grade=grade)) # send the email


        print(f"Sending email to {name}") # print the name of the person we are sending the email to

''
        

