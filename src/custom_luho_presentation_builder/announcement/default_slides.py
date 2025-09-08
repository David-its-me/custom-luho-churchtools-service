# Propresenter file system
from propresenter.file_io import pro_file

# Propresenter protobuf
from propresenter.pb_auto_generated.presentation_pb2 import Presentation
from propresenter.pb_auto_generated.action_pb2 import Action
from propresenter.pb_auto_generated.slide_pb2 import Slide
from propresenter.pb_auto_generated.cue_pb2 import Cue
from propresenter.presentation_builder.cue import (
    createCue,
    generate_cue_group_from_cues,
)
from propresenter.presentation_builder.cue_actions.macro import create_announcement_macro


def __get_default_slides(
    propresenter_library_name: str, default_slides_presentation_name: str
) -> list[Slide]:
    presentation: Presentation = pro_file.read(
        propresenter_library_name, 
        default_slides_presentation_name
    )
    slides = []
    for cue in presentation.cues:
        # Find base slide actions
        action_base_slides = list(
            filter(
                lambda action: action.type
                == Action.ActionType.ACTION_TYPE_PRESENTATION_SLIDE,
                cue.actions,
            )
        )
        if len(action_base_slides) > 0:
            slides.append(action_base_slides[0].slide.presentation.base_slide)

    return slides


def create(
    presentation: Presentation,
    slide_duration: float,
    propresenter_library_name: str,
    default_slides_presentation_name: str,
) -> Presentation:
    print("Füge Standard Folien hinzu ...")
    print()
    cues: list[Cue] = []
    for slide in __get_default_slides(
        propresenter_library_name, default_slides_presentation_name
    ):
        cue = createCue(slide, actions=[create_announcement_macro()], completion_time=slide_duration)
        cues.append(cue)
        presentation.cues.append(cue)

    presentation.cue_groups.append(
        generate_cue_group_from_cues(
            cues, label="Bibliothek/{}/{}".format(propresenter_library_name, default_slides_presentation_name)
        )
    )
    return presentation
