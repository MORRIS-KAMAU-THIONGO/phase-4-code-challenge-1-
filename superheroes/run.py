from app import create_app, mail
from flask_mail import Message

app = create_app()

with app.app_context():
    try:
        msg = Message(
            subject="Superheroes API",
            recipients=["test@example.com"],
            body="API is running successfully!"
        )
        mail.send(msg)
    except Exception:
        pass

if __name__ == '__main__':
    app.run(debug=True)
