import PyPDF2


def read_pdf(pdf_file_path):
    try:
        pdf_file = open(pdf_file_path, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

        pdf_file.close()
        return text
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    pdf_path = r'C:\Users\Isabel\PycharmProjects\PB\programming-basics-files-promises\projects\005-words-that-occur-most\sample_file.pdf'
    extracted_text = read_pdf(pdf_path)

    if extracted_text:
        print(extracted_text)

