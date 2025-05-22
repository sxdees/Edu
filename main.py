from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal, init_db
from app import crud, schemas

app = FastAPI()

init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Folder Handlers
@app.post("/folders/", response_model=schemas.FolderOut)
def create_folder(folder: schemas.FolderCreate, db: Session = Depends(get_db)):
    return crud.create_folder(db, folder)

@app.get("/folders/", response_model=list[schemas.FolderOut])
def list_folders(db: Session = Depends(get_db)):
    return crud.get_folders(db)

@app.delete("/folders/{folder_id}")
def delete_folder(folder_id: int, db: Session = Depends(get_db)):
    crud.delete_folder(db, folder_id)
    return {"message": "Folder and its notes deleted."}

@app.put("/folders/{folder_id}", response_model=schemas.FolderOut)
def update_folder(folder_id: int, folder: schemas.FolderCreate, db: Session = Depends(get_db)):
    updated = crud.update_folder(db, folder_id, folder.name)
    if not updated:
        raise HTTPException(status_code=404, detail="Folder not found")
    return updated

# Note Handlers
@app.post("/notes/", response_model=schemas.NoteOut)
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    return crud.create_note(db, note)

@app.delete("/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    crud.delete_note(db, note_id)
    return {"message": "Note deleted."}

@app.delete("/notes/")
def delete_all_notes(db: Session = Depends(get_db)):
    crud.delete_all_notes(db)
    return {"message": "All notes deleted."}

@app.put("/notes/{note_id}/content", response_model=schemas.NoteOut)
def update_note_content(note_id: int, content: str, db: Session = Depends(get_db)):
    updated = crud.update_note_content(db, note_id, content)
    if not updated:
        raise HTTPException(status_code=404, detail="Note not found")
    return updated

@app.get("/notes/", response_model=list[schemas.NoteOut])
def get_notes(db: Session = Depends(get_db)):
    return crud.get_notes(db)