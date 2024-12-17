'''In this exercise analyze the baby names dataset to gain insights into naming trends and diversity over the years.'''

from collections import Counter

def read_file(year):
    if year == 2020:
        file = open('projects/005-baby-names/python/example.txt', 'r')
        return file
    elif year == 2023:
        file = open('projects/005-baby-names/python/example2.txt', 'r')
        return file
    else:
        print("year non valido! Scegliere tra 2020 o 2023.")

def name_diversity_analysis(file):
    names = set(line.strip() for line in file.readlines())
    return len(names)

def name_length_analysis(file):
    names = [line.strip() for line in file.readlines()]
    name_lengths = [len(name) for name in names]
    avg_length = sum(name_lengths) / len(name_lengths)
    return avg_length

def name_ending_analysis(file):
    names = [line.strip() for line in file.readlines()]
    endings = [name[-1].lower() for name in names]
    most_common_ending = Counter(endings).most_common(1)
    return most_common_ending[0]

def name_initials_analysis(file):
    names = [line.strip() for line in file.readlines()]
    initials = [name[0].upper() for name in names]
    initial_counts = Counter(initials)
    return initial_counts

def name_popularity_over_decades(year, file):
    yearselectedlist = file.readlines()
    print("".join(yearselectedlist[1:6]))
    print("".join(yearselectedlist[13:18]))

def main():
    year = int(input("Please input the year of which you desire to know the most popular names (2020 or 2023): "))
    file = read_file(year)
    name_popularity_over_decades(year, file)
    file.seek(0)

    diversity = name_diversity_analysis(file)
    print(f"Total unique names: {diversity}")
    file.seek(0)

    avg_length = name_length_analysis(file)
    print(f"Average name length: {avg_length:.2f} characters")
    file.seek(0)

    common_ending = name_ending_analysis(file)
    print(f"Most common ending letter: '{common_ending[0]}' with {common_ending[1]} occurrences")
    file.seek(0)

    initial_counts = name_initials_analysis(file)
    print(f"Initial letter counts: {initial_counts}")

    file.close()

if __name__ == "__main__":
    main()