# coffee-roulette

Automated friend matching. Matches random people together for a quick coffee meet up at regular intervals (e.g every week)

### Run locally

Python 3.10 is recommended. Python 3.6 is required (3.6 - 3.9 may cause unforseen issues, 3.10 is recommended).

Install [Google's client library](https://developers.google.com/gmail/api/quickstart/python). Ignore the OAuth consent screen section.

Obtain credentials JSON file from the ```Coffee Roulette``` Google Cloud project, via the service account ```coffee-roulette-email-client```. 
Simply navigate to **IAM and admin**, **Service accounts**, click on ```coffee-roulette-email-client```, **Keys**, click **Add key** and **Create new key**.
Modify ```SERVICE_FILE_PATH``` in ```main.py``` with the appropriate credentials file path.

A CSV file containing details of people participating is needed. The format of the CSV must be identical to the existing ```people.csv```. 
Modify ```CSV_FILE_PATH``` in ```csv_processing.py``` with the appropriate CSV file path.
*Note: People with the active field marked FALSE will be excluded from the roulette*.

### Deployment

Coffee roulette uses Cron to automatically schedule scripts for execution at regular intervals. As such, it is recommended to run coffee roulette in a Linux environment.

First ensure Cron is running properly on the system. Try to schedule a Cron job as **root** to run ```cron_test.py``` every minute, it should send an email to some email address every minute.

Install python's cron module via ```pip install python-crontab```

Ensuring that Cron is running properly, run ```cron_scheduler.py``` and replace ```cron.new(command='/path/to/python /path/to/main.py')``` with the appropriate paths.

By default, coffee roulette is configuered to run on the 1st and 15th of every month at 12am (roughly once every fortnight). This can be adjusted in ```cron_scheduler.py```

## How does it work

Coffee Roulette uses a recursive backtracking algorithm to generate pairs of people that satisfy certain constraints.
It then uses the Gmail API to notify people who their coffee roulette partner is at regular intervals.

### Modifying constraints

Currently, Coffee Roulette has two constraints regarding pair generation:

- A given person's partner must be someone they have not met previously (i.e they were not selected as partners in previous iterations of coffee roulette)
- A given person's partner must not be from the same team (i.e they must have different roles in the CSV file)

These constraints can be amended/changed via ```satisfy_constraint()``` in ```matching.py```. 
Be aware that any additional arguments to ```satisfy_constraint()``` must be partially applied using ```functools.partial``` in ```find()```.
For more information see the relevant docstrings.
