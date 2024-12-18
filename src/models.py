from typing import List
from pydantic import BaseModel, Field


class Fact(BaseModel):
    """A statement that is supported by evidence from a reliable source."""

    sources: List[str] = Field(
        description="A list of excerpts from the content that support the fact."
    )
    statement: str = Field(description="The fact inferred from the list of excerpts.")
