'''
Exercise 1:

Create a synchronous context manager TempFile(content: str):

- Creates a temporary file
- Writes content
- Returns the path
- Removes it on exit

'''
from temp_file import TempFile

print("\n============= Solution to Exercise 1 =============\n")

with TempFile("Jefferson test") as path:
    print("File created in:", path)

print("File removed automatically")

'''
Exercise 2:

Create an asynchronous version of AsyncTempFile(content: str):

- Uses aiofiles
- async with → await write

'''
import asyncio
from temp_file_async import AsyncTempFile

print("\n============= Solution to Exercise 2 =============\n")

async def main():
    async with AsyncTempFile("Content async") as path:
        print("File created:", path)

asyncio.run(main())


'''
Exercise 3:

Create TempDir() that:

- Creates a temporary directory
- Allows creating multiple TempFiles inside
- Removes everything at the end

'''
from temp_dir import TempDir
import os

print("\n============= Solution to Exercise 3 =============\n")

with TempDir() as dir_path:
    with TempFile("Hello", dir_path) as f1:
        with TempFile("World", dir_path) as f2:
            
            print(f"Content of f1: {open(f1).read()}")
            print(f"Content of f2: {open(f2).read()}")
            print(f"Do files exist? f1: {os.path.exists(f1)}, f2: {os.path.exists(f2)} \n")
    
    # Here, f1 and f2 have already been removed by their context managers.
    print(f"Do files exist after inner withs? f1: {os.path.exists(f1)}, f2: {os.path.exists(f2)}")
    print(f"Does the directory still exist? {os.path.exists(dir_path)} \n")

# Here, the directory removed by TempDir.
print(f"Does the directory exist after outer with? {os.path.exists(dir_path)}")


