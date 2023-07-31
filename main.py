import base64

from google.oauth2 import service_account
from googleapiclient.discovery import build
from email.message import EmailMessage

creds = service_account.Credentials.from_service_account_file("coffee-roulette-394514-45407839cfa3.json")
delegated_creds = creds.with_subject('webmaster@cissa.org.au')
scoped_creds = delegated_creds.with_scopes(['https://www.googleapis.com/auth/gmail.send'])

service = build('gmail', 'v1', credentials=scoped_creds)
message = EmailMessage()
message['To'] = '857514.leofeng@gmail.com'
message['From'] = 'webmaster@cissa.org.au'
message['Subject'] = 'Test2'
message.set_content('Test1234')
encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
service.users().messages().send(userId='me', body={'raw': encoded_message}).execute()