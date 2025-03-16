import smtplib
"""
This script is used to send emails using the smtplib library.
Modules used:
- smtplib: This module defines an SMTP client session object that can be used to send mail to any internet machine with an SMTP or ESMTP listener daemon.
- email.mime.text.MIMEText: This module is used to create MIME objects of major type text.
- email.mime.multipart.MIMEMultipart: This module is used to create MIME objects of major type multipart, which can contain multiple parts, such as text and attachments.
"""

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 1025
smtp_server = "localhost"
sender_email = "sender@example.com"
receiver_email = "receiver@example.com"

# Create the message
message = MIMEMultipart("alternative")
message["Subject"] = "Test Mail"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain text part
text = """\
    "   This is a test e-mail message.
        "Hope you are doing well.
                "Regards
                "Test   """

html = """\" \" \
    "<html>
        "<body>
            "<p>This is a test e-mail message.</p><br>
            "<p>Hope you are doing well.</p> <br>
                    "<p>Regards</p>" <br>
                    <a href="https://www.youtube.com">Test</a>
                    
                    "<p>Test</p>" 
        "  </body>
    "</html>" 
                        
      """

# turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# connect to the local SMTP server
with smtplib.SMTP(smtp_server, port) as server:
    # send the email
    server.sendmail(sender_email, receiver_email, message.as_string())

    # print a message to confirm that the email has been sent
    print("Mail sent successfully")