import os.path
import sys
from PyPDF2 import PdfReader, PdfWriter, PdfMerger
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import re


def text_extraction(path_file):
    extracted_text = ""

    with open(path_file, 'rb') as file:
        reader = PdfReader(file)
        number_of_pages = len(reader.pages)

        for page in range(number_of_pages):
            text = reader.pages[page].extract_text()
            extracted_text += text

    return extracted_text


def split_pdf(path_file, start_page, stop_page):
    files = []

    with open(path_file, 'rb') as file:

        reader = PdfReader(file)
        number_of_pages = len(reader.pages)

        if start_page >= number_of_pages or start_page > stop_page:
            raise ValueError("The number of pages entered is wrong!")

        if start_page == stop_page:
            stop_page += 1

        if start_page > 0:
            start_page -= 1

        if start_page < number_of_pages >= stop_page:

            while start_page < stop_page:
                selected_page = reader.pages[start_page]
                writer = PdfWriter()
                writer.add_page(selected_page)
                file_name = os.path.splitext(path_file)[0]
                output_file = f"{file_name}_page_{start_page + 1}.pdf"

                with open(output_file, 'wb') as out:
                    writer.write(out)

                print(f"The {output_file} file has been created!")

                files.append(output_file)
                start_page += 1

        else:

            print(
                "You only have to enter 2 numbers at most: the number of the first page and the last page of the "
                "PDF file you want to split!!"
            )
            raise ValueError("The number of pages entered is wrong!")

    return files


def merging_pdf(pdfs_list, output_file):
    merger = PdfMerger()

    with open(output_file, "wb") as f:
        for file in pdfs_list:
            merger.append(file)

        merger.write(f)

        return f"The {output_file} file has been created!"


def replace(page_number, rows_number, word_number, path_file, text_to_add, text_to_replace):

    if page_number > 0 or rows_number > 0 or word_number > 0:

        page_number = page_number - 1
        rows_number = rows_number - 1
        word_number = word_number - 1

    else:

        raise ValueError("The page and line numbers must be greater than zero!")

    with open(path_file, 'rb') as file:

        reader = PdfReader(file)
        text = reader.pages[page_number].extract_text()
        text = re.split(r'\n', text)

        rows = []

        for row in text:

            if row != " ":
                rows.append(row)

        selected_row = rows[rows_number]

        if text_to_replace.strip() in selected_row.strip():

            counter = 0

            while counter < len(text):

                if selected_row.strip() == text[counter].strip():

                    if text[counter].split(" ")[word_number] == text_to_replace.split(" ")[0]:

                        new_text = []
                        c = 0

                        while c < len(text[counter].split(" ")):

                            if c != word_number:

                                new_text.append(text[counter].split(" ")[c])
                                c += 1

                            else:

                                new_text.append(text_to_add)
                                c += len(text_to_replace.split(" "))

                        text[counter] = " ".join(new_text)

                    while len(text[counter]) > 90:

                        if text[counter + 1] == " ":

                            text.insert(counter + 1, " ")
                            text[counter + 1] = text[counter][90:-1] + " " + text[counter + 1]
                            text[counter] = text[counter][0:90]

                        else:

                            text[counter + 1] = text[counter][90:-1] + " " + text[counter + 1]
                            text[counter] = text[counter][0:90]

                        counter += 1

                    break

                counter += 1

        new_text = []
        counter = 0

        while counter < len(text):

            if text[counter] == " ":

                new_text.append("")
                new_text.append("")

            new_text.append(text[counter])
            counter += 1

        number_of_pages = len(reader.pages)
        files = split_pdf(path_file, 0, number_of_pages)
        file_name = os.path.splitext(path_file)[0]
        output_file = f"{file_name}_page_{page_number + 1}.pdf"

        with open(output_file, 'wb') as f:

            counter = canvas.Canvas(f, pagesize=A4)
            width, height = A4

            text = counter.beginText(50, height - 50)
            text.setFont("Times-Roman", 12)

            text.textLines(new_text)

            counter.drawText(text)

            counter.showPage()
            counter.save()

    return merging_pdf(files, path_file)


