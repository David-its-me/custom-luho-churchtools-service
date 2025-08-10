# Propresenter file system
from propresenter.file_io import pro_file

# Propresenter protobuf
from propresenter.pb_auto_generated.presentation_pb2 import Presentation
from propresenter.pb_auto_generated.action_pb2 import Action
from propresenter.pb_auto_generated.slide_pb2 import Slide
from propresenter.pb_auto_generated.cue_pb2 import Cue
from propresenter.presentation_builder.cue_builder import (
    createCue,
    generate_cue_group_from_cues,
)

##################################
### CONFIG
##################################
slide_duration = 10.0
##################################


def __get_default_slides() -> list[Slide]:
    presentation: Presentation = pro_file.read(
        "Vorlagen", "Announcement_Standard_Folien"
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

def add_slides(presentation: Presentation) -> Presentation:
    print("Füge Standard Folien hinzu ...")
    print()
    cues: list[Cue] = []
    for slide in __get_default_slides():
        cue = createCue(slide, completion_time=slide_duration)
        cues.append(cue)
        presentation.cues.append(cue)

    presentation.cue_groups.append(
        generate_cue_group_from_cues(cues, label="Bibliothek/Vorlagen/Announcement_Standard_Folien")
    )
    return presentation
