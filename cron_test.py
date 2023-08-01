from mailing import authenticate_mail, send_mail
import time

authenticate_mail("/home/pi/coffee-roulette/coffee-roulette-394514-45407839cfa3.json")
send_mail("857514.leofeng@gmail.com", f"cron test {time.time()}", f"Cron test at: {time.time()}")
