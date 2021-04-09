import os

from pandas import merge, ExcelFile, DataFrame
from numpy import array

import dataset_loader
from log_utils import print_merge_error, print_merge_success, print_load_error


def join_columns():
    # get data
    data = dataset_loader.load_data()
    # get columns data
    columns_filename = "columns.xlsx"
    columns_path = os.path.join(dataset_loader.get_current_path(), "files/")

    try:
        columns_to_join = ExcelFile(columns_path + columns_filename)
    except Exception as e:
        print_load_error(columns_filename, e)
        return

    # This should be refactored
    # Initialize DataFrame with meaningless column
    init_df = [{'empt': 1}]
    left_join = DataFrame(init_df)
    # Join main dataset with columns
    for i in columns_to_join.sheet_names:
        try:
            if i == "Hárok1":
                left_join = merge(data, columns_to_join.parse(i), how="left")
            else:
                left_join = merge(left_join, merge(data, columns_to_join.parse(i), how="left"))
        except Exception as e:
            print_merge_error(dataset_loader.get_dataset_name(), columns_filename, e)
            return

    print_merge_success(dataset_loader.get_dataset_name(), columns_filename)
    # create and simplify target attribute
    main_causes_of_accidents = data.loc[:, "Hlavní příčiny nehody"]
    convert_values = []
    for i in main_causes_of_accidents:
        if i == 100:
            convert_values.append("nezaviněná řidičem")
        if 200 < i < 210:
            convert_values.append("nepřiměřená rychlost jízdy")
        if 300 < i < 312:
            convert_values.append("nesprávné předjíždění")
        if 400 < i < 415:
            convert_values.append("nedání přednosti v jízdě")
        if 500 < i < 517:
            convert_values.append("nesprávný způsob jízdy")
        if 600 < i < 616:
            convert_values.append("technická závada vozidla")

    left_join["Hlavní_příčiny_nehody"] = array(convert_values)
    return left_join
