

from propresenter.pb_auto_generated.basicTypes_pb2 import URL
from propresenter.pb_auto_generated.graphicsData_pb2 import Graphics, Media
from propresenter.pb_auto_generated.slide_pb2 import Slide
from propresenter.presentation_builder.slide_element.rectangle import empty_rectangle
from propresenter.presentation_builder.uuid_generator import generate_random_uuid


def image(
    image_path: str,
    # Default bounds is a full HD slide
    bounds: Graphics.Rect = Graphics.Rect(
        origin=Graphics.Point(
            x=0,
            y=0,
        ),
        size=Graphics.Size(
            width=1920,
            height=1080,
        ),
    ),
) -> Slide.Element:
    format = None
    if "." in image_path:
        format = image_path.split(".")[1]

    element = empty_rectangle(bounds)
    element.element.fill.CopyFrom(
        Graphics.Fill(
            enable=True,
            media=Media(
                uuid=generate_random_uuid(),
                url=URL(
                    local=URL.LocalRelativePath(
                        root=URL.LocalRelativePath.Root.ROOT_SHOW,
                        path=image_path,
                    ),
                    platform=URL.Platform.PLATFORM_UNKNOWN,
                ),
                metadata=Media.Metadata(
                    format=format,
                ),
                image=Media.ImageTypeProperties(
                    drawing=Media.DrawingProperties(
                        custom_image_bounds=Graphics.Rect(
                            origin=Graphics.Point(
                                x=0.0,
                                y=0.0,
                            ),
                            size=Graphics.Size(
                                width=1920,
                                height=1080,
                            ),
                        )
                    )
                ),
            ),
        ),
    ),
    return element