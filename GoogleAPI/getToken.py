from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os.path

SCOPES= ["https://www.googleapis.com/auth/calendar"]

def getToken():
    
    flow = InstalledAppFlow.from_client_secrets_file("../Credenciais/credentials.json", scopes=SCOPES)
    flow.run_local_server()
    pickle.dump(flow.credentials, open("../Credenciais/token.pkl", "wb"))

    return pickle.load(open("../Credenciais/token.pkl", "rb"))

def Autentication():

    creds = None

    if os.path.exists('../Credenciais/token.pkl'):
        creds = pickle.load(open("../Credenciais/token.pkl", "rb"))

    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else: 
            getToken()
    
    return creds
