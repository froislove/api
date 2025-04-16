from enum import Enum


class PoetryAPIRoutes(str, Enum):
    """
    <input field> from API reference
    """
    AUTHOR = '/author'
    TITLE = '/title'
    LINES = '/lines'
    LINECOUNT = '/linecount'
    POEMCOUNT = '/poemcount'

    def __str__(self) -> str:
        return self.value
