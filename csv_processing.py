import csv

CSV_FILE_PATH = "people.csv"
csv_data = None


def load_csv():
    global csv_data
    with open(CSV_FILE_PATH, 'r') as f:
        reader = csv.reader(f)
        csv_data = list(filter(lambda x: x[3] != 'FALSE', list(reader)))[1:]


def get_name_list():
    return [row[0] for row in csv_data]


def get_name_email_mapping():
    return {row[0]: row[2] for row in csv_data}


def get_name_role_mapping():
    return {row[0]: row[1] for row in csv_data}