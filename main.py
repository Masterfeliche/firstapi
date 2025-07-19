from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def greet(request: Request):
       return templates.TemplateResponse(
        request=request, name="index.html", context={"id": id}
    )
@app.get("/about")
async def about_me():
    return {
        "name": "Feliche",
        "age": 20,
        "Hobby": "Sports",
        "Team": "Real Madrid",
        "contacts": ["feliche@gmail.com", "0712748364"]
    }








