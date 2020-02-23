#!/usr/bin/env python

"""
SkPictureData.py


"""

import logging
import json

from .SkRect import SkRect

class SkPictInfo(object):
    def __init__(self) -> None:
        self.log = logging.getLogger(SkPictInfo.__name__)
        self.magic: str = ""
        self.version: int = 0
        self.cullRect: SkRect = SkRect()

class SkPictureData(object):
    def __init__(self) -> None:
        pass
