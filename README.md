# img2qr

Service for QR code extraction from image using [sanic](https://github.com/channelcat/sanic/) and [pyzbar](https://github.com/NaturalHistoryMuseum/pyzbar).

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

```
pip install -r requirements.txt
```