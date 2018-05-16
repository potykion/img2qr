from img2qr.app import app
from img2qr.config import PORT, HOST

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
