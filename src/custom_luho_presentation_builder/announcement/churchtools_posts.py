# Churchtools API Client
from churchtools.ct_client.ct_api_client import CTApiClient
from churchtools.ct_client.ct_image_controller import CTImageController

# Churchtools data model
from churchtools.ct_data_model.post.ct_posts import CTPosts, CTPost

# Propresenter file system
from propresenter.file_io import pro_assets

# Propresenter protobuf
from propresenter.presentation_builder.cue_actions.macro import create_announcement_macro
from propresenter.presentation_builder.slide_element.image import image
from propresenter.presentation_builder.standard_colors import *
from propresenter.pb_auto_generated.presentation_pb2 import Presentation
from propresenter.pb_auto_generated.cue_pb2 import Cue
from propresenter.pb_auto_generated.basicTypes_pb2 import Color
from propresenter.presentation_builder.cue import (
    createCue,
    generate_cue_group_from_cues,
)
from propresenter.presentation_builder.slide import (
    create_slide_with_background_color,
)

from datetime import datetime, timedelta
import pytz as timezone


def __fetch_image_and_store_in_pro_assets(
    post: CTPost, ct_image_controller: CTImageController
) -> str:
    image_url = post.get_url_first_image()
    image: bytes = ct_image_controller.get_image_png(image_url=image_url)
    churchtools_image_id = image_url.split("/")[-1]
    filename = "{}.png".format(churchtools_image_id)
    pro_assets.write(filename, image)
    return filename


def __pretty_print_post_info(post: CTPost):
    print("{}".format(post.get_title()))
    print("Autor:  {}".format(post.get_author()))
    print("Gruppe: {}".format(post.get_group_name()))
    print()


def __filter_posts(posts: list[CTPost], post_not_older_than_weeks: int) -> list[CTPost]:
    # Only include post with visibility 'group_visible'
    print("Filtere Beiträge nach Gruppen-Sichtbarkeit")
    posts = list(filter(lambda post: post.is_visibility_not_restricted(), posts))

    # Only include when today is between publishedDate and expirationDate
    print("Filtere Beiträge nach Veröffentlichungszeitraum")
    posts = list(
        filter(
            lambda post: post.is_publicity_period_inside(datetime.now(tz=timezone.utc)),
            posts,
        )
    )

    # Only include post which are younger than 6 months
    print(
        "Filtere Beiträge heraus, die älter als {} Wochen als sind".format(
            post_not_older_than_weeks
        )
    )
    posts = list(
        filter(
            lambda post: post.get_last_edited_date()
            + timedelta(weeks=post_not_older_than_weeks)
            > datetime.now(tz=timezone.utc),
            posts,
        )
    )
    print()

    return posts


def __fetch_filtered_posts_data(
    ct_api_client: CTApiClient, post_not_older_than_weeks: int
) -> list[CTPost]:

    # Fetch Posts
    print("Lade Beiträge von Churchtools ...")
    posts = CTPosts(ct_api_client.get_benste_uem_api().get_posts())

    posts = __filter_posts(posts.posts_data, post_not_older_than_weeks)

    return posts


def __fetch_and_add_ct_post_images_to_presentation(
    ct_api_client: CTApiClient,
    posts: list[CTPost],
    presentation: Presentation,
    slide_duration: int,
) -> Presentation:

    ct_image_controller = CTImageController(
        ct_api_client.get_domain_base_path(), ct_api_client.get_session()
    )
    cues: list[Cue] = []

    for post in posts:
        __pretty_print_post_info(post)
        filename = __fetch_image_and_store_in_pro_assets(post, ct_image_controller)
        slide = create_slide_with_background_color(background_color=black())
        slide.elements.append(image(pro_assets.get_relative_path(filename)))
        cue = createCue(slide, actions=[create_announcement_macro()], completion_time=slide_duration)
        cues.append(cue)
        presentation.cues.append(cue)

    presentation.cue_groups.append(
        generate_cue_group_from_cues(
            cues,
            color=churchtools_blue(),
            label="Churchtools Beiträge",
        )
    )
    return presentation


def create(
    presentation: Presentation, 
    slide_duration: int, 
    post_not_older_than_weeks: int,
    ct_api_client: CTApiClient
) -> Presentation:

    posts = __fetch_filtered_posts_data(ct_api_client, post_not_older_than_weeks)
    presentation = __fetch_and_add_ct_post_images_to_presentation(
        ct_api_client,
        posts,
        presentation,
        slide_duration,
    )
    return presentation
