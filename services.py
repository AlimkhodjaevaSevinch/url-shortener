from datetime import datetime
from flask import request
from app import db
from models import ShortUrl, short_id


class ShortUrlService:

    @staticmethod
    def short(short_url):
        short = db.session.query(ShortUrl).\
                filter_by(short_url=short_url).first()
        return short

    @staticmethod
    def all_urls():
        al = db.session.query(ShortUrl).all()
        return al

    @staticmethod
    def long(long_url):
        long = ShortUrl.query.filter_by(long_url=long_url).first()
        return long

    @staticmethod
    def gen():
        short_url = short_id(6)
        return short_url

    @staticmethod
    def new(url, short_url):
        new_link = ShortUrl(long_url=url,
                            short_url=short_url, time_to_create=datetime.now())
        db.session.add(new_link)
        db.session.commit()
        short = request.host_url + short_url
        return short

    @staticmethod
    def count_click(link):
        link.clicks += 1
        db.session.commit()
