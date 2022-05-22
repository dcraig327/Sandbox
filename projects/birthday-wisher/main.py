import base64
import os
import os.path
from email.mime.text import MIMEText

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

EMAIL_ORIGIN = os.getenv('EMAIL_ORIGIN')
EMAIL_DEST = os.getenv('EMAIL_DEST')
EMAIL_SUBJECT = os.getenv('EMAIL_SUBJECT')
EMAIL_MESSAGE = os.getenv('EMAIL_MESSAGE')
EMAIL_USERID = os.getenv('EMAIL_USERID')
print(EMAIL_ORIGIN)
print(EMAIL_DEST)
print(EMAIL_SUBJECT)
print(EMAIL_MESSAGE)
print(EMAIL_USERID)

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']


def gmail_authenticate():
    creds = None
    # the file token.pickle stores the user's access and refresh tokens,
    # and is created automatically when the authorization flow completes for
    # the first time
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # if there are no (valid) credentials availablle, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json',
                                                             SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)


def build_message(origin, destination, subject, body):
    message = MIMEText(body)
    message['to'] = destination
    message['from'] = origin
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}


def send_message(service, origin, destination, subject, body):
    return service.users().messages().send(
        userId="me",
        body=build_message(origin, destination, subject, body)
    ).execute()


gmail_api = gmail_authenticate()
send_message(gmail_api, EMAIL_ORIGIN, EMAIL_DEST, EMAIL_SUBJECT, EMAIL_MESSAGE)
