#!/usr/bin/env python

"""
SkPicture.py

Represents the skia picture

"""

from __future__ import annotations

__author__  = "Sunil"

import logging

class SkPicture(object):
    def __init__(self, filepath: str) -> None:
        self.log = logging.getLogger(SkPicture.__name__)
        self.log.info("SkPicture object constructed")
        self.filepath = filepath

    def help(self) -> None:
        self.log.error("help called")

    def parse(self) -> None:
        self.log.info("File path: " + str(self.filepath))


    @staticmethod
    def MakeFromStream(filepath: str) -> SkPicture:
        picture = SkPicture(filepath)
        picture.parse()
        return picture
