from propresenter.pb_auto_generated.presentation_pb2 import Presentation
from propresenter.pb_auto_generated.basicTypes_pb2 import Color, UUID
from propresenter.pb_auto_generated.background_pb2 import Background
from propresenter.pb_auto_generated.basicTypes_pb2 import ApplicationInfo
from propresenter.presentation_builder.uuid_builder import generate_random_uuid


def create_empty_presentation() -> Presentation:
    presentation = Presentation(
        application_info=ApplicationInfo(
            application=ApplicationInfo.Application.APPLICATION_UNDEFINED,
            platform=ApplicationInfo.Platform.PLATFORM_UNDEFINED,
        ),
        background=Background(color=Color(red=1, green=1, blue=1, alpha=0)),
        content_destination=Presentation.ContentDestination.CONTENT_DESTINATION_GLOBAL,
        uuid=generate_random_uuid()
    )
    return presentation
