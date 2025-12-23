from flask_mail import Message
from app import mail

def send_test_email():
    msg = Message(
        subject="Superheroes API",
        recipients=["your_email@gmail.com"],
        body="API is running successfully!"
    )
    mail.send(msg)
