from app import create_app
from app.mail import send_test_email

app = create_app()

with app.app_context():
    try:
        send_test_email()
    except Exception:
        pass

if __name__ == '__main__':
    app.run(debug=True)
