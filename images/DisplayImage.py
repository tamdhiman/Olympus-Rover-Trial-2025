from .Image import Image
class DisplayImage(Image):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    #Inherit?
    def getScannable(self):
        return self.is_scannable
