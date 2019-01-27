import os
from glob import glob


def test_no_py_files_without_init_py():

    for file in glob('*/**/*.py', recursive=True):
        dirname = os.path.dirname(file)

        if file == '__init__.py':
            continue

        if dirname in ('docs', ):
            continue

        path = os.path.join(dirname, '__init__.py')
        assert os.path.exists(path), f"File {path} doe not exist, however folder includes *.py files"