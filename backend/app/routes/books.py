from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse
from app.db.mongo import books
import shutil
import os
from uuid import uuid4
from bson import ObjectId

router = APIRouter()

UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.get("/all")
def get_all_books():
    all_books = list(books.find({}, {"_id": 0}))
    return all_books

@router.get("/download/{filename}")
def download_book(filename: str):
    filepath = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="Fichier introuvable")
    return FileResponse(path=filepath, filename=filename)

@router.get("/search")
def search_books(
    title: str = "",
    author: str = "",
    category: str = "",
    niveau: str = ""
):
    query = {}

    if title:
        query["title"] = {"$regex": title, "$options": "i"}
    if author:
        query["author"] = {"$regex": author, "$options": "i"}
    if category:
        query["category"] = {"$regex": category, "$options": "i"}
    if niveau:
        query["niveau"] = {"$regex": niveau, "$options": "i"}

    results = list(books.find(query, {"_id": 0}))
    return results

@router.post("/upload")
def upload_book(
    file: UploadFile = File(...),
    title: str = Form(...),
    author: str = Form(...),
    category: str = Form(...),
    isbn: str = Form(""),
    niveau: str = Form(...)
):
    if not file.filename.endswith((".pdf", ".epub")):
        raise HTTPException(status_code=400, detail="Format non supporté")

    filename = f"{uuid4()}_{file.filename}"
    filepath = os.path.join(UPLOAD_DIR, filename)

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    book = {
        "title": title,
        "author": author,
        "category": category,
        "isbn": isbn,
        "niveau": niveau,
        "file_url": filename  # on stocke juste le nom, pas le chemin complet
    }

    result = books.insert_one(book)

    return {
        "message": "Livre ajouté avec succès",
        "book_id": str(result.inserted_id)  # ✅ conversion de l'ObjectId en string
    }