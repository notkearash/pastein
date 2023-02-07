#!/usr/bin/env python3
import ui
import models
import argparse


__version__ = '0.1.0'

API_POST_URL = 'https://pastebin.com/api/api_post.php'

def arg_parser():
    parser = argparse.ArgumentParser(
        prog="pastein.py",
        description="Pastebin.com Command Line Interface",
    )
    parser.add_argument('-k', '--api-key',
                        help="your api key from http://pastebin.com/doc_api#1")
    parser.add_argument('-f', '--file',
                        help="the file that you want to paste")
    parser.add_argument('-c', '--get',
                        help="reads the paste from paste code.", metavar='PASTE')
    parser.add_argument('--version', help="shows the version number",
                        action="version", version='%(prog)s v{version}'.format(version=__version__))
    args = parser.parse_args()
    return args


def option_parser(parser):
    args = parser
    if args.api_key is not None:
        if args.file is None:
            print(ui.nor, 'specify your file with -f.')
        paste = models.Paste(args.api_key, args.file)
        paste.request()
        
    elif args.get is not None:
        models.read(args)


if __name__ == '__main__':
    option_parser(arg_parser())
