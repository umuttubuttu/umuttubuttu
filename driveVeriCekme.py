import os
import io
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
else:
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

service = build('drive', 'v3', credentials=creds)
# tokeni file id'ye yerleştirin
# Örnek:https://drive.google.com/file/d/XXXX/view ise şu şekide XXXX 
file_id = '1CTqBr5kzGYPag-_Qo6qhh6rEB0-i9Ws'
request = service.files().get_media(fileId=file_id)

fh = io.BytesIO()
downloader = MediaIoBaseDownload(fh, request)
done = False
while done is False:
    status, done = downloader.next_chunk()
    print(f'Download {int(status.progress() * 100)}%.')

fh.seek(0)
with open('downloaded_file', 'wb') as f:
    f.write(fh.read())
