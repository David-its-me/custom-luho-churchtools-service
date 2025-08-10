from churchtools.ct_client.ct_api_client import CTApiClient
import json

from churchtools.ct_data_model.post.ct_posts import CTPosts
from propresenter.pb_auto_generated.presentation_pb2 import Presentation

from custom_luho_presentation_builder.announcement.announcement_presentation import create_announcement_presentation
from propresenter.presentation_builder.slide_builder import create_slide_with_random_background_color
from propresenter.presentation_builder.presentation_builder import create_empty_presentation

# Who am I
# print(json.dumps(ct_api_client.who_am_i(), indent=4))

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

#print("////////////////////////////////////////")

#print(presentation.cues[0].actions[0].slide.presentation.transition)
#print(dir(presentation.cues[0].actions[0].slide.presentation))
#new_presentation.cues.append(createCueWith(create_slide()))
#print(new_presentation.cues[0])
#print(presentation.cue_groups)
#print(presentation.cues[0].uuid)

new_presentation = create_announcement_presentation()
