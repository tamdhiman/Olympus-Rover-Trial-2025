from python import Image
from python import Gallery
import uuid

gallery = Gallery()

#generated random objects

img1 = Image(
    image_id=str(uuid.uuid4()),
    file_path="static/images/mountain.jpg",
    qr_message=None
)

img2 = Image(
    image_id=str(uuid.uuid4()),
    file_path="static/images/city.jpg",
    qr_message=None
)

img3 = Image(
    image_id=str(uuid.uuid4()),
    file_path="static/images/qr_hello.png",
    qr_message="Hello World"
)

img4 = Image(
    image_id=str(uuid.uuid4()),
    file_path="static/images/qr_url.png",
    qr_message="https://example.com"
)

img5 = Image(
    image_id=str(uuid.uuid4()),
    file_path="static/images/portrait.jpg",
    qr_message=None
)

img6 = Image(
    image_id=str(uuid.uuid4()),
    file_path="static/images/qr_code_test.png",
    qr_message="SCAN-ME-12345"
)

gallery.add_image(img1)
gallery.add_image(img2)
gallery.add_image(img3)
gallery.add_image(img4)
gallery.add_image(img5)
gallery.add_image(img6)
