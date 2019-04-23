import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
database = SQLAlchemy(app)
migrate = Migrate(app, database)

from app import routes, models

@app.route('/')
def test():
    return 'Pls work'

if __name__ == '__main__':
    app.run()