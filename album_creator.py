# coding=utf-8
__author__ = 'Alexandr'
import urllib2
from bs4 import BeautifulSoup


ARTISTS_WIKI_URL = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'
ALBUM_WIKI_URL = 'https://ru.wikiquote.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'
IMAGE_WIKI_URL = 'https://commons.wikimedia.org/wiki/Special:Random/File'


class Artist(object):
    name = None

    @staticmethod
    def get_artist():
        return BeautifulSoup(urllib2.urlopen(ARTISTS_WIKI_URL, 'html.parser')).title.text[:-12].encode('utf-8')

    def __init__(self):
        self.name = self.get_artist()


class Album(object):
    name = None

    @staticmethod
    def get_album():
        return BeautifulSoup(urllib2.urlopen(ALBUM_WIKI_URL, 'html.parser')).title.text[:-15].encode('utf-8')

    def __init__(self):
        self.name = self.get_album()


def get_album_image():
    return BeautifulSoup(urllib2.urlopen(IMAGE_WIKI_URL, 'html.parser')).find(class_="fullMedia").a['href']


def create_album():
    artist = Artist()
    album = Album()

    return "{} - {}".format(artist.name, album.name)

