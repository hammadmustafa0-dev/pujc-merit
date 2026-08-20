

import pandas as pd
from app.data_loader import search_by_name

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger=logging.getLogger(__name__)

from fastapi import FastAPI,HTTPException,Request
from fastapi.middleware.cors import CORSMiddleware


from slowapi import Limiter,_rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter=Limiter(key_func=get_remote_address)


app=FastAPI()

app.state.limiter=limiter
app.add_exception_handler(RateLimitExceeded,_rate_limit_exceeded_handler)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/search")
@limiter.limit("20/minute")
def search(name:str , merit_list , request:Request):

    try:
        result=search_by_name(name,merit_list)

    except Exception as e:
        logger.error(f"error is: {e}")
        raise HTTPException(status_code=400,detail="something went wrong! Try again")
    

    return result



@app.get("/health")
def health():
    return {"status":"ok"}


