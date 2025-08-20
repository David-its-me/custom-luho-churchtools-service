

from churchtools.ct_data_model.song.ct_song_arrangement import CTSongArrangement


class CTSong():

    def __init__(self, song_data: dict):
        self.song = song_data
        arrangements_data = []
        if 'arrangements' in song_data:
            arrangements_data = song_data['arrangements']
        self.arrangements: list[CTSongArrangement] = list(map(lambda arrangement: CTSongArrangement(arrangement), arrangements_data))

    
    def get_id(self) -> int:
        if 'id' in self.song:
            return self.song['id']
        return None
    
    def get_name(self) -> str:
        if 'name' in self.song:
            return self.song['name']
        return None
    
    def find_default_arrangement(self) -> CTSongArrangement:
        for arrangement in self.arrangements:
            if arrangement.is_default():
                return arrangement
        return None