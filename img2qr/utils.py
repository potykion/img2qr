import io
from typing import List, Iterable

import aiohttp
from PIL import Image
from pyzbar.pyzbar import decode, Decoded


async def download_image(image_url) -> Image.Image:
    async with aiohttp.ClientSession() as session:
        async with session.get(image_url) as response:
            image_data = await response.read()
            return read_image(image_data)


def read_image(image_data: bytes) -> Image.Image:
    return Image.open(io.BytesIO(image_data))


def recognize_qrs(image) -> List[str]:
    raw_qrs = decode(image)
    formatted_qrs = _format_qrs(raw_qrs)
    return formatted_qrs


def _format_qrs(raw_qrs: Iterable[Decoded]) -> List[str]:
    return [
        qr.data.decode('utf-8')
        for qr in raw_qrs
    ]
