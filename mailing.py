import base64

from google.oauth2 import service_account
from googleapiclient.discovery import build
from email.message import EmailMessage

scoped_creds = None


def authenticate_mail(service_file_path):
    global scoped_creds
    creds = service_account.Credentials.from_service_account_file(service_file_path)
    delegated_creds = creds.with_subject('webmaster@cissa.org.au')
    scoped_creds = delegated_creds.with_scopes(['https://www.googleapis.com/auth/gmail.send'])


def send_mail(to, subject, content):
    service = build('gmail', 'v1', credentials=scoped_creds)
    message = EmailMessage()
    message['To'] = to
    message['From'] = 'webmaster@cissa.org.au'
    message['Subject'] = subject
    message.set_content(content)
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    service.users().messages().send(userId='me', body={'raw': encoded_message}).execute()