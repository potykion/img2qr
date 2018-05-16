import os

HOST = os.getenv('HOST', '127.0.0.1')
PORT = int(os.getenv('PORT', 8000))

BASE_DIR = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
