import json
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

__all__ = ("api", "views", "utils")

_dirname = Path(__file__).parent.absolute()

api = FastAPI(
    name="Suicide Prevention Hotlink",
    description="This app serves as a redirect to your national suicide prevention helpline through GeoIP",
    redoc_url=None,
)

api.mount("/static", StaticFiles(directory=_dirname / "static"), name="static")

api.templates = Jinja2Templates(directory=_dirname / "templates")

api.hotlines = json.loads((_dirname / "countries.json").read_text())

from app import views, utils

del _dirname, json, FastAPI, StaticFiles, Jinja2Templates, Path
