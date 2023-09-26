from pydantic import BaseModel
from typing import List

# model can act as interfaces that can be used to define types at various places

class attachment(BaseModel):
    fileName: str
    content: str

class PutJiraTicket(BaseModel):
    title: str
    description: str
    attachment: List[attachment]