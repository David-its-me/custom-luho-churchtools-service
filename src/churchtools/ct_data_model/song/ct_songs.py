

from churchtools.ct_data_model.song.ct_song import CTSong


class CTSongs():

    def __init__(self, songs_data: list[dict]):
        self.songs: list[CTSong] = list(map(lambda song: CTSong(song), songs_data))

    def find_by_name(self, name: str) -> CTSong:
        for song in self.songs:
            if song.get_name() == name:
                return song
        return None
    
    def get_by_id(self, id: int) -> CTSong:
        for song in self.songs:
            if song.get_id() == id:
                return song
        return None