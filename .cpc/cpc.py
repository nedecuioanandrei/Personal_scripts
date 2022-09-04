import os 
import shutil
import argparse
import sys
import datetime
import getpass
import re
from zipfile import ZipFile


current_path = os.path.abspath(os.getcwd())
scripts_path = 'scripts'
dirs = [
        'tests',
        scripts_path,
        'bs'
        ]


language_extension_mapping = {
        'cpp': 'cpp',
        'py': 'py'
        }


makra_mapping = {
        'cpp' : '//Created by: ' + str(getpass.getuser()) + ' time: '\
                + str(datetime.datetime.now()) + '\n',

        'py' : '# Created by: ' + str(getpass.getuser()) + ' time: '\
                + str(datetime.datetime.now()) + '\n'
        }


def glue(path1, path2):
    return os.path.join(path1, path2)


def create_dir_structure():
    for d in dirs:
        print('Creating dir {} ...'.format(d))
        os.makedirs(glue(current_path, d))


def touch(path):
    if not os.path.isdir(os.path.dirname(path)):
        raise 
    print('Creating file {} ...'.format(path))
    with open(path, 'a') as f:
        pass


def count_archives():
    count = 0
    for file in os.listdir():
        if re.search('Cpc_archive.*.zip', file):
            count += 1
    return count


def init(args):
    '''
    Create a cpc dir!
    '''
    print('Init cpc dir! ...')
    create_dir_structure()
    

def archive(args):
    '''
    Archive cpp dir!
    '''
    # shutil.make_archive('Cpc_archive{}'.format(str(count_archives() + 1)), 'zip', '.')
    # os.chdir('../') 
    print('Archive cpc folder ...')
    with ZipFile('Cpc_archive{}.zip'.format(str(count_archives() + 1)), 'w') as zo:
        zo.write('bs')
        zo.write('scripts')
        zo.write('tests')


def create(args):
    '''
    Create a new source file!
    '''
    filename = args.name
    language = args.language
    file_full_name = filename + '.' + language_extension_mapping[language]
    file_full_path = glue(scripts_path, file_full_name)

    #print('Creating {} ...'.format(file_full_path))

    touch(file_full_path)
    
    if not args.mt:
        with open(file_full_path, 'w') as f:
            f.write(makra_mapping[language])


def get_parser():
    main_parser = argparse.ArgumentParser()
    subparsers = main_parser.add_subparsers()

    init_parser = subparsers.add_parser('init', help='Init cpc folder!')
    init_parser.set_defaults(func=init)

    archive_parser = subparsers.add_parser('archive', help='Archive cpc folde!')
    archive_parser.set_defaults(func=archive)

    create_parser = subparsers.add_parser('create', help='Create new source file!')
    create_parser.add_argument('name', help='filename')
    create_parser.add_argument('language', help='language')
    create_parser.add_argument('--mt', action='store_true', help='No blueprint')
    create_parser.set_defaults(func=create)
    
    return main_parser


def main():
    parser = get_parser()
    args = parser.parse_args(sys.argv[1:])
    args.func(args)


if __name__ == "__main__":
    main()

