#!/usr/bin/env python

"""
SkPicture.py

Represents the skia picture

"""

__author__  = "Sunil"

import logging

class SkPicture(object):
    def __init__(self, filepath):
        self.log = logging.getLogger(SkPicture.__name__)
        self.log.info("SkPicture object constructed")
        self.filepath = filepath

    def help(self):
        self.log.error("help called")

    def parse(self):
        self.log.info("File path: " + str(self.filepath))


    @staticmethod
    def MakeFromStream(filepath: str):
        picture = SkPicture(filepath)
        picture.parse()
        return picture
