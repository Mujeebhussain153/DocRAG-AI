from pathlib import Path
from app.schemas.document import ExtractedDocument, ExtractedPage
import fitz

class PDFService:
    """
    Responsible for extracting text from PDF files.
    """

    def extract_text(
            self,
            pdf_path: Path,
    ) -> ExtractedDocument:
        """
        Extract all text from a PDF.
        """
        document = fitz.open(pdf_path)

        try:
            pages = []
            contains_text = False

            for idx, page in enumerate(document):
                page_text = page.get_text()
                pages.append(
                    ExtractedPage(
                        page_number=idx,
                        text=page_text,
                        contains_text=bool(page_text.strip()) 
                    )
                )

            return ExtractedDocument(
                text="\n".join(pages),
                page_count=len(pages),
                contains_text=contains_text
            )
        
        finally:
            document.close()
        