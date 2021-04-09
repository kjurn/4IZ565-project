import data_cleaner
import dataset_loader
import dataset_splitter
import decisiontree

data_accidents = data_cleaner.clean_duplicate_columns()
# data_accidents = dataset_loader.load_data()
print("------------------------")
print("Showing a head of a data")
print("------------------------")
print(data_accidents.head())
# print(decisiontree.create_tree(data_accidents))
split = dataset_splitter.split(data_accidents, "UPPER")

#TODO: implement tree
