import smtplib
import email.message


def send(sender, to, subject="None", body="None", server="localhost"):
    """sends a message."""
    message = email.message.Message()
    message["To"] = to
    message["From"] = sender
    message["Subject"] = subject
    message.set_payload(body)

    client = smtplib.SMTP(server)
    try:
        return client.sendmail(sender, to, message.as_string())
    finally:
        client.quit()
