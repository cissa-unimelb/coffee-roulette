from mailing import authenticate_mail, send_mail
from matching import find
from csv_processing import load_csv, get_name_email_mapping, get_name_role_mapping

SERVICE_FILE_PATH = "coffee-roulette-394514-45407839cfa3.json"
EMAIL_SUBJECT = "CISSA Coffee/LeetCode time!"
EMAIL_CONTENT = "Hi {receiver}\n\nWelcome to Coffee Roulette!\n\nThis round of coffee roulette you've been paired " \
                "with {partner} from the {partner_role} team.\n\nFeel free to message or email {partner} to organise " \
                "a time and place, their CISSA email is {partner_email}.\n\nHint: A really good time/place to get " \
                "free coffee is Wednesday 12.30pm~1.30pm at our DiversiTea sessions!\n\nHave fun!\n\nCISSA Committee\n"

authenticate_mail(SERVICE_FILE_PATH)
load_csv()

name_email_mapping = get_name_email_mapping()
name_role_mapping = get_name_role_mapping()
for pair in find():
    print(pair)
    send_mail(name_email_mapping[pair[0]], EMAIL_SUBJECT, EMAIL_CONTENT.format(
        receiver=pair[0], partner=pair[1], partner_role=name_role_mapping[pair[1]],
        partner_email=name_email_mapping[pair[1]]))
    send_mail(name_email_mapping[pair[1]], EMAIL_SUBJECT, EMAIL_CONTENT.format(
        receiver=pair[1], partner=pair[0], partner_role=name_role_mapping[pair[0]],
        partner_email=name_email_mapping[pair[0]]))
