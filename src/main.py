from typing import Union
from client.ct_posts_client import CTPostsClient
from client.ct_calendar_client import CTCalendarClient
from client.ct_event_client import CTEventClient
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from services.date_data_service import DateDataService
from starlette.responses import FileResponse
from services.calendar_manager import CalendarManager
from pydantic import BaseModel

app = FastAPI()
ct_calendar_client: CTCalendarClient = CTCalendarClient()
ct_event_client: CTEventClient = CTEventClient()
ct_posts_client: CTPostsClient = CTPostsClient()


calendar_manager: CalendarManager = CalendarManager(ct_calendar_client=ct_calendar_client)
date_service: DateDataService = DateDataService(
    ct_calendar_client=ct_calendar_client, 
    ct_event_client=ct_event_client, 
    calendar_manager=calendar_manager)

@app.on_event("startup")
async def startup_event() -> None:
    """tasks to do at server startup"""
    # Poll once in the beginning, which takes a bit longer. After that the values are cached for 1 hours
    try: # If a problem occours the try catch clause ensures, that the whole server is still able to start.
        ct_posts_client.load_posts()
        date_service.get_upcomming_date(0) 
    except:
        pass
    

@app.get("/")
def read_root():
    return read_static_content(asset_type="html", path="main.html")

@app.get("/slide/upcommingEvents/{slideCount}")
def read_root():
    return read_static_content(asset_type="html", path="main.html")

@app.get("/static/{asset_type}/{path}")
def read_static_content(asset_type: str, path: str):
    return FileResponse("../static/{}/{}".format(asset_type, path))

@app.get("/html/{path}")
def read_html(path: str):
    return read_static_content(asset_type="html", path=path)

@app.get("/icons/{path}")
def read_html(path: str):
    return read_static_content(asset_type="icons", path=path)

@app.get("/script/{path}")
def read_script(path: str):
    return read_static_content(asset_type="script", path=path)

@app.get("/css/{path}")
def read_css(path: str):
    return read_static_content(asset_type="css", path=path)

@app.get("/date/upcomming/{nextUpcomming}")
def get_event(nextUpcomming: int):
    return date_service.get_upcomming_date(nextUpcomming)



@app.get("/test")
def test():
    return ct_posts_client.load_posts()

@app.get("/test2")
def test2():
    return DateDataService._tag_rule({"descriptionSequence": ["<biblicalBook>", "<#1>"], "replacement": ["<biblicalBook>", " <#1>"]})
    
@app.get("/testimage")
def testimage():
    return ct_posts_client.load_image(ct_posts_client.load_posts()["images"][0])

class Visibility(BaseModel):
    visible: bool


@app.get("/calendar/{id}/visible")
def get_calendar_visibility(id: int):
    return {"visible": calendar_manager.is_calendar_visible(id)}


@app.post("/calendar/{id}/visible")
def set_calendar_visibility(id: int, visibility_data: Visibility):
    return calendar_manager.set_calendar_visibility(id = id, visible=visibility_data.visible)

