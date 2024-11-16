import json
from typing import Union
from client.ct_posts_client import CTPostsClient
from client.ct_calendar_client import CTCalendarClient
from client.ct_event_client import CTEventClient
from fastapi import FastAPI
from fastapi.responses import Response, HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from service.calendar_manager import CalendarManager
from service.date_data_service import DateDataService
from service.posts_selection_service import PostSelectionService
from pydantic import BaseModel

app = FastAPI()
ct_calendar_client: CTCalendarClient = CTCalendarClient()
ct_event_client: CTEventClient = CTEventClient()
ct_posts_client: CTPostsClient = CTPostsClient()
current_slide_count: int = 0
numberOfCalendarSlides: int = 6


calendar_manager: CalendarManager = CalendarManager(ct_calendar_client=ct_calendar_client)
date_service: DateDataService = DateDataService(
    ct_calendar_client=ct_calendar_client, 
    ct_event_client=ct_event_client, 
    calendar_manager=calendar_manager)
posts_service: PostSelectionService = PostSelectionService(ct_posts_client)

@app.on_event("startup")
async def startup_event() -> None:
    """tasks to do at server startup"""
    # Poll once in the beginning, which takes a bit longer. After that the values are cached for 1 hours
    try: # If a problem occours the try catch clause ensures, that the whole server is still able to start.
        date_service.get_upcomming_date(0) 
    except:
        pass
    
@app.get("/")
def read_root():
    return read_static_content(asset_type="html", path="main.html")

@app.get("/slide/upcommingEvents/{slideCount}")
def read_root():
    return read_static_content(asset_type="html", path="main.html")

@app.get("/slide/post/{post_id}")
def get_post_slide(post_id: str):
    postData = posts_service.getData(postId=post_id)
    if postData['content'] is None:  
        return read_static_content(asset_type="html", path="announcement_fullscreen.html")
    elif len(postData['content']) < 3:
        return read_static_content(asset_type="html", path="announcement_fullscreen.html")
    elif len(postData['images']) == 1:
        return read_static_content(asset_type="html", path="announcement_one_image.html")
    else: #len(postData['images']) == 2:
        return read_static_content(asset_type="html", path="announcmenet_two_images.html")


@app.get("/slide/next/{propresenterSlideNumber}")
def get_next_Slide():
    visibleIds = posts_service.getAllVisiblePostIds()
    global current_slide_count
    global numberOfCalendarSlides
    current_slide_count = (current_slide_count + 1) % (len(visibleIds) + numberOfCalendarSlides)
    if len(visibleIds) > current_slide_count:
        return RedirectResponse("/slide/post/{}".format(visibleIds[current_slide_count]))    
    
    else:
        return RedirectResponse("/slide/upcommingEvents/{}".format(current_slide_count - len(visibleIds) + 1))
    

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

    
@app.get("/post/image/{postId}",
        responses = {
            200: {
                "content": {"image/png": {}}
            }
        },
        response_class=Response
    )
def get_post_image(postId: str):
    return Response(content=posts_service.getImage(postId=postId), media_type="image/png")


@app.get("/post/data/{postId}")
def get_post_title(postId: str):
    return posts_service.getData(postId=postId)




class Visibility(BaseModel):
    visible: bool


@app.get("/calendar/{id}/visible")
def get_calendar_visibility(id: int):
    return {"visible": calendar_manager.is_calendar_visible(id)}


@app.post("/calendar/{id}/visible")
def set_calendar_visibility(id: int, visibility_data: Visibility):
    return calendar_manager.set_calendar_visibility(id = id, visible=visibility_data.visible)

