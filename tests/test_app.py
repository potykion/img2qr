import json

from img2qr.app import app


def test_extract_api_for_image_file_with_qr(image_file_with_qr):
    image_file, qr = image_file_with_qr

    request, response = app.test_client.post(
        '/extract',
        data={'image_file': image_file}
    )

    assert response.status == 200
    assert response.json == [
        qr
    ]


def test_extract_api_for_image_url_with_qr_as_form(image_url_with_qr):
    image_url, qr = image_url_with_qr

    request, response = app.test_client.post(
        '/extract',
        data={'image_url': image_url}
    )

    assert response.status == 200
    assert response.json == [qr]


def test_extract_api_for_image_url_with_qr_as_json(image_url_with_qr):
    image_url, qr = image_url_with_qr

    request, response = app.test_client.post(
        '/extract',
        data=json.dumps({'image_url': image_url})
    )

    assert response.status == 200
    assert response.json == [qr]


def test_extract_api_for_image_url_with_qr_as_query(image_url_with_qr):
    image_url, qr = image_url_with_qr

    request, response = app.test_client.post(
        '/extract',
        params={'image_url': image_url}
    )

    assert response.status == 200
    assert response.json == [qr]


def test_extract_api_for_image_url_without_qr(image_url_without_qr):
    request, response = app.test_client.post(
        '/extract',
        data={'image_url': image_url_without_qr}
    )

    assert response.status == 404
    assert response.json['error'] == 'No QR codes recognized.'


def test_extract_api_without_image():
    request, response = app.test_client.post(
        '/extract',
    )

    assert response.status == 400
    assert response.json['error'] == 'No image passed.'
