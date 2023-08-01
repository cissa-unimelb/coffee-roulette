import csv


def load_csv(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        return list(filter(lambda x: x[3] != 'FALSE', list(reader)))[1:]


def get_name_list(csv_data):
    return [row[0] for row in csv_data]


def get_name_email_mapping(csv_data):
    return {row[0]: row[1] for row in csv_data}