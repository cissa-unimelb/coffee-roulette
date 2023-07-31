# coffee-roulette

Automated friend matching. Matches random people together for a quick coffee meet up at regular intervals (e.g every week).

### Run locally

Python 3.10 is recommended. Python 3.6 is required (3.6 - 3.9 may cause unforseen issues, 3.10 is recommended).

Install [Google's client library](https://developers.google.com/gmail/api/quickstart/python). Ignore the OAuth consent screen section.

Obtain credentials JSON file from the ```Coffee Roulette``` Google Cloud project, via the service account ```coffee-roulette-email-client```. 
Simply navigate to **IAM and admin**, **Service accounts**, click on ```coffee-roulette-email-client```, **Keys**, click **Add key** and **Create new key**.
