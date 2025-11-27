from .Image import Image
class TakeImage(Image):
    def __init__(self, zoom: float, **kwargs):
        super().__init__(**kwargs)
        self.zoom = zoom

    def sendCaptureSignal (self):
        return self.is_success
    
    def storeImage(self, local_file: str):
        pass

    def getScannable(self):
        return self.is_scannable
