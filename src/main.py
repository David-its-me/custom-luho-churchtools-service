from churchtools.ct_client.ct_api_client import CTApiClient
from churchtools.ct_client.ct_posts_client import CTPostsClient
import json

from churchtools.ct_data_model.post.ct_posts import CTPosts
from propresenter.pro_file_io import pro_file
import presentation_pb2

import propresenter.pro_file_builder.pro_slide_builder as slide_builder

ct_api_client = CTApiClient()

# Login into the api
ct_api_client.open_connection()

# Who am I
# print(json.dumps(ct_api_client.who_am_i(), indent=4))

ct_posts_service = CTPostsClient(
    ct_api_client.get_domain_base_path(), ct_api_client.get_session()
)

# Fetch Posts
posts = CTPosts(ct_posts_service.fetch_posts_list())
print(posts.get_image_urls())

presentation: presentation_pb2.Presentation = pro_file.read("Vorlagen", "Announcements")
# print(presentation.content_destination)
print(presentation.name)

# cue === Folien
print(len(presentation.cues))
print(dir(presentation.cues[0]))

# action
print(len(presentation.cues[0].actions))
# Slide ACTION_TYPE_PRESENTATION_SLIDE
print(presentation.cues[0].actions[0])
# Announcement Makro ACTION_TYPE_MACRO
print(presentation.cues[0].actions[1])

# rv.data.Action.SlideType
# nur verfügbar mit ACTION_TYPE_PRESENTATION_SLIDE
print(presentation.cues[0].actions[0].slide)

# slide == oneof PresentationSlide | PropSlide

# presentation typ PresentationSlide
print(presentation.cues[0].actions[0].slide.presentation)
# base_slide typ Slide
print(presentation.cues[0].actions[0].slide.presentation.base_slide)
presentation.cues[0].actions[0].slide.presentation.base_slide.CopyFrom(slide_builder.create_slide())
print(dir(presentation.cues[0].actions[0].slide.presentation.base_slide))

#print(dir(presentation.cues[0].actions[0].slide.presentation.base_slide.elements[0]))
'''
print(
    dir(
        presentation.cues[0]
        .actions[0]
        .slide.presentation.base_slide.elements[0]
        .element
    )
)
'''

presentation.name =  "Announcements_generated"

pro_file.write(
    "Vorlagen",
    "Announcements_generated",
    presentation,
)
