from email.message import EmailMessage
import smtplib
import ssl
from app.core.config import settings

def smtp_configured() -> bool:
    return bool(settings.smtp_host and settings.smtp_from_email and settings.smtp_username and settings.smtp_password)

def send_customer_email(to_email: str, customer_name: str, subject: str, body: str) -> None:
    if not smtp_configured():
        raise RuntimeError("Email delivery is not configured. Add SMTP settings to your .env file and restart SupportPilot.")
    msg = EmailMessage()
    msg["To"] = to_email
    msg["From"] = f'{settings.smtp_from_name} <{settings.smtp_from_email}>'
    msg["Subject"] = subject
    if settings.smtp_reply_to:
        msg["Reply-To"] = settings.smtp_reply_to
    msg.set_content(body)
    context = ssl.create_default_context()
    if settings.smtp_use_ssl:
        with smtplib.SMTP_SSL(settings.smtp_host, settings.smtp_port, context=context, timeout=20) as server:
            server.login(settings.smtp_username, settings.smtp_password)
            server.send_message(msg)
    else:
        with smtplib.SMTP(settings.smtp_host, settings.smtp_port, timeout=20) as server:
            server.ehlo()
            if settings.smtp_use_tls:
                server.starttls(context=context)
                server.ehlo()
            server.login(settings.smtp_username, settings.smtp_password)
            server.send_message(msg)
