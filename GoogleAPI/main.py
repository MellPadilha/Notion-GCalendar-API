from __future__ import print_function

import datetime
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
            flow = InstalledAppFlow.from_client_secrets_file('GoogleAPI/credentials.json', SCOPES)
            creds = flow.run_local_server(port = 0)            
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
        

        # events = service.events().get(calendarId='primary').execute()
        calendar_list = service.calendarList().list().execute()
        # print(calendar_list['items'])       
        
        timeMin = '2023-08-14T10:00:00Z'
        
        page_token = None
        while True:
            events = service.events().list(calendarId='mellanie.padilha@gmail.com', pageToken=page_token, timeMin=timeMin).execute()
            for event in events['items']:
                # print(event)
                if event['status'] == 'confirmed':
                    print (f'Evento:{event["summary"]} \n')
            page_token = events.get('nextPageToken')
            if not page_token:
                break

    except HttpError as error:
        print("Vai de novo", error)


if __name__ == '__main__':
    main()