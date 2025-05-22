from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class FolderBase(BaseModel):
    name: str

class FolderCreate(FolderBase):
    pass

class FolderOut(FolderBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class NoteBase(BaseModel):
    title: str
    content: Optional[str] = ""

class NoteCreate(NoteBase):
    folder_id: int

class NoteOut(NoteBase):
    id: int
    created_at: datetime
    updated_at: datetime
    folder_id: int

    model_config = ConfigDict(from_attributes=True)
