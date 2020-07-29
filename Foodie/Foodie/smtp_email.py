import smtplib
import ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"


def send_mail(emailid, email_body, email_subject):
    sender_email = ""  # Enter your address
    receiver_email = emailid  # Enter receiver address
    password = ""
    message = 'Subject: {}\n\n{}'.format(email_subject, email_body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.encode('utf-8'))
