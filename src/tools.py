import json
from typing import Literal
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from src.models import Fact


# NOTE: Toy implementation.
def extract(
    section: Literal[
        "abstract",
        "introduction",
        "related_work",
        "approach",
        "dataset",
        "experiments",
        "results",
        "conclusion",
    ]
):
    """Extract content from a section of the paper"""

    with open("data/paper.json") as f:
        paper = json.load(f)

    if section in paper:
        return paper[section]["content"]
    else:
        return "Section not found."


# TODO: Implement synthesize function.
def synthesize(content: str):
    """Generate a summary from the given content."""
    pass


def infer(content: str):
    """Infer a single fact from the given content."""

    llm = ChatOpenAI(temperature=0, model="gpt-4o")

    structured_llm = llm.with_structured_output(Fact)

    system = """
    You are a helpful assistant tasked with inferring a single fact from the given content.
    Avoid speculation or opinion.

    Content: {input}
    """

    prompt = ChatPromptTemplate.from_template(system)
    chain = prompt | structured_llm

    fact = chain.invoke(input=content)

    return fact
