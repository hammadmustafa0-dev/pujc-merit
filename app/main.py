from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware

import pandas as pd
from app.data_loader import search_by_name

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger=logging.getLogger(__name__)




app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/search")
def search(name:str , merit_list):

    try:
        result=search_by_name(name,merit_list)

    except Exception as e:
        logger.error(f"error is: {e}")
    

    return result



@app.get("/health")
def health():
    return {"status":"ok"}


