from propresenter.pb_auto_generated import presentation_pb2
import userpaths

def __get_path(library: str, filename: str):
    if (filename.endswith('.pro')):
        return "{}/ProPresenter/Libraries/{}/{}".format(userpaths.get_my_documents(), library, filename)
    return "{}/ProPresenter/Libraries/{}/{}.pro".format(userpaths.get_my_documents(), library, filename)

def read(library: str, filename: str) -> presentation_pb2.Presentation:
    path = __get_path(library, filename)
    presentation = presentation_pb2.Presentation()
    try:
        with open(path, "rb") as file_data:
            presentation.ParseFromString(file_data.read())
        return presentation
    except IOError:
        print("Could not open file.")


def write(library: str, filename: str, data: presentation_pb2.Presentation):
    path = __get_path(library, filename)
    with open(path, "wb") as file_data:
        file_data.write(data.SerializeToString())