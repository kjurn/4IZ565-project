import column_merger
import dataset_loader

data_accidents = dataset_loader.load_data()
print("------------------------")
print("Showing a head of a data")
print("------------------------")
print(data_accidents.head())

# column_merger.join_columns()


