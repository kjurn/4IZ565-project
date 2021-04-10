import data_cleaner
import dataset_loader
import dataset_splitter
import decisiontree
import target_creator

# load dataset
data_accidents = dataset_loader.load_data()
# create a target attribute
data_accidents = target_creator.simplify_target(data_accidents)
# remove useless columns and treat missing values
data_accidents = data_cleaner.remove_columns(data_accidents)
cleaned_data = data_cleaner.treat_missing_values(data_accidents)

print("------------------------------------------------------")
print("------------  Showing a head of a data  --------------")
print("------------------------------------------------------")
print(cleaned_data.head())
# create a model of a decision tree
decisiontree.create_tree(dataset_splitter.split(cleaned_data, "UPPER"))
