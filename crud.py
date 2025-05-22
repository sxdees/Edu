from sqlalchemy.orm import Session

from app.models import Folder, Note
from app.schemas import FolderCreate, NoteCreate

# Folders
def create_folder(db: Session, folder: FolderCreate):
    db_folder = Folder(name=folder.name)
    db.add(db_folder)
    db.commit()
    db.refresh(db_folder)
    return db_folder

def get_folders(db: Session):
    return db.query(Folder).all()

def delete_folder(db: Session, folder_id: int):
    folder = db.query(Folder).get(folder_id)
    if folder:
        db.delete(folder)
        db.commit()

def update_folder(db: Session, folder_id: int, name: str):
    folder = db.query(Folder).get(folder_id)
    if folder:
        folder.name = name
        db.commit()
        db.refresh(folder)
    return folder

# Notes
def create_note(db: Session, note: NoteCreate):
    db_note = Note(**note.dict())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def delete_note(db: Session, note_id: int):
    note = db.query(Note).get(note_id)
    if note:
        db.delete(note)
        db.commit()

def delete_all_notes(db: Session):
    db.query(Note).delete()
    db.commit()

def update_note_content(db: Session, note_id: int, content: str):
    note = db.query(Note).get(note_id)
    if note:
        note.content = content
        db.commit()
        db.refresh(note)
    return note

def get_notes(db: Session):
    return db.query(Note).all()