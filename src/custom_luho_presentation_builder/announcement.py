# Churchtools API Client
from churchtools.ct_client.ct_api_client import CTApiClient
from churchtools.ct_client.ct_image_fetcher import CTImageFetcher

# Churchtools data model
from churchtools.ct_data_model.post.ct_posts import CTPosts, CTPost

# Propresenter assets
from propresenter.file_io import pro_assets

# Propresenter protobuf
from propresenter.pb_auto_generated.presentation_pb2 import Presentation
from propresenter.pb_auto_generated.slide_pb2 import Slide
from propresenter.presentation_builder.presentation_builder import create_empty_presentation
from propresenter.presentation_builder.transition_builder import cube_transition
from propresenter.presentation_builder.cue_builder import createCue, generate_cue_group_from_cues
from propresenter.presentation_builder.slide_builder import create_random_background_color_slide, create_empty_slide
from propresenter.presentation_builder.element_builder import pink_box_element, image

slide_duration = 10.0
transition_duration = 1.0

def __create_announcement_slide(post: CTPost) -> Slide:
    create_random_background_color_slide()

def __fetch_image_and_store_in_pro_assets(post: CTPost, ct_image_fetcher: CTImageFetcher) -> str:
    image_url = post.get_url_first_image()
    image: bytes = ct_image_fetcher.fetch_image_png(image_url=image_url)
    churchtools_image_id = image_url.split("/")[-1]
    filename = '{}.png'.format(churchtools_image_id)
    pro_assets.write(filename, image)
    return filename


def create_announcement_presentation(posts: CTPosts, ct_api_client: CTApiClient) -> Presentation:
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

    ct_image_fetcher = CTImageFetcher(ct_api_client.get_domain_base_path(), ct_api_client.get_session())
    for post in posts.posts:
        filename = __fetch_image_and_store_in_pro_assets(post, ct_image_fetcher)
        slide = create_empty_slide()
        slide.elements.append(image(pro_assets.get_relative_path(filename)))
        presentation.cues.append(createCue(slide, completion_time=10))

    first_slide = create_empty_slide()
    first_slide.elements.append(pink_box_element())
    presentation.cues.append(createCue(first_slide, completion_time=5))

    second_slide = create_empty_slide()
    second_slide.elements.append(image("Media/Assets/Podcast.png"))
    presentation.cues.append(createCue(second_slide, completion_time=5))
    
    presentation.cue_groups.append(generate_cue_group_from_cues(presentation.cues))
    return presentation
