from churchtools.ct_client.ct_api_client import CTApiClient
from churchtools.ct_client.ct_posts_fetcher import CTPostsFetcher
import json

from churchtools.ct_data_model.post.ct_posts import CTPosts
from propresenter.file_io import pro_file
from propresenter.pb_auto_generated import presentation_pb2

from custom_luho_presentation_builder.announcement import create_announcement_presentation
from propresenter.presentation_builder.slide_builder import create_random_background_color_slide
from propresenter.presentation_builder.presentation_builder import create_empty_presentation


ct_api_client = CTApiClient()

# Login into the api
ct_api_client.open_connection()

# Who am I
# print(json.dumps(ct_api_client.who_am_i(), indent=4))

ct_posts_client = CTPostsFetcher(
    ct_api_client.get_domain_base_path(), ct_api_client.get_session()
)

# Fetch Posts
print("Lade Beiträge von Churtools...")
print()
posts = CTPosts(ct_posts_client.fetch_posts_list())


print(json.dumps(ct_posts_client.fetch_posts_list(), indent=4))

presentation: presentation_pb2.Presentation = pro_file.read("Vorlagen", "Announcements")
# print(presentation.content_destination)
#print(presentation.name)

# cue === Folien
#print(len(presentation.cues))
#print(dir(presentation.cues[0]))

# action
#print(len(presentation.cues[0].actions))
# Slide ACTION_TYPE_PRESENTATION_SLIDE
#print(presentation.cues[0].actions[0])
# Announcement Makro ACTION_TYPE_MACRO
#print(presentation.cues[0].actions[1])

# rv.data.Action.SlideType
# nur verfügbar mit ACTION_TYPE_PRESENTATION_SLIDE
#print(presentation.cues[0].actions[0].slide)

# slide == oneof PresentationSlide | PropSlide

# presentation typ PresentationSlide
#print(presentation.cues[0].actions[0].slide.presentation)
# base_slide typ Slide
# print(presentation.cues[0].actions[0].slide.presentation.base_slide.elements[0])
#presentation.cues[0].actions[0].slide.presentation.base_slide.CopyFrom(create_random_background_color_slide())
#print(dir(presentation.cues[0].actions[0].slide.presentation.base_slide))

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

presentation.name =  "Test"

#print("////////////////////////////////////////")

#print(presentation.cues[0].actions[0].slide.presentation.transition)
#print(dir(presentation.cues[0].actions[0].slide.presentation))
#new_presentation.cues.append(createCueWith(create_slide()))
#print(new_presentation.cues[0])
#print(presentation.cue_groups)
#print(presentation.cues[0].uuid)

new_presentation = create_announcement_presentation(posts, ct_api_client)

pro_file.write(
    "Vorlagen",
    "Test",
    presentation,
)
pro_file.write(
    "Vorlagen",
    "Announcements_generated",
    new_presentation,
)
