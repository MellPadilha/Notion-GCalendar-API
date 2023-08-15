from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

# Antes de ver isso lembra de criar o projeto no Gcloud, criar o OAuth
# e salvar o arquivo de credenciais.json para poder fazer a autenticação
# Ainda tem que instalar a lib do cliente do google:
# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

# AUTH
def main():
    cred: None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port = 0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("calendar", "v3", credentials = creds)
        page_token = None
        while True:
            events = service.events().list(calendarId='primary', pageToken=page_token).execute()
            for event in events['items']:
                # print(event['summary'])
                print(event)
            page_token = events.get('nextPageToken')
            if not page_token:
                break
    except HttpError as error:
        print("Vai de novo", error)


if __name__ == '__main__':
    main()