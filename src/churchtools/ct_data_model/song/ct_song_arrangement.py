

from churchtools.ct_data_model.song.ct_song_file import CTSongFile

class CTSongArrangement():

    def __init__(self, arrangement_data):
        self.arrangement_data = arrangement_data
        self.files: list[CTSongFile] = []
        if 'files' in arrangement_data:
            self.files = list(map(lambda file: CTSongFile(file), arrangement_data['files']))
        

    def is_default(self) -> bool:
        if 'isDefault' in self.arrangement_data:
            return self.arrangement_data['isDefault']
        return False

    def get_id(self) -> int:
        if 'id' in self.arrangement_data:
            return self.arrangement_data['id']
        return None
    
    def get_files(self) -> list[CTSongFile]:
        return self.files