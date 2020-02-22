#!/usr/bin/env python3

"""
main.py:

starter file for skia editor.

"""

__author__  = "Sunil"

import sys
import logging
import logging.config
import yaml
import argparse
import os

import skia as sk

def setupLogging():
    skiaEdRoot = getSkiaEdRoot()
    with open(os.path.join(skiaEdRoot, "logging.yaml"), "r") as f:
        logConfig = yaml.safe_load(f.read())
        logging.config.dictConfig(logConfig)

def getSkiaEdRoot():
    skiaEdRoot = os.path.dirname(os.path.realpath(__file__))
    return skiaEdRoot

def main(args):
    log = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description='Skia Editor')
    parser.add_argument("--json-skps",
                        help="convert given json skia picture into skps format understood by skia debugger.")
    parser.add_argument("--skps",
                        help="parse the given skia picture.")
    parser.add_argument("--out",
                        help="capture output to the given file.")
    args = parser.parse_args()

    log.info(args)
    log.info("Skia Editor")
    log.warning("Skia Editor warning")

    picture = sk.SkPicture.MakeFromStream(99)
    picture.help()


if __name__ == "__main__":
    sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
    setupLogging()
    main(sys.argv[1:])
