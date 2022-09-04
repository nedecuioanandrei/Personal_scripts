import os 
import datetime
import argparse
import sys

current_path = os.getcwd()

def glue(p1, p2):
    return os.path.join(p1, p2)

root_dir = '{}'.format(datetime.datetime.now().strftime('%m_%d_%Y'))

dirs = [
        '{}/code'.format(root_dir),
        '{}/books'.format(root_dir)
        ]

files = [
        '{}/raport.md'.format(root_dir),
        '{}/links.md'.format(root_dir)
        ]


def touch(path):
    print('Creating file {}'.format(path))
    with open(path, 'a') as f:
        pass


def make_structure():
    for d in dirs:
        os.makedirs(glue(current_path, d), exist_ok=True)
    for f in files:
        touch(f)


def create(args):
    make_structure()


def get_parser():
    parser = argparse.ArgumentParser()
    parser.set_defaults(func=create)

    return parser


def main():
    parser = get_parser()
    args = parser.parse_args(sys.argv[1:])
    args.func(args)


if __name__ == "__main__":
    main()
