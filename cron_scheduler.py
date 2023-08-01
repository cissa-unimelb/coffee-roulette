from crontab import CronTab

cron = CronTab(user='root')
job = cron.new(command='/usr/bin/python3 /mnt/d/Projects/CoffeeRoulette/cron_test.py')
job.day.on(1, 15)
job.hour.on(0)
job.minute.on(0)
cron.write()