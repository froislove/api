from enum import Enum


class BaseQueryEnum(str, Enum):
    def __str__(self) -> str:
        return self.value


class SearchTerm(BaseQueryEnum):
    """
    <search term> query parameter
    """
    author = "author"
    title = "title"
    lines = "lines"
    linecount = "linecount"
    poemcount = "poemcount"
    random = 'random'


class SearchType(str, Enum):
    """
    <search type> query parameter
    """
    abs = "abs"  # Match <search term> exactly when searching <input field>

    def __str__(self) -> str:
        return self.value


class OutputField(str, Enum):
    """
    [/<output field>] query parameter
    """
    author = "author"
    title = "title"
    lines = "lines"
    linecount = "linecount"
    all = "all"


class ResponseFormat(str, Enum):
    """
    [.<format>] query parameter
    """
    json = "json"
    text = "text"
