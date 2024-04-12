import matplotlib.pyplot as plt


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


"""
User Input. The program will prompt the user to enter the text or provide the path to a text file they want to
analyze.
"""


def user_input():
    user_choice = input('Press enter to write your text, or press "p" to insert the path of your file.txt: \n').lower()

    if user_choice not in ["", "p"]:

        return user_input()

    else:

        if user_choice == "":
            text = input("Enter your text here:\n")

            return text

        path = input("Enter the path of your file.txt here:\n")
        lines = read_files(path)

        return "".join(lines)


"""
Text Processing. The program will clean the input text by removing punctuation, numbers, and other non-letter 
characters. Remove punctuation and non-letter characters using regular expressions or string manipulation techniques.
"""


def text_processing(txt):
    new_text = ""

    for character in txt:

        if character.isalpha():
            new_text += character.lower()

    return new_text


"""
Letter Frequency Analysis. The program will calculate the frequency of each letter (case-insensitive) in the cleaned 
text.
"""


def frequency_letters(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    counter = {letter: 0 for letter in alphabet}

    for character in text:
        counter[character] += 1

    return counter


def display_chart(text):
    dict_letters = frequency_letters(text)
    values = []
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z']
    i = 0

    for key, value in dict_letters.items():

        if key.upper() == letters[i]:
            values.append(value)

        i += 1

    plt.bar(letters, values, color='blue')
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.title('Frequency letters')

    plt.show()


"""
User Interaction. The program will ask the user if they want to analyze another text or exit the program.
"""


def user_interaction():
    while True:

        continue_to_analyze = input("Press enter if you want to analyze another text or any key to close the program:")

        if continue_to_analyze != "":
            break

        text = user_input()
        processed_test = text_processing(text)
        print(display_chart(processed_test))
    return "Closing the program..."


def main():
    return user_interaction()


if __name__ == '__main__':
    main()
