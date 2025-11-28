class Image:
    def __init__(self, image_id: str, file_path: str, qr_message: str |None = None):
        self.image_id = image_id
        self.file_path = file_path
        self.qr_message = qr_message
        self.is_scannable = qr_message is not None
    
    def to_dict(self):
        #dictionary for JSON/frontend objects
        return{
            "id": self.image_id,
            "file_path": self.file_path,
            "qr_message": self.qr_message,
            "is_scannable": self.is_scannable,
            
        }