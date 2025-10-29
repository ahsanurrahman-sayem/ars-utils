from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from ars import mail
from getpass import getpass
SCOPES = ['https://mail.google.com/']

flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
creds = flow.run_local_server(port=0)

token = creds.token  # OAuth2 access token
email = mail.Email(sender_email="ahsanurrahman1.sayem10000@gmail.com", password=getpass("Enter pasword (Not shown): "))
email.setRecipient("skgroup10000@gamil.com")
email.setSubject("OAuth2 Test")
email.setContent("Hey buddy! This is a secure OAuth2-based email.")
email.send()