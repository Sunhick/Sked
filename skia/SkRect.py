#!/usr/bin/env python

"""
SkRect.py


"""

class SkRect(object):
    def __init__(self) -> None:
        self.top: float = 0.0
        self.left: float = 0.0
        self.bottom: float = 0.0
        self.right: float = 0.0

    def __str__(self) -> str:
        return (
            f"top: {self.top}"
            f"left: {self.left}"
            f"bottom: {self.bottom}"
            f"right: {self.right}"
        )
