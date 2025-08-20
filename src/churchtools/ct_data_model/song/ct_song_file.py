class CTSongFile():

    def __init__(self, song_file_data):
        self.song_file_data = song_file_data

    def get_domain_id(self) -> str:
        if 'domainId' in self.song_file_data:
            return self.song_file_data['domainId']
        return None