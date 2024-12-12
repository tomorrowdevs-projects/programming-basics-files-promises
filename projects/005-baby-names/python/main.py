'''In this exercise analyze the baby names dataset to gain insights into naming trends and diversity over the years.'''

def read_file(anno):
    if anno == 2020:
        file = open('projects/005-baby-names/python/example.txt', 'r')
        return file
    if anno == 2023:
        file = open('projects/005-baby-names/python/example2.txt', 'r')
        return file

def name_diversity_analysis():
    next

def name_length_analysis():
    next

def name_ending_analysis():
    next

def name_initials_analysis():
    next

def name_popularity_over_decades(anno, file):
    yearselectedlist = file.readlines()
    print(yearselectedlist[2:6])
    print(yearselectedlist[14:18])

def main():
    anno = ("Please input the year of which you desire to know the most popular names (2020 or 2023): ")
    file = read_file(anno)


if __name__ == "__main__":
    main()