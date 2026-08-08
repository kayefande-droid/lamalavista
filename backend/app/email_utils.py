import os
from dotenv import load_dotenv
load_dotenv()
from aiosmtplib import SMTP
from email.message import EmailMessage

SMTP_HOST = os.getenv('SMTP_HOST')
SMTP_PORT = int(os.getenv('SMTP_PORT') or 587)
SMTP_USERNAME = os.getenv('SMTP_USERNAME')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
FROM = SMTP_USERNAME

async def send_email(to_email: str, subject: str, html: str):
    msg = EmailMessage()
    msg['From'] = FROM
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.set_content('Please open HTML email client')
    msg.add_alternative(html, subtype='html')

    smtp = SMTP(hostname=SMTP_HOST, port=SMTP_PORT, start_tls=True)
    await smtp.connect()
    try:
        await smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
        await smtp.send_message(msg)
    finally:
        await smtp.quit()
