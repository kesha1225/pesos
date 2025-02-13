from fastapi import FastAPI
from fastapi.responses import FileResponse, Response
import os

from starlette.status import HTTP_404_NOT_FOUND

app = FastAPI(redoc_url=None, docs_url=None)

PDF_FOLDER = "static"

@app.get("/pesos.pdf")
async def get_pdf():
    file_path = os.path.join(PDF_FOLDER, "whitepaper.pdf")
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="application/pdf", headers={"Content-Disposition": "inline"})
    
    return Response(status_code=HTTP_404_NOT_FOUND)