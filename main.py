# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 19:44:42 2022

@author: Alex
"""

from typing import Optional
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from flask import request
import json
db = []

class Item(BaseModel):
    data: dict
    epoch: int



app = FastAPI()


@app.post("/publish/epoch/end")
async def create_item(item: Item):

    db.append(item)
    #return item
    

@app.get("/publish/epoch/end")
async def get_item():
    return db