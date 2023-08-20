from google_auth_oauthlib.flow import InstalledAppFlow
import pickle

def getToken():
    scopes = ["https://www.googleapis.com/auth/calendar"]
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
    flow.run_local_server()
    pickle.dump(flow.credentials, open("token.pkl", "wb"))

    return pickle.load(open("token.pkl", "rb"))

