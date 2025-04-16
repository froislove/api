from typing import List, Optional
from pydantic import BaseModel, field_validator
from models.query_enums import SearchTerm, SearchType, OutputField, ResponseFormat


class AuthorQueryParams(BaseModel):
    search_terms: Optional[List[SearchTerm]] = None
    search_type: Optional[SearchType] = None
    output_fields: Optional[List[OutputField]] = None
    format: Optional[ResponseFormat] = None

    @field_validator('output_fields', mode='before')
    @classmethod
    def validate_output_fields(cls, v):
        if v and OutputField.all in v and len(v) > 1:
            raise ValueError("'all' must not be combined with other fields")
        return v

    def to_url_path(self) -> str:
        base = f''
        if self.search_type:
            base += f":{self.search_type.value}"

        if self.search_terms:
            base += '/'
            base += ";".join(self.search_terms)

        if self.output_fields:
            if OutputField.all in self.output_fields:
                pass
            else:
                base += '/'
                base += ",".join([f.value for f in self.output_fields])

        if self.format:
            base += f".{self.format.value}"
        return base


class Author(BaseModel):
    author: str = None
    title: str = None
    lines: List[str] = None
    linecount: str = None


class AuthorAllFieldsPresence(BaseModel):
    author: str
    title: str
    lines: List[str]
    linecount: str


class Authors(BaseModel):
    authors: List[str] = None
