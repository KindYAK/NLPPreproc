from textblob import TextBlob


def process(news, args):
    for new in news[:1]:
        blob = TextBlob(new['text'])
        new['text_tokens'] = [{"token": str(token).lower()} for token in blob.words]

        blob = TextBlob(new['title'])
        new['title_tokens'] = [{"token": str(token).lower()} for token in blob.words]
    return news
