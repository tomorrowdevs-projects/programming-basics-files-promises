from pypdf import PdfReader


def open_file(file):
    text = ""
    formatted_text = ""
    read_file = PdfReader(file)
    pages_number = len(read_file.pages)
    i = 0

    for page in range(pages_number):
        text += read_file.pages[i].extract_text()
        i += 1

    text = text.split(" ")

    if text:

        for word in text:

            for letter in word:

                if letter.isalpha():
                    formatted_text += letter.lower()

            formatted_text += " "

        return formatted_text.split(" ")

    raise FileNotFoundError(f"cannot open {file} file!")


def most_common_words(text):
    if text:

        words_counter = {word: 0 for word in text if word != ""}

        for word in text:

            if word != "":
                words_counter[word] += 1

        total_common_words = sorted([(value, key) for (key, value) in words_counter.items()], reverse=True)

        for frequency, word in total_common_words:
            print(f"{word}:{frequency}")

    return "Empty text!"


def main():
    file = '../sample_file.pdf'
    text = open_file(file)
    return most_common_words(text)


if __name__ == '__main__':
    main()