def delete(page_number, rows_number, word_number, path_file, text_to_delete):

    if page_number > 0 or rows_number > 0 or word_number > 0:

        page_number = page_number - 1
        rows_number = rows_number - 1
        word_number = word_number - 1

    else:

        raise ValueError("The page and line numbers must be greater than zero!")

    with open(path_file, 'rb') as file:

        reader = PdfReader(file)
        text = reader.pages[page_number].extract_text()
        text = re.split(r'\n', text)

        rows = []

        for row in text:

            if row != " ":
                rows.append(row)

        selected_row = rows[rows_number]

        if text_to_delete.strip() in selected_row.strip():

            counter = 0

            while counter < len(text):

                if selected_row.strip() == text[counter].strip():

                    if text[counter].split(" ")[word_number] == text_to_delete.split(" ")[0]:

                        new_text = []
                        c = 0

                        while c < len(text[counter].split(" ")):

                            if c != word_number:
                                new_text.append(text[counter].split(" ")[c])
                                c += 1

                            else:

                                c += len(text_to_delete.split(" "))

                        text[counter] = " ".join(new_text)

                    break

                counter += 1

        else:

            raise ValueError(f"{text_to_delete} not found!")

        new_text = []
        counter = 0

        while counter < len(text):

            if text[counter] == " ":

                new_text.append("")
                new_text.append("")

            new_text.append(text[counter])
            counter += 1

        number_of_pages = len(reader.pages)

        files = split_pdf(path_file, 0, number_of_pages)
        file_name = os.path.splitext(path_file)[0]
        output_file = f"{file_name}_page_{page_number + 1}.pdf"

        with open(output_file, 'wb') as f:

            counter = canvas.Canvas(f, pagesize=A4)
            width, height = A4

            text = counter.beginText(50, height - 50)
            text.setFont("Times-Roman", 12)

            text.textLines(new_text)

            counter.drawText(text)

            counter.showPage()
            counter.save()

    print("Deleted!")

    return merging_pdf(files, path_file)


def add_text(page_number, rows_number, word_number, path_file, text_to_add):

    if page_number > 0:

        page_number = page_number - 1
        rows_number = rows_number - 1

    else:

        raise ValueError("The page and line numbers must be greater than zero!")

    with open(path_file, 'rb') as file:

        reader = PdfReader(file)
        number_of_pages = len(reader.pages)

        text = reader.pages[page_number].extract_text()
        text = re.split(r'\n', text)

        rows = []

        for row in text:

            if row != " ":
                rows.append(row)

        selected_row = rows[rows_number]

        counter = 0

        while counter < len(text):

            if selected_row.strip() == text[counter].strip():

                text[counter] = text[counter].split()
                text[counter].insert(word_number, text_to_add)
                text[counter] = " ".join(text[counter])

                while len(text[counter]) > 100:

                    if text[counter + 1] == " ":

                        text.insert(counter + 1, " ")
                        text[counter + 1] = text[counter][100:-1] + " " + text[counter + 1]
                        text[counter] = text[counter][0:100]

                    else:

                        text[counter + 1] = text[counter][100:-1] + " " + text[counter + 1]
                        text[counter] = text[counter][0:100]

                    counter += 1

                break

            counter += 1

        new_text = []
        counter = 0

        while counter < len(text):

            if text[counter] == " ":
                new_text.append("")
                new_text.append("")

            new_text.append(text[counter])

            if counter == len(text) - 1:
                new_text.append("")

            counter += 1

        files = split_pdf(path_file, 0, number_of_pages)
        file_name = os.path.splitext(path_file)[0]
        output_file = f"{file_name}_page_{page_number + 1}.pdf"

        with open(output_file, 'wb') as f:

            counter = canvas.Canvas(f, pagesize=A4)
            width, height = A4

            text = counter.beginText(50, height - 50)
            text.setFont("Times-Roman", 12)

            text.textLines(new_text)

            counter.drawText(text)

            counter.showPage()
            counter.save()

    return merging_pdf(files, path_file)


def search_file_txt(n, command):
    file_pdf = command[n]
    script = command[0]
    directory = os.path.dirname(os.path.abspath(script))
    path_file = None

    while True:

        if file_pdf in os.listdir(directory):
            path_file = os.path.join(directory, file_pdf)
            file_pdf = "../" + file_pdf

            break

        directory = os.path.dirname(directory)

        if directory == os.path.dirname(directory):
            break

    return path_file, file_pdf


