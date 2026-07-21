from enum import Enum

class DocumentStatus(str, Enum):
    """
    Represents the lifecycle of a document.
    """

    UPLOADED = "UPLOADED"

    PARSING = "PARSING"

    CHUNKING = "CHUNKING"

    EMBEDDING = "EMBEDDING"

    INDEXED = "INDEXED"

    FAILED = "FAILED"
