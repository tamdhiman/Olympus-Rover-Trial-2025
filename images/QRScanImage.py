from .Image import Image
class QRScanImage(Image):
    
    # Abstract root class for images
    #resolution used for testing?
    def __init__(self, image_obj, message: str, **kwargs):
        # Pass Image attributes via kwargs
        super().__init__(**kwargs)
        self.image_obj = image_obj
        self._message = message

    def _detectQR(self):
        """Private method to detect QR code."""
        #Add QR detection logic
        pass

    def getStatus(self):
        """Public method to get the scan status."""
        #Determine status
        pass

    def getMessage(self):
        """Public method to get the decoded message."""
        return self._message

    def getScannable(self):
        return self.is_scannable

