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


def user_input():
    user_choice = input('Press Enter to write your text, or press "p" to insert the path of your file.txt: \n').lower()

    if user_choice not in ["", "p"]:

        return user_input()

    else:

        if user_choice == "":

            text = input("Enter your text here:\n")

            return text

        path = input("Enter the path of your file.txt here:\n")
        lines = read_files(path)

        return lines


def select_year(names, year):
    names_by_year = []

    for row in names:

        if row.split(",")[1] == f" {year}":

            names_by_year.append(row)

    return names_by_year


def select_sex(names, sex):

    names_by_sex = []

    for row in names:

        if row.split(",")[2][:-1] == f" {sex}":

            names_by_sex.append(row)

    return names_by_sex


def top_10_popular_names(all_names, year, sex):

    if all_names:

        names = select_sex(all_names, sex)
        names = select_year(names, year)
        names_counter = {m.split(",")[0]: 0 for m in names}

        for row in names:

            names_counter[row.split(",")[0]] += 1

        sorted_ranking = sorted([(value, key) for (key, value) in names_counter.items()], reverse=True)
        top_10 = sorted_ranking[:10]

        return top_10

    else:

        raise ValueError("Dataset error!")


def unique_names(all_names):

    years = {y.split(",")[1] for y in all_names}

    for sex in ["male", "female"]:

        print(f"\nTotal of unique {sex} names for each year in the database:\n")

        for year in years:

            names = select_sex(all_names, sex)
            counter = 0
            top_10_names = top_10_popular_names(names, year[1:], sex)

            for name in top_10_names:

                if name[0] == 1:

                    counter += 1

            if counter != 0:

                print(f"{year}: {counter}")
    return ""


def length_name(all_names):

    for sex in ["male", "female"]:

        print(f"\nAverage length of {sex} names for each year in the database:\n")

        names = select_sex(all_names, sex)
        counter = {m.split(",")[1]: 0 for m in names}
        years = {y.split(",")[1] for y in names}

        for year in years:

            length_names = 0
            names_counter = 0

            for row in names:

                if row.split(",")[1] == year:

                    length_names += (len(row.split(",")[0]))
                    names_counter += 1

            average = length_names // names_counter
            counter[year] += average

        for key, value in counter.items():

            print(f"{key}: {value}")

    return ""


def ending_analysis(all_names):

    for sex in ["male", "female"]:

        print(f"\nHere are the top 5 most popular last letters for {sex} names in the dataset:\n")

        names = select_sex(all_names, sex)
        last_letters = {}

        for name in names:

            name = name.split(",")[0]

            if len(name) <= 3:
                name = name[-2:]

            elif len(name) == 4:
                name = name[-3:]

            else:
                name = name[-4:]

            if name in last_letters:
                last_letters[name] += 1

            else:
                last_letters[name] = 1

        sorted_names = sorted([(value, key) for (key, value) in last_letters.items()], reverse=True)
        top_5 = sorted_names[:5]

        for letters, times in top_5:

            print(f"'{letters}': {times} times")

    return ""


def initials_analysis(all_names):

    for sex in ["male", "female"]:

        print(f"\nHere are the top 5 most popular first letters for {sex} names in the dataset:\n")

        names = select_sex(all_names, sex)
        initial_letters = {}

        for name in names:

            name = name.split(",")[0]

            if len(name) <= 3:

                name = name[:2]

            elif len(name) == 4:

                name = name[:3]

            else:

                name = name[:4]

            if name in initial_letters:

                initial_letters[name] += 1

            else:

                initial_letters[name] = 1

        sorted_ranking = sorted([(value, key) for (key, value) in initial_letters.items()], reverse=True)

        top_5 = sorted_ranking[:5]

        for letters, times in top_5:

            print(f"'{letters}': {times} times")

    return ""


def popular_names_decades(all_names):

    for sex in ["male", "female"]:

        print(f"\nHere are the top 5 most popular {sex} names for each decade in the dataset:\n")
        years = 1900

        while years < 2030:

            top_10 = []

            for year in range(years, years + 10):

                names = select_sex(all_names, sex)
                names = select_year(names, str(year))
                names_counter = {m.split(",")[0]: 0 for m in names}

                if names:

                    for row in names:
                        names_counter[row.split(",")[0]] += 1
                sorted_ranking = sorted([(value, key) for (key, value) in names_counter.items()], reverse=True)

                for name in sorted_ranking:
                    top_10.append(name)

            if top_10:

                print(f"{str(years)[2:]}s:")
                print(f"{top_10[:5]}\n")

            years += 10

    return ""


def read_file():

    names = user_input()
    year = input("Enter a year to view the most popular male and female names in it:\n")
    print(f"\nHere is the top 10 most popular male names in the dataset for the year {year}:\n")
    print(top_10_popular_names(names, year, "male"))
    print(f"\nHere is the top 10 most popular female names in the dataset for the year {year}:\n")
    print(top_10_popular_names(names, year, "female"))

    print(unique_names(names))

    print(length_name(names))

    print(ending_analysis(names))

    print(initials_analysis(names))

    print(popular_names_decades(names))


def main():
    return read_file()


if __name__ == '__main__':
    main()
