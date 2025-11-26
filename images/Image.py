from abc import ABC, abstractmethod

class Image(ABC):
    
    # Abstract root class for images
    #resolution used for testing?
    def __init__(self, resolution: int, name: str, is_scannable: bool, image_link:str):
        self.resolution = resolution
        self.name = name
        self.is_scannable = is_scannable
        self.image_link = image_link
        
    @abstractmethod
    
    def getScannable(self):
        #return if image is scannable
        pass
    
