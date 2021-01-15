from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os, sys

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/barcodes/{barcode}", response_class=HTMLResponse)
async def read_item(request: Request, barcode: str):
    return templates.TemplateResponse("barcode.html", {"request": request, "barcode": barcode})

@app.get("/index/", response_class=HTMLResponse)
async def read_item(request: Request):
    barcodeList = []
    for x in os.listdir('./static/small'):
        barcodeList.append(x)
    return templates.TemplateResponse("index.html", {"request": request, "barcodeList": barcodeList})

@app.get("/loop", response_class=HTMLResponse)
async def loop(request: Request):
    stuff = [i**2 for i in range(1000)]
    return templates.TemplateResponse("loop.html", {"request": request, "stuff": stuff})