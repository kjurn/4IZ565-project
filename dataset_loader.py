from pandas import read_csv, read_excel

from log_utils import print_load_error, print_load_success, print_merge_success, print_merge_error


def load_data():
    # Load header from Excel file
    files_path = "files/"
    header = "header.xlsx"
    excel_sheet_name = "Hárok1"
    main_csv = "HlmestoPraha2019.csv"
    try:
        names_of_columns = read_excel(files_path + header, sheet_name=excel_sheet_name, nrows=1)
    except Exception as e:
        print_load_error(header, e)
        return
    else:
        print_load_success(header)

    # Load dataset from .csv file
    try:
        dataset = read_csv(files_path + main_csv, delimiter=";", encoding="windows-1250", dtype={45: str, 46: str},
                           header=None)
    except Exception as e:
        print_load_error(main_csv, e)
        return
    else:
        print_load_success(main_csv)

    # Assign header to dataset
    try:
        dataset.columns = names_of_columns.columns
    except Exception as e:
        print_merge_error(header, main_csv, e)
        return
    else:
        print_merge_success(header, main_csv)
    return dataset
