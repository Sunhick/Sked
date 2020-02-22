#!/usr/bin/env python

"""
SkPicture.py

Represents the skia picture

"""

__author__  = "Sunil"

import logging

class SkPicture(object):
    def __init__(self):
        self.log = logging.getLogger(SkPicture.__name__)
        self.log.info("SkPicture object constructed")

    def help(self):
        self.log.error("help called")
