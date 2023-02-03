from exchangelib import DELEGATE, Account, Credentials, Configuration

usrn = input("Username:...")
pswd = input("Password:...")
username = usrn
password = pswd
Credentials = Credentials(usrn, pswd)

config = Configuration(server='SMTP.landmark.co.uk', credentials=Credentials)

Account = Account(
    primary_smtp_address=usrn,
    credentials=Credentials,
    autodiscover=False,
    config=config,
    access_type=DELEGATE,
)

print(Account)
