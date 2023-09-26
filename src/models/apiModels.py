from pydantic import BaseModel
from typing import List

class attachment(BaseModel):
    fileName: str
    content: str

class PutJiraTicket(BaseModel):
    title: str
    description: str
    attachment: List[attachment]