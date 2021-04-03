from pandas import read_excel, merge, ExcelFile
from numpy import array

import dataset_loader
from log_utils import print_merge_error, print_merge_success, print_load_success


def join_columns():
    data = dataset_loader.load_data()
    # print("Preparing to join columns")
    # print("-------------------------")
    columns_path = "files/columns.xlsx"
    # name = read_excel(columns_path, sheet_name=None)
    columns_to_join = ExcelFile(columns_path)
    # print(columns_to_join.sheet_names)
    # number_of_sheets = len(columns_to_join.sheet_names)
    # print(number_of_sheets)
    # print(columns_to_join.parse(1).iloc[:, 1])

    # left_join = merge(data, columns_to_join.parse("Hárok1"), how="left")
    # print(left_join)
    # print(left_join.loc[:, 'Druh pozemní komunikace'])

    for i in columns_to_join.sheet_names:
        try:
            left_join = merge(data, columns_to_join.parse(i), how="left")
        except Exception as e:
            print_merge_error(data, columns_to_join, e)
            return

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

    # Index(['ID', 'Druh pozemní komunikace', 'Číslo pozemní komunikace',
    #        'Den, měsíc, rok', 'Den v týdnu', 'Čas ', 'Druh nehody',
    #        'Druh srážky jedoucích vozidel', 'Druh pevné překážky',
    #        'Charakter nehody', 'Zavinění nehody',
    #        'Alkohol u viníka nehody přítomen', 'Hlavní příčiny nehody',
    #        'Usmrceno osob', 'Těžce zraněno osob', 'Lehce zraněno osob',
    #        'Celková hmotná škoda', 'Druh povrchu vozovky',
    #        'Stav povrchu vozovky v době nehody', 'Stav komunikace',
    #        'Povětrnostní podmínky v době nehody', 'Viditelnost',
    #        'Rozhledové poměry', 'Dělení komunikace',
    #        'Situování nehody na komunikaci', 'Řízení provozu v době nehody',
    #        'Místní úprava přednosti v jízdě',
    #        'Specifická místa a objekty v místě nehody', 'Směrové poměry',
    #        'Počet zúčastněných vozidel', 'Místo dopravní nehody',
    #        'Druh křižující komunikace', 'Druh vozidla',
    #        'Výrobní značka motorového vozidla', 'Rok výroby vozidla',
    #        'Charakteristika vozidla ', 'Smyk', 'Vozidlo po nehodě',
    #        'Únik provozních, přepravovaných hmot',
    #        'Způsob vyproštění osob z vozidla', 'Směr jízdy nebo postavení vozidla',
    #        'Škoda na vozidle', 'Kategorie řidiče', 'Stav řidiče',
    #        'Vnější ovlivnění řidiče', 'a', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    #        'k', 'l', 'n', 'o', 'p', 'q', 'r', 's', 't', 'Lokalita nehody',
    #        'Lokalita_nehody', 'Hlavní_příčiny_nehody'],


join_columns()
