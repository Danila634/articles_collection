import json


def get_articles():
    with open('articles.json', 'r', encoding='UTF-8') as f:
        articles = json.load(f)
        return articles


def save_article(name, text):
    with open('articles.json', 'r+', encoding='UTF-8') as f:
        article = json.load(f)
        article[name] = text

        f.seek(0)
        json.dump(article, f, ensure_ascii=False)
        f.truncate()


def delete_article(name):
    with open('articles.json', 'r', encoding='utf-8') as f:
        article = json.load(f)

        if name in article:
            del article[name]

    with open('articles.json', 'w', encoding='utf-8') as f:
        json                          .dump(article, f, ensure_ascii=False)
