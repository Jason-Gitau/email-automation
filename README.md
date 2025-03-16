# Bulk Email Sender - Documentation

## Overview
This script automates sending personalized emails to multiple recipients using Python's built-in `smtplib` and `csv` modules. It reads recipient details from a CSV file and sends customized emails to each one.

## Dependencies
No external libraries are required as the script uses built-in Python modules:
```python
import csv  # For reading the CSV file
import smtplib  # For sending emails
from email.mime.text import MIMEText  # For email formatting
from email.mime.multipart import MIMEMultipart  # For handling multipart emails
```

## Configuration
The script uses the following configurations:
```python
port = 1025  # SMTP server port
SMTP_server = "localhost"  # SMTP server address
sender_email = "sender@example.com"  # Sender's email
receiver_email = "receiver@example.com"  # Default receiver (not used in bulk emails)
```

## Data Input
- The script reads recipient details from a CSV file (`personal_data.csv`).
- Expected CSV format:
  ```csv
  name,email,grade
  John Doe,johndoe@example.com,A
  Jane Smith,janesmith@example.com,B
  ```

## Functionality
1. **Reading Data from CSV**
   ```python
   with open("personal_data.csv") as file:
       reader = csv.reader(file)
       next(reader)  # Skip the header row
   ```
   - Opens and reads `personal_data.csv`.
   - Skips the header row to process only recipient data.

2. **Sending Emails**
   ```python
   for name, email, grade in reader:
       with smtplib.SMTP(SMTP_server, port) as server:
           server.sendmail(sender_email, email, message.format(name=name, grade=grade))
       print(f"Sending email to {name}")
   ```
   - Iterates over each recipient.
   - Sends a personalized email using `smtplib.SMTP.sendmail()`.
   - Prints a confirmation message.

3. **Email Message Format**
   ```python
   message = """
   subject: Your Grade
   
   Dear {name},
   Your grade is {grade}.
   """
   ```
   - Uses a simple text format.
   - Dynamically inserts recipient’s `name` and `grade`.

## Expected Output
The script sends personalized emails to all recipients listed in the CSV file.

### Question: What is the output of the code?
**Correct Answer:**
**A. The code sends personalized emails to the recipients in the CSV file.**

## Issues and Recommendations
1. **SMTP Server Requirement**: Ensure a local or external SMTP server is running on port `1025`.
2. **Email Formatting**: Consider using `MIMEText` for better email structuring.
3. **Security**: Avoid hardcoding sender credentials. Use environment variables instead.
4. **Error Handling**: Implement exception handling to manage connection failures or invalid email addresses.

## Usage
1. **Prepare the CSV File** with recipient names, emails, and grades.
2. **Run the Script**:
   ```sh
   python bulk_email_sender.py
   ```
3. **Monitor the Output** for confirmation messages.

This script provides an efficient way to send bulk personalized emails, ideal for notifications, grading reports, or announcements. 🚀

