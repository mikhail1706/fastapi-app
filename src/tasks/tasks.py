import smtplib
from email.message import EmailMessage

from celery import Celery

# from config import SMTP_USER, SMTP_PASSWORD
from config import REDIS_HOST, REDIS_PORT

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

celery_app = Celery(
    "tasks",
    broker=f"redis://{REDIS_HOST}:{REDIS_PORT}",
    broker_connection_retry_on_startup=True,
)


def get_email_template_dashboard(username: str):
    email = EmailMessage()
    email["Subject"] = "My first subject"
    email["From"] = "mgumenm@gmail.com"
    email["To"] = "mgumenm@gmail.com"

    email.set_content(
        "<div>" "<h1>This is my email </h1>" "</div>", subtype="html"
    )

    return email


@celery_app.task
def send_email_report_dashboard(username: str):
    email = get_email_template_dashboard(username)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login("username", "password")
        server.send_message(email)
