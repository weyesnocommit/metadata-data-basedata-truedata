from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

musharraxxa = Flask(__name__)
CORS(musharraxxa)

musharraxxa.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://<PATH>/database.db"
musharraxxa.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
extrememeBase = SQLAlchemy(musharraxxa)

@musharraxxa.route('/')
def tofi():
    return "yes" 




