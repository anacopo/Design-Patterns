from Element import Element
import time
from Visitor import Visitor

class Image(Element):
    def __init__(self, image_name):
        self.image_name = image_name
        time.sleep(5)

    def print(self):
        print(f"Image with name: {self.image_name}")

    def accept(self, visitor: Visitor):
        visitor.visitImage(self)
