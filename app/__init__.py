from flask import Flask
from config import Config

app = Flask(__name__)  # init flask object
app.config.from_object(Config)  # enabling command to run to be just 'flask run'

from app import routes  # leave as last line !!!!!!!!!