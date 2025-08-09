
import userpaths

def get_relative_path(filename: str):
    return "Media/Assets/{}".format(filename)

def get_absolute_path(filename: str):
    return "{}/ProPresenter/{}".format(userpaths.get_my_documents(), get_relative_path(filename))

def write(filename: str, data: bytes):
    path = get_absolute_path(filename)
    with open(path, "wb") as file_data:
        file_data.write(data)