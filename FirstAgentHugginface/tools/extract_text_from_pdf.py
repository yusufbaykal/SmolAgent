from PyPDF2 import PdfReader
from smolagents.tools import Tool

class ExtractTextFromPdfTool(Tool):
    name = "extract_text_from_pdf"
    description = "Extracts text from a PDF file given its path."
    inputs = {'pdf_path': {'type': 'string', 'description': 'The path to the PDF file.'}}
    output_type = "string"

    def forward(self, pdf_path: str) -> str:
        try:
            reader = PdfReader(pdf_path)
            extracted_text = ""
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    extracted_text += text + "\n"
            if not extracted_text:
                return "No text could be extracted from the PDF."
            return extracted_text.strip()
        except Exception as e:
            return f"An error occurred while extracting text: {e}"

    def __init__(self, *args, **kwargs):
        self.is_initialized = False