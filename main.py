#!/usr/bin/env python

"""main.py: starter file for skia editor."""

__author__      = "Sunil"

import sys
import logging
import logging.config
import yaml

def setupLogging():
    with open('logging.yaml', 'r') as f:
        logConfig = yaml.safe_load(f.read())
        logging.config.dictConfig(logConfig)

def main(args):
    log = logging.getLogger(__name__)
    log.info("Skia Editor")
    log.warning("Skia Editor warning")


if __name__ == "__main__":
    setupLogging()
    main(sys.argv[1:])
