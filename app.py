from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import time
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Epoch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    epoch_time = db.Column(db.String(200), unique=True, nullable=False)

    def __init__(self, epoch_time):
        self.epoch_time = epoch_time


@app.route('/', methods=['GET','POST'])
def index():
    query = '''CREATE TABLE if not exists epoch(id serial PRIMARY KEY, epoch_time VARCHAR (200) UNIQUE NOT NULL);'''
    db.engine.execute(query)
    epoch_time = int(time.time())
    entry = Epoch(epoch_time)
    db.session.add(entry)
    db.session.commit()
    return render_template("index.html", epoch_time=epoch_time)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=8888)
