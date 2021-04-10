from pandas import to_numeric
import target_creator
from log_utils import print_column_delete_success, print_clean_success


def remove_columns(dataset):
    # Get data with created target variable
    # data_to_clean = target_creator.simplify_target()
    # Delete useless attributes and attributes with a lot of missings
    dataset.drop("ID", axis=1, inplace=True)
    dataset.drop("Číslo pozemní komunikace", axis=1, inplace=True)
    dataset.drop("Den, měsíc, rok", axis=1, inplace=True)
    dataset.drop("Čas ", axis=1, inplace=True)
    dataset.drop("Druh křižující komunikace", axis=1, inplace=True)
    dataset.drop("Lokalita nehody", axis=1, inplace=True)

    for i in range(1, 19):
        dataset.drop(dataset.columns[40], axis=1, inplace=True)

    print_column_delete_success()
    return dataset


def treat_missing_values(dataset):
    # Replace missing values with median category
    impute_value = dataset["Charakteristika vozidla "].median()
    dataset["Charakteristika vozidla "] = dataset["Charakteristika vozidla "].fillna(impute_value)

    impute_value = dataset["Výrobní značka motorového vozidla"].median()
    dataset["Výrobní značka motorového vozidla"] = dataset["Výrobní značka motorového vozidla"].fillna(impute_value)

    impute_value = dataset["Smyk"].median()
    dataset["Smyk"] = dataset["Smyk"].fillna(impute_value)

    impute_value = dataset["Vozidlo po nehodě"].median()
    dataset["Vozidlo po nehodě"] = dataset["Vozidlo po nehodě"].fillna(impute_value)

    impute_value = dataset["Únik provozních, přepravovaných hmot"].median()
    dataset["Únik provozních, přepravovaných hmot"] = dataset["Únik provozních, přepravovaných hmot"].fillna(
        impute_value)

    impute_value = dataset["Způsob vyproštění osob z vozidla"].median()
    dataset["Způsob vyproštění osob z vozidla"] = dataset["Způsob vyproštění osob z vozidla"].fillna(
        impute_value)

    impute_value = dataset["Směr jízdy nebo postavení vozidla"].median()
    dataset["Směr jízdy nebo postavení vozidla"] = dataset["Směr jízdy nebo postavení vozidla"].fillna(
        impute_value)

    impute_value = dataset["Kategorie řidiče"].median()
    dataset["Kategorie řidiče"] = dataset["Kategorie řidiče"].fillna(
        impute_value)

    impute_value = dataset["Stav řidiče"].median()
    dataset["Stav řidiče"] = dataset["Stav řidiče"].fillna(
        impute_value)

    impute_value = dataset["Vnější ovlivnění řidiče"].median()
    dataset["Vnější ovlivnění řidiče"] = dataset["Vnější ovlivnění řidiče"].fillna(
        impute_value)

    dataset["Rok výroby vozidla"] = to_numeric(dataset["Rok výroby vozidla"], errors='coerce')
    impute_value = dataset["Rok výroby vozidla"].median()
    dataset["Rok výroby vozidla"] = dataset["Rok výroby vozidla"].fillna(impute_value)
    print_clean_success()
    return dataset

    # old code
    # data_to_clean.drop(data_to_clean.columns[1], axis=1, inplace=True)
    # data_to_clean.drop(data_to_clean.columns[3], axis=1, inplace=True)

    # for i in range(1, 8):
    #     data_to_clean.drop(data_to_clean.columns[4], axis=1, inplace=True)
    #
    # for i in range(1, 13):
    #     data_to_clean.drop(data_to_clean.columns[8], axis=1, inplace=True)
    #
    # for i in range(1, 4):
    #     data_to_clean.drop(data_to_clean.columns[10], axis=1, inplace=True)
    #
    # for i in range(1, 7):
    #     data_to_clean.drop(data_to_clean.columns[11], axis=1, inplace=True)
    #
    # for i in range(1, 23):
    #     data_to_clean.drop(data_to_clean.columns[12], axis=1, inplace=True)
