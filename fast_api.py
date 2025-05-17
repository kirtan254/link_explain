# app.py

from fastapi import FastAPI
from pydantic import BaseModel
from process import explain_link
from fastapi.responses import FileResponse
import uuid

app = FastAPI()

class URLRequest(BaseModel):
    url: str

@app.post("/explain", response_class=FileResponse)
def explain_url(request: URLRequest):
    # Generate explanation
    explanation = explain_link(request.url)

    # Generate a unique filename
    filename = f"explanation_{uuid.uuid4().hex}.txt"
    
    # Save to file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(explanation)

    # Return the file as a downloadable response
    return FileResponse(
        path=filename,
        filename=filename,
        media_type="text/plain"
    )
