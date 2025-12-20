from contextlib import asynccontextmanager
from typing import AsyncGenerator
import aiofiles
import tempfile
import os


@asynccontextmanager
async def AsyncTempFile(content: str) -> AsyncGenerator[str, None]:
    fd, path = tempfile.mkstemp(suffix=".tmp")
    os.close(fd)

    try:
        async with aiofiles.open(path, mode="w") as f:
            await f.write(content)

        yield path
    finally:
        os.remove(path)
