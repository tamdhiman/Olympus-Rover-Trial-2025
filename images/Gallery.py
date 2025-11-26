from .Image import Image
class Gallery:
    """
    Manages captured images, favourites, and simple ordering.
    """

    def __init__(self):
        # All stored images:
        # key: image_id or filename
        # value: dict with image object, message, status, and index number
        self.all_images = {}

        # Linked-list style ordering (for drag & drop in UI)
        # For now, represented as a Python list of keys
        self.image_order = []

        # Favourite images
        # key: image_id -> value: same structure as all_images
        self.favourite_images = {}

        # Total number of images stored
        self.image_count = 0
