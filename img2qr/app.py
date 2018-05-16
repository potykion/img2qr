from typing import Optional

from PIL import Image
from sanic import Sanic
from sanic.exceptions import InvalidUsage
from sanic.request import Request
from sanic.response import json

from img2qr.utils import download_image, read_image, recognize_qrs

app = Sanic()


@app.route('/extract', ['GET', 'POST'])
async def extract(request):
    image = await _try_extract_image(request)
    if not image:
        return json({'error': 'No image passed.'}, 400)

    qrs = recognize_qrs(image)
    if qrs:
        return json(qrs)
    else:
        return json({'error': 'No QR codes recognized.'}, 404)


async def _try_extract_image(request: Request) -> Optional[Image.Image]:
    image_url = _try_extract_image_url(request)
    if image_url:
        return await download_image(image_url)

    image_data = _try_extract_image_data(request)
    if image_data:
        return read_image(image_data)

    return None


def _try_extract_image_url(request: Request) -> Optional[str]:
    image_url = request.form.get('image_url') or request.args.get('image_url')

    if not image_url:
        try:
            image_url = request.json.get('image_url')
        except (InvalidUsage, AttributeError):
            image_url = None

    return image_url


def _try_extract_image_data(request: Request) -> Optional[bytes]:
    image_file = request.files.get('image_file')
    image_data = getattr(image_file, 'body', None)
    return image_data
