from googleapiclient.discovery import build
import datetime
from datetime import timedelta
import json

class _Event:

    # Usadas por enquanto
    name= None
    start= None
    end= None
    eventID= None
    link= None

    """
    # Não usadas 
    created= None
    updated= None
    creator= None
    organizer= None
    recurringEventId= None
    iCalUID= None
    eventType= None

    # Especialmente inutil
    eventType= None
    sequence= None
    """
    

    def __init__(self, event):
        """
        _summary_

        A mellaniue não sabe documentar, vai ficar assim até ela aprender

        Check the google calendar API documentation.

        Args: 
        event (dict): Event structure.

        """
        

        # Dados que estou usando agora
        self.name = event['summary']
        self.start = event['start']['dateTime']
        self.end = event['end']['dateTime']
        self.eventID = event['id']
        self.link = event['htmlLink']

        """
        Most comunment used data, but we not use in this project

        self.created= event['created']
        self.updated= event['updated']
        self.creator= event['creator']['email']
        self.organizer= event['organizer']['email']
        self.recurringEventId= event['recurringEventId']
        self.iCalUID= event['iCalUID']
        self.eventType= event['eventType']

        #################################################################

        IDK, how u can use this, but how to get this is here:

        self.eventType = event['eventType']
        self.sequence = event['sequence']

        """

        pass


class Calendar:

    # Estou com preguiça agora, mas não esquece de tipar isso se o pŕojeto crescer isso é fonte de bug
    events = []
    #updated: None

    def __init__(self, timeMin, creds, calendarId = 'primary', singleEvents = True, orderBy='startTime'):
        """_summary_
        A mellaniue não sabe documentar, vai ficar assim até ela aprender

        Check the google calendar API documentation.

        Args:
            timeMin (dateTime): Take the date and search from this date.
            creds (google.oauth2.credentials.Credentialsa): Google credentials use Autentication() or getToken().
            calendarId (str, optional): Calendar Id, if you need the primary calendar you can pass the e-mail or just 'primary'. Defaults to 'primary'.
            singleEvents (bool, optional): Check the google calendar API documentation. Defaults to True.
            orderBy (str, optional): Check the google calendar API documentation. Defaults to 'startTime'.
        """

        try:           
            service = build('calendar', 'v3', credentials=creds)
            request = service.events().list(calendarId=calendarId, timeMin=timeMin, singleEvents=singleEvents, orderBy=orderBy).execute()
            

            for item in request['items']:
                if item['status'] == 'confirmed':
                    event = _Event(item)
                    self.events.append(event)
                    print(event)
        
        except Exception as e:
            print(e)


    def createJsonFile(self, path = ''):
        json_object = json.dumps(self.formatAsJson(), indent = 4)

        with open(f'{path}events.json', 'w') as file:
            file.write(json_object)


    def formatAsJson(self):
        dict = []

        for event in self.events:
            aux = {
                "name": event.name,
                "startDate": event.start,
                "endDate": event.end,
                "eventId": event.eventID,
                "link": event.link
            }
            dict.append(aux)

        data = {'data:' : dict}

        return data