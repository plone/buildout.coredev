import os
import os.path
import sys

BASE = os.path.abspath(os.curdir)
SRC = os.path.join(BASE, 'src')

def main():
    path = sys.path
    path = [p for p in path if 'python2.6' not in p]
    path = [p for p in path if 'python-2.6' not in p]
    path = [p for p in path if not p.startswith(BASE)]
    folders = path + [SRC]

    arg = ' '.join(folders)
    command = 'ohcount ' + arg + ' > ' + BASE + '/size.txt'
    print command
    os.system(command)

if __name__ == '__main__':
    main()
