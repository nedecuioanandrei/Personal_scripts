import os 


current_path = os.getcwd()
ignored_dirs = [
        '.git'
        ]
ignored_files = [
        'README.md',
        '.gitignore',
        'init.py',
        '.bashrc'
        ]

def glue(pth1, pth2):
    return os.path.join(pth1, pth2)


bashrc_path = glue(current_path, '.bashrc')


def append_scripts_aliases():
    aliases = []

    for root, dirs, files in os.walk(current_path, topdown=True, onerror=None, followlinks=False):
        for d in dirs:
            if d in ignored_dirs:
                dirs.remove(d)
        
        new_files = []

        for f in files:
            if not f in ignored_files:
                new_files.append(f)

        for f in new_files:
            aliases.append('alias {}=\"python3 {}\"'.format(os.path.basename(f).split('.')[0], glue(root, f)))
    
    
   # for alias in aliases:
   #     print(alias)

    
    with open(bashrc_path, 'r') as f:
        data = f.read()
        new_aliases = []
        for alias in aliases:
            if not alias in data:
                new_aliases.append(alias)
    
    with open(bashrc_path, 'a') as f:
        for alias in new_aliases:
            print('New alias {}'.format(alias))
            f.write(alias + '\n')

    

def main():
    print('bashrc path is {}'.format(bashrc_path))
    append_scripts_aliases() 


if __name__ == "__main__":
    main()

