import pandas as pd
from PyPDF2 import PdfReader
from fastapi import UploadFile
import io

def read_file_content(file: UploadFile) -> str:
    """
    Reads the content of a file based on its content type.

    Args:
        file (UploadFile): The file to be read.

    Returns:
        str: The content of the file as a string.

    Raises:
        ValueError: If the file type is unsupported.
    """
    if file.content_type == "application/pdf":
        return read_pdf_content(file)
    elif file.content_type in ["text/csv", "application/vnd.ms-excel",
                               "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"]:
        return read_csv_or_excel_content(file)
    elif file.content_type == "text/plain":
        return read_txt_content(file)
    else:
        raise ValueError("Unsupported file type")

def read_pdf_content(file: UploadFile) -> str:
    """
    Reads the content of a PDF file.

    Args:
        file (UploadFile): The PDF file to be read.

    Returns:
        str: The text content of the first page of the PDF.
    """
    pdf_reader = PdfReader(io.BytesIO(file.file.read()))
    first_page = pdf_reader.pages[0]
    return first_page.extract_text()

def read_csv_or_excel_content(file: UploadFile) -> str:
    """
    Reads the content of a CSV or Excel file.

    Args:
        file (UploadFile): The CSV or Excel file to be read.

    Returns:
        str: The content of the file as a string representation of the first few rows.
    """
    if file.content_type == "text/csv":
        df = pd.read_csv(io.BytesIO(file.file.read()))
    else:
        df = pd.read_excel(io.BytesIO(file.file.read()))
    return df.head().to_string()

def read_txt_content(file: UploadFile) -> str:
    """
    Reads the content of a text file.

    Args:
        file (UploadFile): The text file to be read.

    Returns:
        str: The content of the text file as a string.
    """
    content = file.file.read()
    return content.decode('utf-8')