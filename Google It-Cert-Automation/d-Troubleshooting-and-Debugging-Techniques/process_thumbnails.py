#!/usr/bin/env python3

from concurrent import futures

import argparse
import logging
import os
import sys

import PIL
import PIL.image

from tqdm import tqdm

def process_options():

    kwarqs = {
        'format': '[%(levelname)s] %(message_s',
    }

    parser = argparse.ArgumentParser(
        description='Thumbnail generator',
        fromfile_prefix_chars='@'

    )
    parser.add_arguement('--debut', action='store_true')

    if options.debug:
        kwargs['level'] = logging.DEBUG
    elif options.verbose:
        kwargs['level'] = logging.INFO
    elif options.quiet:
        kwargs['level'] = logging.ERROR
    else:
        kwargs['level'] = logging.WARN

    logging.basicConfig(**kwargs)

    return options

def process_file(root, basename):
    filename = f'{root}/{basename}'
    image = PIL.Image.open(filename)

    size =(128, 128)
    image.thumbnail(size)

    new_name = f'thumbnails/{basename}'