from contextlib import contextmanager
import tempfile
import os
from typing import Generator

@contextmanager
def TempFile(content: str, dir_path: str = None) -> Generator[str, None, None]:
    """
    Cria um arquivo temporário, escreve o conteúdo
    e remove automaticamente ao sair do contexto.
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
        yield temp.name  # <-- retorna o caminho
    finally:
        temp.close()
        os.remove(temp.name)
