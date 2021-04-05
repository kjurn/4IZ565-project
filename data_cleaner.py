import column_merger
from log_utils import print_clean_success


def clean_duplicate_columns():
    data_to_clean = column_merger.join_columns()

    data_to_clean.drop(data_to_clean.columns[1], axis=1, inplace=True)
    data_to_clean.drop(data_to_clean.columns[3], axis=1, inplace=True)

    for i in range(1, 8):
        data_to_clean.drop(data_to_clean.columns[4], axis=1, inplace=True)

    for i in range(1, 13):
        data_to_clean.drop(data_to_clean.columns[8], axis=1, inplace=True)

    for i in range(1, 4):
        data_to_clean.drop(data_to_clean.columns[10], axis=1, inplace=True)

    for i in range(1, 7):
        data_to_clean.drop(data_to_clean.columns[11], axis=1, inplace=True)

    for i in range(1, 23):
        data_to_clean.drop(data_to_clean.columns[12], axis=1, inplace=True)

    print_clean_success()

    return data_to_clean
