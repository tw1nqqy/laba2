from pydantic import BaseModel, Field


class ArticleRequest(BaseModel):
    language: str = Field(min_lenght=2, max_lenght=2)
    articles: str = Field(min_lenght=1)
    amount: int


class ArticlePost(BaseModel):
    language: str = Field(min_lenght=2, max_lenght=2)
    articles: str = Field(min_lenght=1)
    amount: int


class MetaRequest(BaseModel):
    article: str = Field(min_lenght=1)
    url: str
    category: str
    tags: str


class MetaPost(BaseModel):
    article: str = Field(min_lenght=1)
    url: str
    category: str
    tags: str


class ArticleSumRequest(BaseModel):
    article: str = Field(min_lenght=1)
    summary: str


class ArticleSumPost(BaseModel):
    article: str = Field(min_lenght=1)
    summary: str
