from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static/small", StaticFiles(directory="static/small"), name="small")

templates = Jinja2Templates(directory="templates")

@app.get("/barcodes/{barcode}", response_class=HTMLResponse)
async def read_item(request: Request, barcode: str):
    return templates.TemplateResponse("barcodes.html", {"request": request, "barcode": barcode})