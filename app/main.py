#!/usr/bin/env python
# coding: utf-8

# uvicorn main:app -> pour lancer l'API

from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=["Home"])
def get_root() -> dict:
    return {
        "message": "API de detection des TAGS StackOverFlow :"
    }