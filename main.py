from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os, sys

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

#root endpoint
@app.get("/")
async def read_item(request: Request):
    return templates.TemplateResponse("root.html", {"request": request})

@app.get("/barcodes/{barcode}", response_class=HTMLResponse)
async def read_item(request: Request, barcode: str):
    imagePath = []
    imageName = []
    imageSize = []
    path = f"./static/small/{barcode}"
    for img in os.listdir(path):
        imagePath.append(f"/small/{barcode}/{img}")
        imageName.append(img)
        imageSize.append(round(os.path.getsize(f"{path}/{img}")/1000, 1)) # converts to kB and rounds the file size to 1dp
    imageDetails = zip(imagePath, imageName, imageSize)
    return templates.TemplateResponse("barcode.html", {"request": request, "barcode" : barcode, "imageDetails": imageDetails})

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