#!/usr/bin/env python

"""
SkStream.py


"""

import logging
import struct
import ctypes

from typing import TextIO

class SkStream(object):
    def __init__(self, stream: TextIO, encoding: str) -> None:
        self.log = logging.getLogger(SkStream.__name__)
        self.stream = stream
        self.encoding = encoding

    def readU32(self) -> int:
        (value, ) = struct.unpack("I",str.encode(
            self.stream.read(ctypes.sizeof(ctypes.c_uint32)), self.encoding))
        return value

    def readFloat(self) -> float:
        (value, ) = struct.unpack("f", str.encode(
            self.stream.read(ctypes.sizeof(ctypes.c_float)), self.encoding))
        return value

    def read(self, size: int) -> str:
        return self.stream.read(size)
