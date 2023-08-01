from mailing import authenticate_mail, send_mail
from matching import find

SERVICE_FILE_PATH = "coffee-roulette-394514-45407839cfa3.json"

# authenticate_mail(SERVICE_FILE_PATH)
# send_mail("857514.leofeng@gmail.com", "Another test", "This is a test.")

for i in range(10):
    print(find())
