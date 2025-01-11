import PyPDF2

def read_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text() + '\n'
        return text
    except Exception as e:
        return f"Error reading the PDF: {e}"

def replace_text(input_path, output_path, search_text, replace_text):
    try:
        reader = PyPDF2.PdfReader(input_path)
        writer = PyPDF2.PdfWriter()

        for page in reader.pages:
            text = page.extract_text()
            if text:
                new_text = text.replace(search_text, replace_text)
                page = PyPDF2.PageObject.create_blank_page(None, page.mediabox.width, page.mediabox.height)
            writer.add_page(page)

        with open(output_path, 'wb') as output_file:
            writer.write(output_file)
        print("Text replacement completed.")
    except Exception as e:
        print(f"Error replacing text: {e}")

def merge_pdfs(pdf_list, output_path):
    try:
        writer = PyPDF2.PdfWriter()
        for pdf in pdf_list:
            reader = PyPDF2.PdfReader(pdf)
            for page in reader.pages:
                writer.add_page(page)
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)
        print("PDFs merged successfully.")
    except Exception as e:
        print(f"Error merging PDFs: {e}")

def split_pdf(input_path, page_ranges):
    try:
        reader = PyPDF2.PdfReader(input_path)
        for i, (start, end) in enumerate(page_ranges):
            writer = PyPDF2.PdfWriter()
            for page_num in range(start, end + 1):
                writer.add_page(reader.pages[page_num])
            with open(f"output_part_{i + 1}.pdf", 'wb') as output_file:
                writer.write(output_file)
        print("PDF split successfully.")
    except Exception as e:
        print(f"Error splitting PDF: {e}")

def main():
    print("PDF Command-Line Editor")
    print("1. Extract Text")
    print("2. Replace Text")
    print("3. Merge PDFs")
    print("4. Split PDF")
    choice = input("Select an option (1-4): ")

    if choice == '1':
        file_path = input("Enter PDF file path: ")
        print(read_pdf(file_path))
    elif choice == '2':
        input_path = input("Enter input PDF file path: ")
        output_path = input("Enter output PDF file path: ")
        search_text = input("Enter text to search: ")
        replacement_text = input("Enter replacement text: ")
        replace_text(input_path, output_path, search_text, replacement_text)
    elif choice == '3':
        pdf_list = input("Enter PDF file paths separated by commas: ").split(',')
        output_path = input("Enter output PDF file path: ")
        merge_pdfs(pdf_list, output_path)
    elif choice == '4':
        input_path = input("Enter input PDF file path: ")
        ranges = input("Enter page ranges (e.g., 1-3,4-6): ")
        page_ranges = [tuple(map(int, r.split('-'))) for r in ranges.split(',')]
        split_pdf(input_path, page_ranges)
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()