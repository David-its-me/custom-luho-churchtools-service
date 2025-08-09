# Churchtools API Client
from churchtools.ct_client.ct_api_client import CTApiClient

# Propresenter file system
from propresenter.file_io import pro_file

# Propresenter protobuf
from propresenter.pb_auto_generated.presentation_pb2 import Presentation
from propresenter.presentation_builder.presentation_builder import (
    create_empty_presentation,
)
from propresenter.presentation_builder.transition_builder import cube_transition

import custom_luho_presentation_builder.announcement.churchtools_posts as churchtools_posts
import custom_luho_presentation_builder.announcement.default_slides as default_slides
import custom_luho_presentation_builder.announcement.churchtools_dates as churchtools_dates

##################################
### CONFIG
##################################
slide_duration = 10.0
transition_duration = 1.0
post_not_older_than_weeks = 26
##################################



def __create_empty_announcement_base_presentation() -> Presentation:
    presentation: Presentation = create_empty_presentation()
    # Configure the loop transition
    presentation.transition.CopyFrom(
        cube_transition(transition_duration=transition_duration)
    )
    presentation.slide_show_duration = slide_duration
    presentation.timeline.CopyFrom(
        Presentation.Timeline(
            loop=True, duration=(slide_duration - transition_duration)
        )
    ),
    return presentation


def create_announcement_presentation(ct_api_client: CTApiClient) -> Presentation:
    print("Erstelle Announcement Präsentation:")
    print()

    presentation = __create_empty_announcement_base_presentation()
    presentation = churchtools_posts.add_slides(presentation, ct_api_client)
    presentation = default_slides.add_slides(presentation)
    presentation = churchtools_dates.add_slides(presentation)

    print("Speichere Announcement Präsentation")
    print()
    pro_file.write(
        "Vorlagen",
        "Announcements_generated",
        presentation,
    )
    return presentation
