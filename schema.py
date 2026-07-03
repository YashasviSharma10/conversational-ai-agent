from typing import Optional

from pydantic import BaseModel, Field


class MyOutput(BaseModel):
    """
    Structured output returned by the LLM.
    """

    step: str = Field(
        ...,
        description="The ID of the step. Example: start, plan, Tool, output."
    )

    content: Optional[str] = Field(
        default=None,
        description="The optional string content for the current step."
    )

    tool: Optional[str] = Field(
        default=None,
        description="The ID of the tool to call."
    )

    input: Optional[str] = Field(
        default=None,
        description="The input parameter for the selected tool."
    )