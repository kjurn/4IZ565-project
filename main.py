import data_cleaner

data_accidents = data_cleaner.clean_duplicate_columns()
print("------------------------")
print("Showing a head of a data")
print("------------------------")
print(data_accidents.head())


