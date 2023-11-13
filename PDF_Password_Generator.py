import PyPDF2
import tkinter as tk
from tkinter import filedialog, simpledialog
import os

def add_password(input_pdf, output_pdf, password):
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()

        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        pdf_writer.encrypt(password)

        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)

def select_pdf_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(filetypes=[('PDF Files', '*.pdf')],
                                           title='Select a PDF file')

    return file_path

def get_password():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    password = simpledialog.askstring("Password", "Enter password for the PDF:",
                                      show='*')

    return password

def get_output_file_path(input_pdf_file_path):
  """Returns the output PDF file path in the same directory as the input PDF file."""

  file_name, file_extension = os.path.splitext(os.path.basename(input_pdf_file_path))
  output_file_path = f"{os.path.dirname(input_pdf_file_path)}/{file_name}_encrypted{file_extension}"

  return output_file_path

def main():
    input_pdf = select_pdf_file()

    if not input_pdf:
        print("No file selected. Exiting.")
        return

    # Extract file name and extension
    file_name, file_extension = os.path.splitext(os.path.basename(input_pdf))

    # Set the output PDF file path
    output_pdf = get_output_file_path(input_pdf)


    password = get_password()

    if not password:
        print("No password entered. Exiting.")
        return

    add_password(input_pdf, output_pdf, password)

    print(f"PDF encrypted successfully. Encrypted file saved as: {output_pdf}")
    os.startfile(os.path.dirname(output_pdf))

if __name__ == "__main__":
    main()
