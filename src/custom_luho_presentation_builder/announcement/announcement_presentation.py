# Churchtools API Client
from churchtools.ct_client.ct_api_client import CTApiClient

# Propresenter file system
from churchtools.ct_data_model.song.ct_song import CTSong
from churchtools.ct_data_model.song.ct_songs import CTSongs
from propresenter.file_io import pro_file

# Propresenter protobuf
from propresenter.pb_auto_generated.presentation_pb2 import Presentation
from propresenter.presentation_builder.presentation import (
    create_empty_presentation,
)
from propresenter.presentation_builder.transition import dissolve_transition

import custom_luho_presentation_builder.announcement.churchtools_posts as churchtools_posts
import custom_luho_presentation_builder.announcement.default_slides as default_slides
import custom_luho_presentation_builder.announcement.churchtools_dates as churchtools_dates

##################################
### CONFIG
##################################
slide_duration = 10.0
transition_duration = 0.2
post_not_older_than_weeks = 26
##################################
presentation_name = "Announcements"
default_slides_presentation_name = "Announcements-Standard-Folien"
default_slides_library_name = "Vorlagen"
propresenter_save_library_names = ["Vorlagen", "Default", "...aktueller GoDi"]
churchtools_song_name = "Announcements"
##################################


def __create_empty_announcement_base_presentation() -> Presentation:
    presentation: Presentation = create_empty_presentation()
    # Configure the loop transition
    presentation.transition.CopyFrom(
        dissolve_transition(transition_duration=transition_duration)
    )
    presentation.slide_show_duration = slide_duration
    presentation.timeline.CopyFrom(
        Presentation.Timeline(
            loop=True, duration=(slide_duration - transition_duration)
        )
    ),
    return presentation


def __upload_presentation_churchtools(ct_api_client: CTApiClient):
    print("Lade Announcement Präsentation auf Churchtools hoch ...")

    # get songs from churchtools
    songs = CTSongs(ct_api_client.get_benste_uem_api().get_songs())

    announcement_song: CTSong = songs.find_by_name(churchtools_song_name)

    print("Song name:  {}".format(announcement_song.get_name()))
    print("Song id:    {}".format(announcement_song.get_id()))
    print("Datei:      {}.pro".format(presentation_name))
    print()

    # delete old files
    ct_api_client.get_benste_uem_api().file_delete(
        domain_type="song_arrangement",
        domain_identifier=announcement_song.find_default_arrangement().get_id()
    )

    # upload file
    ct_api_client.get_benste_uem_api().file_upload(
        source_filepath=pro_file.get_absolute_path(
            library=propresenter_save_library_names[0], filename=presentation_name
        ),
        domain_type="song_arrangement",
        domain_identifier=announcement_song.find_default_arrangement().get_id(),
    )
    


def create_announcement_presentation() -> Presentation:

    ct_api_client = CTApiClient()
    # Login into the api
    ct_api_client.open_connection()
    ct_api_client.open_benste_uem_api()

    presentation = __create_empty_announcement_base_presentation()
    print("################")
    print("### Beiträge ###")
    print("################")
    print()
    presentation = churchtools_posts.create(
        presentation, 
        slide_duration, 
        post_not_older_than_weeks, 
        ct_api_client
    )
    print("#######################")
    print("### Standard Folien ###")
    print("#######################")
    print()
    presentation = default_slides.create(
        presentation,
        slide_duration,
        default_slides_library_name,
        default_slides_presentation_name,
    )
    #print("###############")
    #print("### Termine ###")
    #print("###############")
    #print()
    #presentation = churchtools_dates.create(
    #    presentation, 
    #    slide_duration, 
    #    ct_api_client)

    
    print("#################")
    print("### Speichern ###")
    print("#################")
    print()

    print("Speichere Präsentation in Propresenter")

    for propresenter_library_name in propresenter_save_library_names:
        print("Bibliothek: {}".format(propresenter_library_name))
        print("Name:       {}".format(presentation_name))
        print()
        pro_file.write(
            propresenter_library_name,
            presentation_name,
            presentation,
        )

    __upload_presentation_churchtools(ct_api_client)
    return presentation
