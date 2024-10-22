import smtplib, ssl
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "hellokinkoa@gmail.com"
    password = os.getenv("PASSWORD")

    # Check if the password is available
    if password is None:
        print("ERROR: Password not found in environment variables.")
        return

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, username, message)  # Sending to self for testing
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Define the email message (for testing)
email_message = """\
Subject: Hi!

How are you?
Bye!
"""

# Call the function with the email message (for testing)
send_email(email_message)
