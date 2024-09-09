from service.openai_service import OpenAIService
from utils.file_reader import read_file_content
from fastapi import UploadFile


def document_search(file: UploadFile, question: str) -> str:
    """
    Searches the content of a document for answers to a given question.

    Args:
        file (UploadFile): The file to be read and searched.
        question (str): The question to query against the document content.

    Returns:
        str: The response from the OpenAI service based on the document content and question.
    """
    # Read the content of the file
    content = read_file_content(file)

    # Prepare messages for OpenAI
    messages = [
        {"role": "system", "content": "You are an AI assistant created to help users query data from documents."},
        {"role": "user", "content": f"This is the document data: {content}"},
        {"role": "user", "content": question}
    ]

    # Initialize the OpenAI service
    openai_service = OpenAIService()

    # Get the chat completion response from OpenAI
    return openai_service.get_chat_completion(messages)
