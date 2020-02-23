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
from typing import List

from skia import *

def setupLogging() -> None:
    skiaEdRoot = getSkiaEdRoot()
    with open(os.path.join(skiaEdRoot, "logging.yaml"), "r") as f:
        logConfig = yaml.safe_load(f.read())
        logging.config.dictConfig(logConfig)

def getSkiaEdRoot() -> str:
    skiaEdRoot = os.path.dirname(os.path.realpath(__file__))
    return skiaEdRoot

def main(args: List[str]) -> None:
    log = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description='Skia Editor')
    parser.add_argument("--json-skps",
                        help="convert given json skia picture into skps format understood by skia debugger.")
    parser.add_argument("--skps", required=True,
                        help="parse the given skia picture.")
    parser.add_argument("--out",
                        help="capture output to the given file.")
    pargs = parser.parse_args()

    # validate pargs

    log.info(args)
    log.info("Skia Editor")
    log.warning("Skia Editor warning")

    picture: SkPicture = SkPicture.MakeFromStream(pargs.skps)
    picture.help()

if __name__ == "__main__":
    setupLogging()
    main(sys.argv[1:])
