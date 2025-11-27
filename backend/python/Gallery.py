from attempt2 import Image
class Gallery:
    
    def __init__(self):
        #make into a list for gallery
        self.images = []
        
    
    def add_image(self,image: Image):
        self.images.append(image)
    
    def remove_image(self, image: Image):
        self.images.remove(image)
    
    def list_images(self):
        return self.images
    
    def get_image(self):
        return self.image