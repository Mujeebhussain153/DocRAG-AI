from dataclasses import dataclass

@dataclass
class TextChunk:
    """
    Represents one chunk of text.
    """
    chunk_number: int
    text: str

class ChunkingService:

    def create_chunks(
            self,
            text:str,
            chunk_size: int = 500,
            overlap: int =100
    ) -> list[TextChunk]:
        
        """
        Split text into overlapping chunks.
        """

        if chunk_size <= 0:
            raise ValueError(
                "Chunk Size must be greater than zero"
            )

        if overlap < 0:
            raise ValueError(
                "overlap cannot be negative."
            )

        if overlap >= chunk_size:
            raise ValueError(
                f"overlap ({overlap}) must be smaller than chunk_size ({chunk_size})."
            )

        chunks = []

        step = chunk_size - overlap

        chunk_number = 1

        for start in range(0, len(text), step):
            chunk_text = text[start: start+ chunk_size]

            if not chunk_text:
                break

            chunks.append(
                TextChunk(
                    chunk_number=chunk_number,
                    text=chunk_text
                )
            )

            chunk_number+=1

        return chunks

