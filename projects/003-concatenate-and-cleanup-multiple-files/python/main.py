import os


def search_file_txt(file_txt):

    script = os.path.basename(__file__)
    directory = os.path.dirname(os.path.abspath(script))

    while True:

        for (root, dirs, file) in os.walk(directory):

            for f in file:

                if f == file_txt:

                    path_file = os.path.join(root, file_txt)

                    return path_file

        directory = os.path.dirname(directory)


# read files
def read_files(path):

    if path:

        try:

            with open(path, 'r') as f:

                lines = f.readlines()

            return lines

        except OSError:

            print('cannot open', path)

    else:

        raise FileNotFoundError(f"{path} not found!")


# concatenate files
def concatenate_files(file_to_write, file_to_get_values):

    path_1 = search_file_txt(file_to_get_values)
    lines = read_files(path_1)
    path_2 = search_file_txt(file_to_write)

    if file_to_get_values:

        with open(path_2, 'a') as file_txt:

            file_txt.write(f"File name: {file_to_get_values}\n")
            file_txt.writelines(lines)

        return "Done!"

    else:

        raise f"Cannot get values from the file {file_to_get_values}. Empty file!"


# remove duplicates
# Remove any lines with missing or incomplete information.
# Remove any leading or trailing whitespace from each line.
def clean_dataset(file):

    path = search_file_txt(file)
    lines = read_files(path)
    no_duplicates = []

    for line in lines:

        if line not in no_duplicates and len(line.split(",")) == 4 and line != " ":

            no_duplicates.append(line)

    with open(path, 'w') as file_txt:

        file_txt.writelines(no_duplicates)

    return ""


# save_file
def save_file(files, file):

    for rows in files:

        print(concatenate_files(file, rows))

    print(clean_dataset("combined_products.txt"))

    return ""


def main():

    files = ["products_1.txt", "products_2.txt", "products_3.txt"]
    print(save_file(files, "combined_products.txt"))

    return ""


if __name__ == '__main__':
    print(main())
