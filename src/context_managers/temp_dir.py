import tempfile
import shutil
import os
from contextlib import contextmanager
from typing import Generator
import shutil

@contextmanager
def TempDir() -> Generator[str, None, None]:
    """
    Creates a temporary directory, allows you to create files inside
    and removes everything (directory and contents) when you exit the context.
    """
    dir_path = tempfile.mkdtemp()  # Create an empty temp directory.

    try:
        yield dir_path
    finally:
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)  # recursively remove everything
