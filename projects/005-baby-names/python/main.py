'''In this exercise analyze the baby names dataset to gain insights into naming trends and diversity over the s.'''

from collections import Counter

def read_file():
    file = open('projects/005-baby-names/python/example.txt', 'r')
    read_file = file.readlines()
    file.close()
    return read_file

def name_diversity_analysis(file):
    names = set()
    for line in file:
        splitted_list = line.split(", ")
        if len(splitted_list) > 0:
            names.add(splitted_list[0].strip())
    return len(names)

def name_length_analysis(file):
    names = []
    for line in file:
        splitted_list = line.split(", ")
        if len(splitted_list) > 0:
            names.append(splitted_list[0].strip())
    name_lengths = [len(name) for name in names]
    avg_length = sum(name_lengths) / len(name_lengths) if name_lengths else 0
    return avg_length

def name_ending_analysis(file):
    names = []
    for line in file:
        splitted_list = line.split(", ")
        if len(splitted_list) > 0:
            names.append(splitted_list[0].strip())
    endings = [name[-1].lower() for name in names if name]
    most_common_ending = Counter(endings).most_common(1)
    return most_common_ending[0] if most_common_ending else ('', 0)

def name_initials_analysis(file):
    names = []
    for line in file:
        splitted_list = line.split(", ")
        if len(splitted_list) > 0:
            names.append(splitted_list[0].strip())
    initials = [name[0].upper() for name in names if name]
    initial_counts = Counter(initials)
    return initial_counts

def name_popularity_over_decades(file):
    decades = {}
    for line in file:
        splitted_list = line.split(", ")
        decade_key = splitted_list[1][:3] + "0s"
        if decade_key in decades:
            try:
                decades[decade_key][splitted_list[0]] += 1
            except KeyError:
                decades[decade_key][splitted_list[0]] = 1
        else:
            tmp = {splitted_list[0] : 1}
            decades[decade_key] = tmp
            
    for decade, names in decades.items():
        for name, counter in names.items():
            print(name, counter)

def main():
    file = read_file()
    name_popularity_over_decades(file)

    diversity = name_diversity_analysis(file)
    print(f"Total unique names: {diversity}")

    avg_length = name_length_analysis(file)
    print(f"Average name length: {avg_length:.2f} characters")

    common_ending = name_ending_analysis(file)
    print(f"Most common ending letter: '{common_ending[0]}' with {common_ending[1]} occurrences")

    initial_counts = name_initials_analysis(file)
    print(f"Initial letter counts: {initial_counts}")

if __name__ == "__main__":
    main()