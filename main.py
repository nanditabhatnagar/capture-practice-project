from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional
import os, sys

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

#this function sorts a list of folders in ascending order, depending on how many files are in each folder
def sort_files(barcodeList, file_count):
    bigPicture = zip(barcodeList, file_count)
    bigPicture = list(bigPicture)
    barcodeList = sorted(bigPicture, key = lambda x: x[1]) 
    barcodeList = list(zip(*barcodeList))
    return list(barcodeList[0])

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
async def read_item(request: Request, sortingby: Optional[str] = None):
    #if the user wants to sort the index by the number of images per barcode folder in ascending order
    if sortingby == 'numfilesasc': 
        barcodeList = []
        file_count = []
        for x in os.listdir('./static/small'):
            barcodeList.append(x)
            path = f"./static/small/{x}"
            file_counter = len(os.listdir(path)) #counting no. of files in each folder
            file_count.append(file_counter)
        barcodeList = sort_files(barcodeList, file_count)
        return templates.TemplateResponse("index.html", {"request": request, "barcodeList": barcodeList})
    
    #if the user wants to sort the index by the number of images per barcode folder in descending order
    if sortingby == 'numfilesdesc': 
        barcodeList = []
        file_count = []
        for x in os.listdir('./static/small'):
            barcodeList.append(x)
            path = f"./static/small/{x}"
            file_counter = len(os.listdir(path)) #counting no. of files in each folder
            file_count.append(file_counter)
        barcodeList = sort_files(barcodeList, file_count)
        barcodeList.reverse()
        return templates.TemplateResponse("index.html", {"request": request, "barcodeList": barcodeList})
    
    #if the user wants to sort the index by barcode number in descending order
    if sortingby == 'barcodedesc': 
        barcodeList = []
        file_count = []
        for x in os.listdir('./static/small'):
            barcodeList.append(x)
            barcodeList.sort(key = int)
        barcodeList.reverse()
        return templates.TemplateResponse("index.html", {"request": request, "barcodeList": barcodeList})
    
    #default option: the user wants to sort the index by barcode number in ascending order
    barcodeList = []
    file_count = []
    for x in os.listdir('./static/small'):
        barcodeList.append(x)
        barcodeList.sort(key = int)   
    return templates.TemplateResponse("index.html", {"request": request, "barcodeList": barcodeList})