def user_interface():

    command = sys.argv
    script = os.path.basename(__file__)

    suggested_option = (
        f"{script} -r file.pdf: allows to read the pdf file;\n"

        f"{script} -s [first page number - last page number] file.pdf: split a PDF file into multiple "
        f"smaller PDF files based on page ranges specified by the user;\n"

        f"{script} -m file_1.pdf, file_2.pdf -o output_file.pdf: concatenate a list of pdf files into a "
        f"single output PDF;\n"

        f"{script} delete [page_number - row_number - number_of_first_word_to_delete] -t text_to_delete file.pdf: "
        f"delete specific text content from the PDF file;\n"

        f"{script} add [page_number - row_number - word_number] -t text_to_add file.pdf: add new text to "
        f"specific locations within the PDF document;\n"

        f"{script} replace text_to_replace -o [page_number - row_number - number_of_first_word_to_replace] -t "
        f"text_to_add file.pdf: replace a text string with a new text string within the pdf file.\n"
    )

    if len(command) < 3:
        raise ValueError(f"Invalid command! Options:\n{suggested_option}")

    if " ".join(command[:2]) not in [f"{script} -r", f"{script} -s", f"{script} -m", f"{script} replace",
                                     f"{script} add", f"{script} delete"]:
        raise ValueError(f"Invalid command! Options:\n{suggested_option}")

    if len(command) == 3:

        if command[1] == "-r":

            path = search_file_txt(-1, command)[1]

            if path:

                try:

                    print(text_extraction(path))

                except OSError:

                    print('cannot open', path)

            else:

                raise FileNotFoundError(f"{path} not found!")
        else:

            raise ValueError(f"Invalid command! Options:\n{suggested_option}")

    elif len(command) >= 6:

        if command[1] == "-s":

            text_to_replace = []

            if len(command) > 4:

                for i in command[2:]:

                    number = ""
                    counter = 0

                    while counter < len(i):

                        if i[counter].isdigit():
                            number += i[counter]

                        counter += 1

                    if number:
                        text_to_replace.append(number)

            else:

                for i in command[2:]:

                    try:

                        number = ""

                        for ch in i:

                            if ch.isdigit():

                                number += ch

                            else:

                                if number:
                                    text_to_replace.append(number)

                                number = ""

                        if len(text_to_replace) > 2:
                            print(
                                "You only have to enter 2 numbers at most: the number of the first page and the last "
                                "page of the PDF file you want to split!!"
                            )

                    except ValueError:

                        raise ValueError(f"Invalid command! Options:\n{suggested_option}")

            start_page = text_to_replace[0]
            stop_page = text_to_replace[1]

            try:

                start_page = int(start_page)
                stop_page = int(stop_page)
                path = search_file_txt(-1, command)[1]

                if start_page < 0 or stop_page < 0:
                    raise ValueError("Number must be greater than zero!")

            except ValueError:

                raise ValueError("Number must be greater than zero!")

            if path:

                print(split_pdf(path, start_page, stop_page))

            else:

                raise FileNotFoundError(f"{path} not found!")

        elif command[1] == "-m" and command[-2] == "-o":

            files = []
            counter = 0

            for file in command[2:-2]:

                if file[-4:] == ".pdf":

                    while True:

                        if file == command[counter]:

                            path = search_file_txt(counter, command)[1]

                            if path:

                                files.append(path)

                            else:

                                raise FileNotFoundError(f"{path[1]} not found!")

                            break

                        else:

                            counter += 1

            if files:
                print(merging_pdf(files, command[-1]))

        elif command[1] == "delete":

            text_to_replace = []

            if "-t" in command:

                if len(command) > 6:

                    for i in command[2:]:

                        if i == "-t":

                            break

                        number = ""
                        counter = 0

                        while counter < len(i):

                            if i[counter].isdigit():

                                number += i[counter]

                            counter += 1

                        if number:
                            text_to_replace.append(number)

                else:

                    for i in command[2:]:

                        try:

                            number = ""

                            for ch in i:

                                if ch.isdigit():

                                    number += ch

                                else:

                                    if number:

                                        text_to_replace.append(number)

                                    number = ""

                        except ValueError:

                            raise ValueError(f"Invalid command! Options:\n{suggested_option}")

                if len(text_to_replace) == 3:

                    page = int(text_to_replace[0])
                    row = int(text_to_replace[1])
                    word = int(text_to_replace[2])

                    text_to_replace = []

                    for i in command[::-1]:

                        if i == "-t":
                            break

                        text_to_replace.append(i)

                    text_to_replace.reverse()
                    text_to_replace = " ".join(text_to_replace[:-1])
                    path = search_file_txt(-1, command)[1]

                    if path:

                        print(delete(page, row, word, path, text_to_replace))

                    else:

                        raise FileNotFoundError(f"{path[1]} not found!")

            else:

                print(
                    "You only have to enter 2 numbers at most: the number of the page and the number of the row"
                )

                raise ValueError(f"Invalid command! Options:\n{suggested_option}")

        elif command[1] == "add":

            text_to_replace = []

            if "-t" in command:

                if len(command) > 6:

                    for i in command[2:]:

                        if i == "-t":
                            break

                        number = ""
                        counter = 0

                        while counter < len(i):

                            if i[counter].isdigit():
                                number += i[counter]

                            counter += 1

                        if number:
                            text_to_replace.append(number)

                else:

                    for i in command[2:]:

                        try:

                            number = ""

                            for ch in i:

                                if ch.isdigit():

                                    number += ch

                                else:

                                    if number:
                                        text_to_replace.append(number)

                                    number = ""

                        except ValueError:

                            raise ValueError(f"Invalid command! Options:\n{suggested_option}")

                if len(text_to_replace) == 3:

                    page = int(text_to_replace[0])
                    row = int(text_to_replace[1])
                    word = int(text_to_replace[2])

                    text_to_replace = []

                    for i in command[::-1]:

                        if i == "-t":
                            break

                        text_to_replace.append(i)

                    text_to_replace.reverse()
                    text_to_replace = " ".join(text_to_replace[:-1])
                    path = search_file_txt(-1, command)[1]

                    if path:

                        print(add_text(page, row, word, path, text_to_replace))

                    else:

                        raise FileNotFoundError(f"{path[1]} not found!")

                else:

                    print(
                        "You only have to enter 2 numbers at most: the number of the page and the number of the row")

                    raise ValueError(f"Invalid command! Options:\n{suggested_option}")

        elif command[1] == "replace":

            text_to_replace = []

            counter = 0

            while counter < len(command):

                if command[counter] == "-o":

                    break

                text_to_replace.append(command[counter])
                counter += 1

            text_to_replace = " ".join(text_to_replace[2:])

            numbers = []
            counter += 1

            while counter < len(command):

                if command[counter] == "-t":

                    break

                numbers.append(command[counter])
                counter += 1

            if len(numbers) > 1:

                list_of_numbers = []

                for i in numbers:

                    number = ""
                    c = 0

                    while c < len(i):

                        if i[c].isdigit():

                            number += i[c]

                        c += 1

                    if number:

                        list_of_numbers.append(number)
            else:

                list_of_numbers = []

                for i in numbers:

                    try:

                        number = ""

                        for ch in i:

                            if ch.isdigit():

                                number += ch

                            else:

                                if number:
                                    list_of_numbers.append(number)

                                number = ""

                    except ValueError:

                        raise ValueError(f"Invalid command! Options:\n{suggested_option}")

            if len(list_of_numbers) == 3:

                page = int(list_of_numbers[0])
                row = int(list_of_numbers[1])
                word = int(list_of_numbers[2])

                text_to_add = " ".join(command[counter + 1:-1])
                path = search_file_txt(-1, command)[1]

                if path:

                    print(replace(page, row, word, path, text_to_add, text_to_replace))

                else:

                    raise FileNotFoundError(f"{path[1]} not found!")

            else:

                print(
                    "You only have to enter 2 numbers at most: the number of the page and the number of the row")

                raise ValueError(f"Invalid command! Options:\n{suggested_option}")

        else:

            raise ValueError(f"Invalid command! Options:\n{suggested_option}")

    else:

        raise ValueError(f"Invalid command! Options:\n{suggested_option}")


if __name__ == '__main__':
    user_interface()
