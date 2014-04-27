
from flask import Flask

app = Flask(__name__)
app.config.from_object(__name__)

IMG_FOLDER = "imgs/"

API_BASE_URL = "http://jhproj05.cs.st-andrews.ac.uk"
API_SENSORS_URL = API_BASE_URL + "/sensor/"
