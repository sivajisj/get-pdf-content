import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def find_details_by_name(text, name):
    # Split the text into lines
    lines = text.split('\n')
    # Initialize variables to store details
    details = []
    # Iterate through lines to find details associated with the name
    for line in lines:
        # Check if the line contains the name
        if name in line:
            # Extract details from nearby lines
            details.append(line.strip())
            # Extract additional lines for more details if needed
            for i in range(1, 5):
                details.append(lines[lines.index(line) + i].strip())
    return '\n'.join(details)


# Replace "your_pdf_file.pdf" with the path to your PDF file
pdf_text = extract_text_from_pdf("one.pdf")
# print(pdf_text)
name = input("Enter Full Name Name of the Person: ")
details = find_details_by_name(pdf_text, name)
print(details)
