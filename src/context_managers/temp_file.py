from contextlib import contextmanager
import tempfile
import os
from typing import Generator

@contextmanager
def TempFile(content: str, dir_path: str = None) -> Generator[str, None, None]:
    """
    Creates a temporary file, writes the content
    and automatically removes it when exiting the context.
    """
    temp = tempfile.NamedTemporaryFile(
        mode="w",
        delete=False,
        dir=dir_path,
        suffix=".tmp"
    )

    try:
        temp.write(content)
        temp.flush()
        yield temp.name  # returns the path
    finally:
        temp.close()
        os.remove(temp.name)
