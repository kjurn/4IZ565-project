def print_load_error(filename, exception):
    print("File", filename, "cannot be loaded, reason:", exception)


def print_load_success(filename):
    print("File", filename, "was successfully loaded.")


def print_merge_error(file1, file2, exception):
    print("Merge of files", file1, "and", file2, "failed, reason:", exception)


def print_merge_success(file1, file2):
    print("Merge of files", file1, "and", file2, "was successful.")
