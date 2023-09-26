from pydantic import BaseModel
from typing import List, Union

# model can act as interfaces that can be used to define types at various places

class Attachment(BaseModel):
    fileName: str
    content: str

class PutJiraTicket(BaseModel):
    title: str
    description: str
    attachment: List[Attachment] = []