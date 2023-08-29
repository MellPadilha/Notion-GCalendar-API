from __future__ import print_function

import datetime
from datetime import timedelta
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/calendar']

# AUTH
def main():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('Credenciais/credentials.json', SCOPES)
            creds = flow.run_local_server(port = 0)            
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
                
        timeMin = datetime.datetime.utcnow()
        timeMin = timeMin - timedelta(weeks = 1)
        timeMin = timeMin.isoformat() + 'Z'     

        events = service.events().list(calendarId='mellanie.padilha@gmail.com', 
                                        timeMin=timeMin, 
                                        singleEvents=True,
                                        orderBy='startTime').execute()
        for event in events['items']:
            if event['status'] == 'confirmed':
                start = event['start'].get('dateTime', event['start'].get('date'))
                print (f'Evento:{start}::{event["summary"]} \n')
                print (event)


    except HttpError as error:
        print("Vai de novo", error)


if __name__ == '__main__':
    main()