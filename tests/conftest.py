import os

import pytest

from img2qr.config import BASE_DIR


@pytest.fixture()
def image_file_with_qr():
    image_file = open(os.path.join(BASE_DIR, 'data/jNPRavAzQZU.jpg'), 'rb')
    qr = 't=20180511T222100&s=49.90&fn=8710000101339597&i=91551&fp=2266822142&n=1'
    return image_file, qr


@pytest.fixture()
def image_url_without_qr():
    return 'https://upload.wikimedia.org/wikipedia/ru/2/22/Kot_gav_Gav.jpg'


@pytest.fixture()
def image_url_with_qr():
    image_url = 'https://www.qrstuff.com/images/sample.png'
    qr = 'http://www.qrstuff.com/'
    return image_url, qr
