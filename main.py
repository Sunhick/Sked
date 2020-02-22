#!/usr/bin/env python

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

from skia import SkPicture as sk

def setupLogging():
    with open('logging.yaml', 'r') as f:
        logConfig = yaml.safe_load(f.read())
        logging.config.dictConfig(logConfig)

def main(args):
    log = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description='Skia Editor')
    parser.add_argument("--json-skps",
                        help="Convert given json skia picture into skps format unerstood by skia debugger")
    args = parser.parse_args()

    log.info(args)
    log.info("Skia Editor")
    log.warning("Skia Editor warning")

    picture = sk.SkPicture()
    picture.help()


if __name__ == "__main__":
    setupLogging()
    main(sys.argv[1:])
