from pydantic import BaseModel

class IngestResponse(BaseModel):
    message: str

class AskRequest(BaseModel):
    question: str

class AskResponse(BaseModel):
    response: str
    sources: list
