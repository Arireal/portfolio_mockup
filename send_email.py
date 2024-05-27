import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "hellokinkoa@gmail.com"
    password = "hhfghgdnxlcjyjkp"  # It's not secure to hardcode passwords in your code
    receiver = "hellokinkoa@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


# Define the email message
email_message = """\
Subject: Hi!

How are you?
Bye!
"""

# Call the function with the email message
send_email(email_message)
