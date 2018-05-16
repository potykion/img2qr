# img2qr

Service for QR code extraction from image using [sanic](https://github.com/channelcat/sanic/) and [pyzbar](https://github.com/NaturalHistoryMuseum/pyzbar).

# Usage

Request with `image_url`:
```
GET /extract?image_url=https://www.qrstuff.com/images/sample.png HTTP/1.1
Host: img2qr.herokuapp.com
```

Response:
```
[
    "http://www.qrstuff.com/"
]
```

Request with `image_file` (using `data/6JEmaP3mj80.jpg`):

```
POST /extract HTTP/1.1
Host: img2qr.herokuapp.com
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="image_file"; filename="6JEmaP3mj80.jpg"
Content-Type: image/jpeg


------WebKitFormBoundary7MA4YWxkTrZu0gW--
```

Response:
```
[
    "t=20180511T222100&s=49.90&fn=8710000101339597&i=91551&fp=2266822142&n=1"
]
```


# Installation

## Sanic

### Windows

```
git clone https://github.com/channelcat/sanic.git
cd sanic
pip install .
```

### Linux

```
pip install sanic
```

## PyZBar

```
pip install pyzbar
```

### Windows

1. Download and install from [here](http://zbar.sourceforge.net/download.html)
2. Add path to libzbar-0.dll to PATH env (e.g. `C:\Program Files (x86)\ZBar\bin`)

### Linux

```
sudo apt-get install libzbar-dev
```

## Other libs

### On machine
```
pip install -r requirements/prod.txt
```

### On Heroku
```
pip install -r requirements/heroku.txt
```

# Deploy

## Heroku

0. https://github.com/NaturalHistoryMuseum/pyzbar/issues/23
1. Install [Heroku ZBar buildpack](https://github.com/sheck/heroku-buildpack-zbar)
2. Set envs:
    ```
    HOST = 0.0.0.0
    ZBAR_LIB = vendor/lib/libzbar.so
    LD_LIBRARY_PATH = $LD_LIBRARY_PATH:vendor/lib/
    ```
3. Install forked [PyZBar](https://github.com/CptSpaceToaster/pyzbar.git) (already included in requirements.txt)
