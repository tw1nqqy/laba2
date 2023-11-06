# импортируем все нужное
import uvicorn
from fastapi import FastAPI
from models import ArticleSumRequest, ArticleSumPost, ArticleRequest, ArticlePost, MetaRequest, MetaPost
import wikipedia

# создаем объект FastAPI
app = FastAPI(title='lab2')


# path запрос
@app.post('/database/{art}', response_model=ArticleSumRequest)
def get_article_summary(art: str):
    art_sum = wikipedia.summary(art)
    return ArticleSumPost(article=art,
                          summary=art_sum
                          )


# query запрос
@app.get('/', response_model=MetaRequest)
def get_meta(art: str):
    wiki = wikipedia.page(art)
    art_url = wiki.url
    art_cat = ' || '.join(wiki.categories)
    art_tags = ' || '.join(wiki.links)
    return MetaPost(article=art,
                    url=art_url,
                    category=art_cat,
                    tags=art_tags
                    )


# запрос с body
@app.post('/articles/', response_model=ArticleRequest)
def get_articles(article: ArticleRequest):
    wikipedia.set_lang(article.language)
    art = ' || '.join(wikipedia.search(article.articles, article.amount))
    return ArticlePost(language=article.language,
                       articles=art,
                       amount=article.amount
                       )


# шобы в консольку не писать каждый раз
if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
