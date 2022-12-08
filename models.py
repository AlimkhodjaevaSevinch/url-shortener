from datetime import datetime
import string
from random import choice
from app import db


class ShortUrl(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    long_url = db.Column(db.String(400), unique=True, nullable=False)
    short_url = db.Column(db.String(20), unique=True, nullable=False)
    time_to_create = db.Column(db.DateTime(),
                               default=datetime.now(), nullable=False)
    clicks = db.Column(db.Integer, default=0)

    def __init__(self, long_url, short_url, time_to_create):
        self.long_url = long_url
        self.short_url = short_url
        self.time_to_create = time_to_create


def short_id(num_of_chars: int):
    return ''.join(choice(string.ascii_letters + string.digits)
                   for _ in range(num_of_chars))
