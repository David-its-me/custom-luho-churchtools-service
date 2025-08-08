import slide_pb2
import basicTypes_pb2
import graphicsData_pb2

def getSlideSize()-> graphicsData_pb2.Graphics.Size:
    size = graphicsData_pb2.Graphics.Size()
    size.height = 1080
    size.width = 1920
    return size

def createElement() -> slide_pb2.Slide.Element:
    element = slide_pb2.Slide.Element()
    return element

def create_slide() -> slide_pb2.Slide:
    slide = slide_pb2.Slide()
    color = basicTypes_pb2.Color()
    color.alpha = 255
    color.blue = 200
    color.red = 100
    color.green = 0
    slide.background_color.CopyFrom(color)
    slide.draws_background_color = True
    slide.size.CopyFrom(getSlideSize())
    #slide.elements.append(createElement())
    return slide