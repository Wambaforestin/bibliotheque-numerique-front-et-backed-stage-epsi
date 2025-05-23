from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, books

app = FastAPI(title="Bibliothèque Auth")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(books.router, prefix="/books", tags=["Books"])
