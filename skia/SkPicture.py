#!/usr/bin/env python

"""
SkPicture.py

Represents the skia picture

"""

from __future__ import annotations

__author__  = "Sunil"

import logging
import struct


from typing_extensions import Final
from typing import (Tuple,
                    Optional,
                    TextIO)

from .SkStream import SkStream
from .SkPictureData import SkPictInfo

kMagic: Final = "skiapict"
kSkFileEncoding: Final = "ISO-8859-1"
kCurrentVersion: Final = 73

class SkPicture(object):
    def __init__(self, filepath: str) -> None:
        self.log = logging.getLogger(SkPicture.__name__)
        self.log.info("SkPicture object constructed")
        self.filepath = filepath

    def help(self) -> None:
        self.log.error("help called")

    def streamIsSkp(self, stream: TextIO) -> Tuple[bool, Optional[SkPictInfo]]:
        info = SkPictInfo()
        if not stream: return (False, info)

        skStream = SkStream(stream, kSkFileEncoding)
        info.magic = stream.read(len(kMagic))
        if not info.magic: return (False, None)

        info.version = skStream.readU32()
        assert info.version > 60, "Skia pict version lesser than 60 isn't support!"

        info.cullRect.left = skStream.readFloat()
        info.cullRect.top = skStream.readFloat()
        info.cullRect.right = skStream.readFloat()
        info.cullRect.bottom = skStream.readFloat()
        return (self.isValidPict(info), info)

    def isValidPict(self, pict: SkPictInfo) -> bool:
        return (
            # skia also requires a min version check but we don't need that as we
            # only support versions 60 and up.
            pict.magic == kMagic and pict.version <= kCurrentVersion
        )

    def parse(self) -> None:
        self.log.info("File path: " + str(self.filepath))
        with open(self.filepath, "r", encoding=kSkFileEncoding) as skfile:
            status, pInfo = self.streamIsSkp(skfile)
            assert status, f"{self.filepath} isn't a skia picture file!"


    def __str__(self) -> str:
        return f"{self.filepath}"

    @staticmethod
    def MakeFromStream(filepath: str) -> SkPicture:
        picture = SkPicture(filepath)
        picture.parse()
        return picture
