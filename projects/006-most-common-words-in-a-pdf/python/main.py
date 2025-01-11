'''Read text data from a PDF file and perform word frequency analysis to determine the most common words.'''

from PyPDF2 import PdfReader

def read_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def most_common_words(content):
    words = content.split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    for word, count in word_counts.items():
        print(word, ":", count)

def main():
    pdf_path = "projects/006-most-common-words-in-a-pdf/python/sample_file.pdf"
    content = read_pdf(pdf_path)
    print(content)
    most_common_words(content)

if __name__ == '__main__':
    main()